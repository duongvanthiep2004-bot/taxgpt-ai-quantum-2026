from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)

EXPECTED_CASE_TOTALS = {
    "CASE_1_DUPLICATE_INVOICE": 1,
    "CASE_2_BUYER_INFO_MISMATCH": 2,
    "CASE_3_VAT_MISMATCH": 2,
    "CASE_4_OUT_OF_REVIEW_PERIOD": 2,
    "CASE_5_MISSING_BANK_PAYMENT": 2,
}
PROHIBITED_MESSAGE_PHRASES = {
    "vi phạm pháp luật",
    "gian lận",
    "hóa đơn vô hiệu",
    "hóa đơn không hợp lệ",
    "không được khấu trừ",
    "bị xử phạt",
    "bị loại chi phí",
    "ngưỡng pháp luật",
}


def test_scan_all_returns_aggregate_demo_result() -> None:
    response = client.get("/demo/scan-all")

    assert response.status_code == 200
    payload = response.json()
    assert {
        "status",
        "source_invoice_file",
        "source_payment_file",
        "total_invoices",
        "total_payments",
        "total_alerts",
        "case_summary",
        "alerts",
    }.issubset(payload)
    assert payload["status"] == "ok"
    assert payload["source_invoice_file"] == (
        "data-mau/excel/sample_invoices_mvp.xlsx"
    )
    assert payload["source_payment_file"] == (
        "data-mau/bank_statements/sample_bank_payments_mvp.xlsx"
    )
    assert payload["total_invoices"] == 12
    assert payload["total_payments"] == 6
    assert payload["total_alerts"] == 9

    case_summary = payload["case_summary"]
    assert set(case_summary) == set(EXPECTED_CASE_TOTALS)
    assert {
        case_id: summary["total_alerts"]
        for case_id, summary in case_summary.items()
    } == EXPECTED_CASE_TOTALS
    assert all(summary["case_name"] for summary in case_summary.values())

    alerts = payload["alerts"]
    assert len(alerts) == payload["total_alerts"]
    assert [alert["case_order"] for alert in alerts] == sorted(
        alert["case_order"] for alert in alerts
    )
    assert all("evidence" in alert for alert in alerts)
    for alert in alerts:
        message = alert["message"].casefold()
        assert not any(phrase in message for phrase in PROHIBITED_MESSAGE_PHRASES)
