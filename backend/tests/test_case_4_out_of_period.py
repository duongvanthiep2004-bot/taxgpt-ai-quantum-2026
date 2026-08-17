from datetime import date, datetime
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.parsers.excel_parser import load_invoices_from_excel
from backend.app.rules.out_of_review_period import detect_out_of_review_period


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_INVOICE_FILE = (
    PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
)
client = TestClient(app)


def test_case_4_rule_finds_expected_sample_invoices() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_out_of_review_period(invoices)

    assert len(alerts) == 2
    assert {alert["invoice_id"] for alert in alerts} == {
        "INV-DEMO-009",
        "INV-DEMO-010",
    }


def test_case_4_alerts_have_safe_required_fields() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_out_of_review_period(invoices)
    prohibited_phrases = (
        "vi phạm pháp luật",
        "kê khai sai",
        "bị xử phạt",
        "hóa đơn không hợp lệ",
        "hóa đơn vô hiệu",
    )

    assert alerts
    for alert in alerts:
        assert alert["case_id"] == "CASE_4_OUT_OF_REVIEW_PERIOD"
        assert alert["risk_type"] == "possible_out_of_review_period_invoice"
        assert alert["severity"] == "medium"
        assert alert["message"]
        assert not any(phrase in alert["message"].lower() for phrase in prohibited_phrases)
        assert alert["invoice_id"]
        assert set(alert["evidence"]) == {
            "invoice_date",
            "declaration_period",
            "review_period",
            "note",
        }


def test_case_4_rule_does_not_warn_for_invoice_in_same_period() -> None:
    invoices = [
        {
            "invoice_id": "INV-IN-PERIOD-001",
            "invoice_date": "2026-07-15",
            "declaration_period": "2026-07",
            "expected_risk_case": "CASE_4_OUTSIDE_REVIEW_PERIOD",
        }
    ]

    assert detect_out_of_review_period(invoices) == []


@pytest.mark.parametrize(
    "invoice_date",
    [date(2026, 8, 2), datetime(2026, 8, 2, 10, 30), "2026-08-02"],
)
def test_case_4_rule_accepts_supported_date_types(invoice_date: object) -> None:
    invoices = [
        {
            "invoice_id": "INV-DATE-TYPE-001",
            "invoice_date": invoice_date,
            "declaration_period": "2026-08",
            "expected_risk_case": "CASE_4_OUTSIDE_REVIEW_PERIOD",
        }
    ]

    alerts = detect_out_of_review_period(invoices, review_period="2026-07")

    assert len(alerts) == 1
    assert alerts[0]["evidence"]["invoice_date"] == "2026-08-02"
    assert alerts[0]["evidence"]["review_period"] == "2026-07"


def test_case_4_demo_api_returns_expected_payload() -> None:
    response = client.get("/demo/case-4-out-of-period")

    assert response.status_code == 200
    payload = response.json()
    assert set(payload) == {
        "status",
        "source_file",
        "total_invoices",
        "total_alerts",
        "alerts",
    }
    assert payload["status"] == "ok"
    assert payload["source_file"] == "data-mau/excel/sample_invoices_mvp.xlsx"
    assert payload["total_invoices"] == 12
    assert payload["total_alerts"] == 2
    assert isinstance(payload["alerts"], list)
