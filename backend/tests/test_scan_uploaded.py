from pathlib import Path

from fastapi.testclient import TestClient

from backend.app.main import app


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INVOICE_FILE = PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
PAYMENT_FILE = (
    PROJECT_ROOT
    / "data-mau"
    / "bank_statements"
    / "sample_bank_payments_mvp.xlsx"
)
client = TestClient(app)


def test_scan_uploaded_returns_same_totals_as_demo() -> None:
    with INVOICE_FILE.open("rb") as invoice_file, PAYMENT_FILE.open("rb") as payment_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    INVOICE_FILE.name,
                    invoice_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                "payment_file": (
                    PAYMENT_FILE.name,
                    payment_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["total_invoices"] == 12
    assert payload["total_payments"] == 6
    assert payload["total_alerts"] == 9
    assert payload["uploaded_files"] == {
        "invoice_file": INVOICE_FILE.name,
        "payment_file": PAYMENT_FILE.name,
    }
    assert len(payload["case_summary"]) == 5
    assert len(payload["alerts"]) == 9


def test_scan_uploaded_rejects_non_xlsx_file() -> None:
    response = client.post(
        "/demo/scan-uploaded",
        files={
            "invoice_file": ("invoices.csv", b"invoice_id", "text/csv"),
            "payment_file": (
                "payments.xlsx",
                b"not needed for extension validation",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "File hóa đơn phải có định dạng .xlsx."


def test_scan_uploaded_returns_friendly_error_for_invalid_workbook() -> None:
    with PAYMENT_FILE.open("rb") as payment_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    "invoices.xlsx",
                    b"not an Excel workbook",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                "payment_file": (
                    PAYMENT_FILE.name,
                    payment_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )

    assert response.status_code == 400
    assert response.json()["detail"].startswith("File hóa đơn không hợp lệ:")


def test_scan_uploaded_requires_both_files() -> None:
    with INVOICE_FILE.open("rb") as invoice_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    INVOICE_FILE.name,
                    invoice_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
            },
        )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Vui lòng tải lên đủ file hóa đơn và file thanh toán."
    )
