from io import BytesIO
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from openpyxl import Workbook

from backend.app.main import app
from backend.app.parsers.excel_parser import (
    REQUIRED_INVOICE_COLUMNS,
    load_invoices_from_excel,
)
from backend.app.parsers.payment_parser import (
    REQUIRED_PAYMENT_COLUMNS,
    load_payments_from_excel,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INVOICE_FILE = PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
PAYMENT_FILE = (
    PROJECT_ROOT
    / "data-mau"
    / "bank_statements"
    / "sample_bank_payments_mvp.xlsx"
)
INVOICE_TEMPLATE_FILE = (
    PROJECT_ROOT / "data-mau" / "excel" / "template_invoices_mvp.xlsx"
)
PAYMENT_TEMPLATE_FILE = (
    PROJECT_ROOT
    / "data-mau"
    / "bank_statements"
    / "template_bank_payments_mvp.xlsx"
)
client = TestClient(app)
INVOICE_HEADERS = ["invoice_id", "invoice_no", "invoice_date", "total_amount"]
PAYMENT_HEADERS = [
    "payment_ref",
    "payment_date",
    "amount",
    "payment_method",
    "related_invoice_no",
]


def build_workbook(
    sheet_name: str,
    headers: list[str],
    rows: list[list[object]] | None = None,
) -> bytes:
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = sheet_name
    worksheet.append(headers)
    for row in rows or []:
        worksheet.append(row)
    output = BytesIO()
    workbook.save(output)
    return output.getvalue()


def post_invoice_workbook(invoice_workbook: bytes):
    with PAYMENT_FILE.open("rb") as payment_file:
        return client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    "invoices.xlsx",
                    invoice_workbook,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                "payment_file": (
                    PAYMENT_FILE.name,
                    payment_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )


def post_payment_workbook(payment_workbook: bytes):
    with INVOICE_FILE.open("rb") as invoice_file:
        return client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    INVOICE_FILE.name,
                    invoice_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                "payment_file": (
                    "payments.xlsx",
                    payment_workbook,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )


def test_excel_templates_are_readable_by_current_parsers() -> None:
    invoices = load_invoices_from_excel(str(INVOICE_TEMPLATE_FILE))
    payments = load_payments_from_excel(str(PAYMENT_TEMPLATE_FILE))

    assert len(invoices) == 1
    assert len(payments) == 1
    assert REQUIRED_INVOICE_COLUMNS <= set(invoices[0])
    assert {"taxable_amount", "vat_rate", "vat_amount"} <= set(invoices[0])
    assert "net_amount" not in invoices[0]
    assert invoices[0]["taxable_amount"] == 1_000_000
    assert invoices[0]["vat_rate"] == 0.1
    assert invoices[0]["vat_amount"] == 100_000
    assert set(payments[0]) == REQUIRED_PAYMENT_COLUMNS
    assert invoices[0]["invoice_id"].startswith("DEMO-")
    assert payments[0]["payment_ref"].startswith("DEMO-")


def test_scan_uploaded_rejects_invoice_with_header_only() -> None:
    response = post_invoice_workbook(build_workbook("invoices", INVOICE_HEADERS))

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: File hóa đơn không có dòng dữ liệu."
    )


def test_scan_uploaded_rejects_payment_with_header_only() -> None:
    response = post_payment_workbook(build_workbook("payments", PAYMENT_HEADERS))

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File thanh toán không hợp lệ: File thanh toán không có dòng dữ liệu."
    )


def test_scan_uploaded_rejects_blank_invoice_id() -> None:
    workbook = build_workbook(
        "invoices",
        INVOICE_HEADERS,
        [[None, "DEMO-0001", "2026-01-15", 1_000_000]],
    )
    response = post_invoice_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: "
        "File hóa đơn có dữ liệu trống ở cột bắt buộc: invoice_id"
    )


