from pathlib import Path

from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.parsers.excel_parser import load_invoices_from_excel
from backend.app.rules.vat_mismatch import detect_vat_mismatch


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_INVOICE_FILE = (
    PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
)
client = TestClient(app)


def test_case_3_rule_finds_expected_sample_invoices() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_vat_mismatch(invoices)

    assert len(alerts) == 2
    assert {alert["invoice_id"] for alert in alerts} == {
        "INV-DEMO-007",
        "INV-DEMO-008",
    }


def test_case_3_alerts_have_safe_required_fields() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_vat_mismatch(invoices)
    required_evidence = {
        "taxable_amount",
        "vat_rate",
        "vat_amount",
        "recalculated_vat",
        "difference",
        "tolerance",
        "note",
    }
    prohibited_phrases = (
        "vi phạm pháp luật",
        "không được khấu trừ",
        "bị xử phạt",
        "hóa đơn vô hiệu",
    )

    assert alerts
    for alert in alerts:
        assert alert["case_id"] == "CASE_3_VAT_MISMATCH"
        assert alert["risk_type"] == "possible_vat_calculation_mismatch"
        assert alert["severity"] == "medium"
        assert alert["message"]
        assert not any(phrase in alert["message"].lower() for phrase in prohibited_phrases)
        assert alert["invoice_id"]
        assert set(alert["evidence"]) == required_evidence


def test_case_3_rule_calculates_expected_sample_differences() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_vat_mismatch(invoices)
    evidence_by_invoice = {
        alert["invoice_id"]: alert["evidence"] for alert in alerts
    }

    assert evidence_by_invoice["INV-DEMO-007"]["recalculated_vat"] == 800_000
    assert evidence_by_invoice["INV-DEMO-007"]["difference"] == 100_000
    assert evidence_by_invoice["INV-DEMO-008"]["recalculated_vat"] == 960_000
    assert evidence_by_invoice["INV-DEMO-008"]["difference"] == 60_000


def test_case_3_rule_accepts_percentage_style_rate() -> None:
    invoices = [
        {
            "invoice_id": "INV-PERCENT-001",
            "taxable_amount": 1_000,
            "vat_rate": 10,
            "vat_amount": 90,
            "expected_risk_case": "CASE_3_VAT_CALC_MISMATCH",
            "note": "Dữ liệu kiểm thử thuế suất dạng phần trăm.",
        }
    ]

    alerts = detect_vat_mismatch(invoices)

    assert len(alerts) == 1
    assert alerts[0]["evidence"]["recalculated_vat"] == 100
    assert alerts[0]["evidence"]["difference"] == 10


def test_case_3_demo_api_returns_expected_payload() -> None:
    response = client.get("/demo/case-3-vat-mismatch")

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
