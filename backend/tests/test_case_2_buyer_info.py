from pathlib import Path

from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.parsers.excel_parser import load_invoices_from_excel
from backend.app.rules.buyer_info_mismatch import detect_buyer_info_mismatch


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_INVOICE_FILE = (
    PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
)
client = TestClient(app)


def test_case_2_rule_finds_expected_sample_invoices() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_buyer_info_mismatch(invoices)

    assert len(alerts) == 2
    assert {alert["invoice_id"] for alert in alerts} == {
        "INV-DEMO-005",
        "INV-DEMO-006",
    }


def test_case_2_alerts_have_safe_required_fields() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_buyer_info_mismatch(invoices)
    prohibited_phrases = (
        "hóa đơn sai pháp luật",
        "hóa đơn vô hiệu",
        "không được khấu trừ",
        "bị xử phạt",
    )

    assert alerts
    for alert in alerts:
        assert alert["case_id"] == "CASE_2_BUYER_INFO_MISMATCH"
        assert alert["risk_type"] == "possible_buyer_info_mismatch"
        assert alert["severity"] == "medium"
        assert alert["message"]
        assert not any(phrase in alert["message"].lower() for phrase in prohibited_phrases)
        assert alert["invoice_id"]
        assert set(alert["evidence"]) == {"buyer_tax_code", "buyer_name", "note"}


def test_case_2_rule_ignores_unlabelled_invoice() -> None:
    invoices = [
        {
            "invoice_id": "INV-NORMAL-001",
            "buyer_tax_code": "BUYER-001",
            "buyer_name": "Doanh nghiệp mẫu",
            "expected_risk_case": "NORMAL",
        }
    ]

    assert detect_buyer_info_mismatch(invoices) == []


def test_case_2_demo_api_returns_expected_payload() -> None:
    response = client.get("/demo/case-2-buyer-info")

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