def test_scan_uploaded_rejects_blank_payment_amount() -> None:
    workbook = build_workbook(
        "payments",
        PAYMENT_HEADERS,
        [["DEMO-PAY-001", "2026-01-16", None, "bank_transfer", "DEMO-0001"]],
    )
    response = post_payment_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File thanh toán không hợp lệ: "
        "File thanh toán có dữ liệu trống ở cột bắt buộc: amount"
    )


def test_scan_uploaded_rejects_invalid_invoice_date() -> None:
    workbook = build_workbook(
        "invoices",
        INVOICE_HEADERS,
        [["DEMO-INV-001", "DEMO-0001", "not-a-date", 1_000_000]],
    )
    response = post_invoice_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: "
        "File hóa đơn có ngày không hợp lệ ở cột invoice_date."
    )


def test_scan_uploaded_rejects_invalid_payment_date() -> None:
    workbook = build_workbook(
        "payments",
        PAYMENT_HEADERS,
        [["DEMO-PAY-001", "not-a-date", 1_000_000, "bank_transfer", "DEMO-0001"]],
    )
    response = post_payment_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File thanh toán không hợp lệ: "
        "File thanh toán có ngày không hợp lệ ở cột payment_date."
    )


def test_scan_uploaded_rejects_invalid_invoice_total_amount() -> None:
    workbook = build_workbook(
        "invoices",
        INVOICE_HEADERS,
        [["DEMO-INV-001", "DEMO-0001", "2026-01-15", "not-a-number"]],
    )
    response = post_invoice_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: "
        "File hóa đơn có số tiền không hợp lệ ở cột total_amount."
    )


def test_scan_uploaded_rejects_invalid_payment_amount() -> None:
    workbook = build_workbook(
        "payments",
        PAYMENT_HEADERS,
        [["DEMO-PAY-001", "2026-01-16", "not-a-number", "bank_transfer", "DEMO-0001"]],
    )
    response = post_payment_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File thanh toán không hợp lệ: "
        "File thanh toán có số tiền không hợp lệ ở cột amount."
    )


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
    assert payload["case_summary"]["CASE_3_VAT_MISMATCH"]["total_alerts"] == 2
    assert {
        alert["invoice_id"]
        for alert in payload["alerts"]
        if alert["case_id"] == "CASE_3_VAT_MISMATCH"
    } == {"INV-DEMO-007", "INV-DEMO-008"}


def test_scan_uploaded_maps_net_amount_for_unlabelled_case_3_invoice() -> None:
    workbook = build_workbook(
        "invoices",
        [
            "invoice_id",
            "invoice_no",
            "invoice_date",
            "total_amount",
            "net_amount",
            "vat_rate",
            "vat_amount",
        ],
        [["INV-NET-001", "NET-0001", "2026-01-15", 1_090, 1_000, 10, 90]],
    )

    response = post_invoice_workbook(workbook)

    assert response.status_code == 200
    payload = response.json()
    assert payload["case_summary"]["CASE_3_VAT_MISMATCH"]["total_alerts"] == 1
    case_3_alerts = [
        alert
        for alert in payload["alerts"]
        if alert["case_id"] == "CASE_3_VAT_MISMATCH"
    ]
    assert len(case_3_alerts) == 1
    assert case_3_alerts[0]["invoice_id"] == "INV-NET-001"
    assert case_3_alerts[0]["evidence"]["taxable_amount"] == 1_000


def test_invoice_parser_keeps_net_amount_when_adding_taxable_amount(tmp_path: Path) -> None:
    workbook_path = tmp_path / "invoices.xlsx"
    workbook_path.write_bytes(
        build_workbook(
            "invoices",
            [
                "invoice_id",
                "invoice_no",
                "invoice_date",
                "total_amount",
                "net_amount",
                "vat_rate",
                "vat_amount",
            ],
            [["INV-NET-002", "NET-0002", "2026-01-15", 1_100, 1_000, 10, 100]],
        )
    )

    invoice = load_invoices_from_excel(str(workbook_path))[0]

    assert invoice["net_amount"] == 1_000
    assert invoice["taxable_amount"] == 1_000


