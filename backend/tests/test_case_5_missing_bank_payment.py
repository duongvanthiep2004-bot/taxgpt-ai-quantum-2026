from pathlib import Path

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.parsers.excel_parser import load_invoices_from_excel
from backend.app.parsers.payment_parser import PaymentExcelError, load_payments_from_excel
from backend.app.rules.missing_bank_payment import detect_missing_bank_payment


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_INVOICE_FILE = (
    PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
)
SAMPLE_PAYMENT_FILE = (
    PROJECT_ROOT
    / "data-mau"
    / "bank_statements"
    / "sample_bank_payments_mvp.xlsx"
)
client = TestClient(app)


def test_payment_parser_loads_6_sample_payments() -> None:
    payments = load_payments_from_excel(str(SAMPLE_PAYMENT_FILE))

    assert len(payments) == 6
    assert payments[0]["payment_ref"] == "PAY-DEMO-001"
    assert payments[0]["payment_date"] == "2026-07-03"


def test_payment_parser_rejects_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_payments_from_excel(str(tmp_path / "missing.xlsx"))


def test_payment_parser_rejects_missing_payment_sheet(tmp_path: Path) -> None:
    workbook = tmp_path / "wrong-sheet.xlsx"
    pd.DataFrame({"payment_ref": ["PAY-001"]}).to_excel(
        workbook,
        sheet_name="other",
        index=False,
    )

    with pytest.raises(PaymentExcelError, match="payments"):
        load_payments_from_excel(str(workbook))


def test_payment_parser_rejects_missing_important_column(tmp_path: Path) -> None:
    workbook = tmp_path / "missing-column.xlsx"
    pd.DataFrame(
        {
            "payment_ref": ["PAY-001"],
            "payment_date": ["2026-07-01"],
            "payment_method": ["Chuyển khoản"],
            "related_invoice_no": ["INV-001"],
        }
    ).to_excel(workbook, sheet_name="payments", index=False)

    with pytest.raises(PaymentExcelError, match="amount"):
        load_payments_from_excel(str(workbook))


def test_case_5_rule_finds_expected_sample_invoices() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))
    payments = load_payments_from_excel(str(SAMPLE_PAYMENT_FILE))

    alerts = detect_missing_bank_payment(invoices, payments)

    assert len(alerts) == 2
    assert {alert["invoice_id"] for alert in alerts} == {
        "INV-DEMO-011",
        "INV-DEMO-012",
    }


def test_case_5_alerts_have_safe_required_fields() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))
    payments = load_payments_from_excel(str(SAMPLE_PAYMENT_FILE))

    alerts = detect_missing_bank_payment(invoices, payments)
    prohibited_phrases = (
        "vi phạm pháp luật",
        "không được khấu trừ",
        "bị xử phạt",
        "bị loại chi phí",
        "hóa đơn không hợp lệ",
        "hóa đơn vô hiệu",
        "ngưỡng pháp luật",
    )

    assert alerts
    for alert in alerts:
        assert alert["case_id"] == "CASE_5_MISSING_BANK_PAYMENT"
        assert alert["risk_type"] == "possible_missing_non_cash_payment_evidence"
        assert alert["severity"] == "medium"
        assert alert["message"]
        assert not any(phrase in alert["message"].lower() for phrase in prohibited_phrases)
        assert alert["invoice_id"]
        assert set(alert["evidence"]) == {
            "total_amount",
            "payment_method",
            "bank_payment_ref",
            "matched_payment_found",
            "note",
        }
        assert alert["evidence"]["matched_payment_found"] is False


def test_case_5_rule_does_not_warn_when_payment_reference_matches() -> None:
    invoices = [
        {
            "invoice_id": "INV-MATCHED-001",
            "total_amount": 50_000,
            "payment_method": "Chuyển khoản",
            "bank_payment_ref": "PAY-MATCHED-001",
            "expected_risk_case": "CASE_5_MISSING_NONCASH_PAYMENT",
        }
    ]
    payments = [{"payment_ref": "PAY-MATCHED-001"}]

    assert detect_missing_bank_payment(invoices, payments) == []


def test_case_5_rule_can_use_demo_threshold_for_unlabelled_invoice() -> None:
    invoices = [
        {
            "invoice_id": "INV-THRESHOLD-001",
            "total_amount": 50_000,
            "payment_method": "Chuyển khoản",
            "bank_payment_ref": None,
            "expected_risk_case": "NORMAL",
        }
    ]

    alerts = detect_missing_bank_payment(invoices, [], demo_threshold=10_000)

    assert len(alerts) == 1
    assert alerts[0]["invoice_id"] == "INV-THRESHOLD-001"


def test_case_5_demo_api_returns_expected_payload() -> None:
    response = client.get("/demo/case-5-missing-bank-payment")

    assert response.status_code == 200
    payload = response.json()
    assert set(payload) == {
        "status",
        "source_invoice_file",
        "source_payment_file",
        "total_invoices",
        "total_payments",
        "total_alerts",
        "alerts",
    }
    assert payload["status"] == "ok"
    assert payload["source_invoice_file"] == (
        "data-mau/excel/sample_invoices_mvp.xlsx"
    )
    assert payload["source_payment_file"] == (
        "data-mau/bank_statements/sample_bank_payments_mvp.xlsx"
    )
    assert payload["total_invoices"] == 12
    assert payload["total_payments"] == 6
    assert payload["total_alerts"] == 2
    assert isinstance(payload["alerts"], list)