def test_scan_uploaded_rejects_conflicting_taxable_and_net_amount() -> None:
    workbook = build_workbook(
        "invoices",
        [
            "invoice_id",
            "invoice_no",
            "invoice_date",
            "total_amount",
            "taxable_amount",
            "net_amount",
            "vat_rate",
            "vat_amount",
        ],
        [
            [
                "INV-CONFLICT-001",
                "CONFLICT-0001",
                "2026-01-15",
                1_100,
                1_000,
                900,
                10,
                100,
            ]
        ],
    )

    response = post_invoice_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: "
        "File hóa đơn có taxable_amount và net_amount không khớp nhau."
    )


def test_scan_uploaded_accepts_matching_taxable_and_net_amount() -> None:
    workbook = build_workbook(
        "invoices",
        [
            "invoice_id",
            "invoice_no",
            "invoice_date",
            "total_amount",
            "taxable_amount",
            "net_amount",
            "vat_rate",
            "vat_amount",
        ],
        [
            [
                "INV-MATCH-001",
                "MATCH-0001",
                "2026-01-15",
                1_090,
                1_000,
                1_000.0,
                10,
                90,
            ]
        ],
    )

    response = post_invoice_workbook(workbook)

    assert response.status_code == 200
    assert response.json()["case_summary"]["CASE_3_VAT_MISMATCH"]["total_alerts"] == 1


@pytest.mark.parametrize("column", ["taxable_amount", "net_amount", "vat_rate", "vat_amount"])
def test_scan_uploaded_rejects_invalid_optional_case_3_number(column: str) -> None:
    workbook = build_workbook(
        "invoices",
        ["invoice_id", "invoice_no", "invoice_date", "total_amount", column],
        [["INV-INVALID-001", "INVALID-0001", "2026-01-15", 1_100, "not-a-number"]],
    )

    response = post_invoice_workbook(workbook)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: "
        f"File hóa đơn có số tiền không hợp lệ ở cột {column}."
    )


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
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: Không đọc được file hóa đơn Excel."
    )


def test_scan_uploaded_rejects_invoice_without_invoices_sheet() -> None:
    with PAYMENT_FILE.open("rb") as payment_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    "invoices.xlsx",
                    build_workbook("other", ["invoice_id"]),
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
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: "
        "Không tìm thấy sheet invoices trong file hóa đơn."
    )


def test_scan_uploaded_rejects_payment_without_payments_sheet() -> None:
    with INVOICE_FILE.open("rb") as invoice_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    INVOICE_FILE.name,
                    invoice_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                "payment_file": (
                    "payments.xlsx",
                    build_workbook("other", ["payment_ref"]),
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File thanh toán không hợp lệ: "
        "Không tìm thấy sheet payments trong file thanh toán."
    )


def test_scan_uploaded_lists_missing_invoice_columns() -> None:
    invoice_workbook = build_workbook(
        "invoices",
        ["invoice_no", "invoice_date"],
    )
    with PAYMENT_FILE.open("rb") as payment_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    "invoices.xlsx",
                    invoice_workbook,
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
    assert response.json()["detail"] == (
        "File hóa đơn không hợp lệ: File hóa đơn thiếu các cột bắt buộc: "
        "invoice_id, total_amount"
    )


def test_scan_uploaded_lists_missing_payment_column() -> None:
    payment_workbook = build_workbook(
        "payments",
        [
            "payment_ref",
            "payment_date",
            "payment_method",
            "related_invoice_no",
        ],
    )
    with INVOICE_FILE.open("rb") as invoice_file:
        response = client.post(
            "/demo/scan-uploaded",
            files={
                "invoice_file": (
                    INVOICE_FILE.name,
                    invoice_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                "payment_file": (
                    "payments.xlsx",
                    payment_workbook,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "File thanh toán không hợp lệ: "
        "File thanh toán thiếu cột bắt buộc: amount"
    )


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
