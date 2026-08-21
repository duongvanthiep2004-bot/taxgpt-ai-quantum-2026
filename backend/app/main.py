from pathlib import Path
from tempfile import TemporaryDirectory

from fastapi import FastAPI, File, HTTPException, UploadFile

from backend.app.parsers.excel_parser import InvoiceExcelError, load_invoices_from_excel
from backend.app.parsers.payment_parser import PaymentExcelError, load_payments_from_excel
from backend.app.rules.buyer_info_mismatch import detect_buyer_info_mismatch
from backend.app.rules.duplicate_invoice import detect_duplicate_invoices
from backend.app.rules.missing_bank_payment import detect_missing_bank_payment
from backend.app.rules.out_of_review_period import detect_out_of_review_period
from backend.app.rules.vat_mismatch import detect_vat_mismatch


app = FastAPI(title="TaxGPT Backend")

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEMO_INVOICE_FILE = PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
DEMO_PAYMENT_FILE = (
    PROJECT_ROOT
    / "data-mau"
    / "bank_statements"
    / "sample_bank_payments_mvp.xlsx"
)
DEMO_INVOICE_SOURCE = "data-mau/excel/sample_invoices_mvp.xlsx"
DEMO_PAYMENT_SOURCE = "data-mau/bank_statements/sample_bank_payments_mvp.xlsx"
ALLOWED_UPLOAD_SUFFIX = ".xlsx"


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "TaxGPT backend"}


@app.get("/demo/case-1-duplicates")
def demo_case_1_duplicates() -> dict:
    try:
        invoices = load_invoices_from_excel(str(DEMO_INVOICE_FILE))
    except (FileNotFoundError, InvoiceExcelError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    alerts = detect_duplicate_invoices(invoices)
    return {
        "status": "ok",
        "source_file": "data-mau/excel/sample_invoices_mvp.xlsx",
        "total_invoices": len(invoices),
        "total_alerts": len(alerts),
        "alerts": alerts,
    }


@app.get("/demo/case-2-buyer-info")
def demo_case_2_buyer_info() -> dict:
    try:
        invoices = load_invoices_from_excel(str(DEMO_INVOICE_FILE))
    except (FileNotFoundError, InvoiceExcelError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    alerts = detect_buyer_info_mismatch(invoices)
    return {
        "status": "ok",
        "source_file": "data-mau/excel/sample_invoices_mvp.xlsx",
        "total_invoices": len(invoices),
        "total_alerts": len(alerts),
        "alerts": alerts,
    }


@app.get("/demo/case-3-vat-mismatch")
def demo_case_3_vat_mismatch() -> dict:
    try:
        invoices = load_invoices_from_excel(str(DEMO_INVOICE_FILE))
    except (FileNotFoundError, InvoiceExcelError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    alerts = detect_vat_mismatch(invoices)
    return {
        "status": "ok",
        "source_file": "data-mau/excel/sample_invoices_mvp.xlsx",
        "total_invoices": len(invoices),
        "total_alerts": len(alerts),
        "alerts": alerts,
    }


@app.get("/demo/case-4-out-of-period")
def demo_case_4_out_of_period() -> dict:
    try:
        invoices = load_invoices_from_excel(str(DEMO_INVOICE_FILE))
    except (FileNotFoundError, InvoiceExcelError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    alerts = detect_out_of_review_period(invoices)
    return {
        "status": "ok",
        "source_file": "data-mau/excel/sample_invoices_mvp.xlsx",
        "total_invoices": len(invoices),
        "total_alerts": len(alerts),
        "alerts": alerts,
    }


@app.get("/demo/case-5-missing-bank-payment")
def demo_case_5_missing_bank_payment() -> dict:
    try:
        invoices = load_invoices_from_excel(str(DEMO_INVOICE_FILE))
        payments = load_payments_from_excel(str(DEMO_PAYMENT_FILE))
    except (FileNotFoundError, InvoiceExcelError, PaymentExcelError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    alerts = detect_missing_bank_payment(invoices, payments)
    return {
        "status": "ok",
        "source_invoice_file": "data-mau/excel/sample_invoices_mvp.xlsx",
        "source_payment_file": (
            "data-mau/bank_statements/sample_bank_payments_mvp.xlsx"
        ),
        "total_invoices": len(invoices),
        "total_payments": len(payments),
        "total_alerts": len(alerts),
        "alerts": alerts,
    }


@app.get("/demo/scan-all")
def demo_scan_all() -> dict:
    try:
        invoices = load_invoices_from_excel(str(DEMO_INVOICE_FILE))
        payments = load_payments_from_excel(str(DEMO_PAYMENT_FILE))
    except (FileNotFoundError, InvoiceExcelError, PaymentExcelError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return build_scan_result(
        invoices,
        payments,
        source_invoice_file=DEMO_INVOICE_SOURCE,
        source_payment_file=DEMO_PAYMENT_SOURCE,
    )


def build_scan_result(
    invoices: list[dict],
    payments: list[dict],
    *,
    source_invoice_file: str,
    source_payment_file: str,
) -> dict:
    case_results = (
        (
            "CASE_1_DUPLICATE_INVOICE",
            "Hóa đơn trùng",
            detect_duplicate_invoices(invoices),
        ),
        (
            "CASE_2_BUYER_INFO_MISMATCH",
            "Sai MST/tên người mua",
            detect_buyer_info_mismatch(invoices),
        ),
        (
            "CASE_3_VAT_MISMATCH",
            "VAT không khớp phép tính",
            detect_vat_mismatch(invoices),
        ),
        (
            "CASE_4_OUT_OF_REVIEW_PERIOD",
            "Hóa đơn ngoài kỳ dữ liệu đang rà soát",
            detect_out_of_review_period(invoices),
        ),
        (
            "CASE_5_MISSING_BANK_PAYMENT",
            "Thiếu chứng từ thanh toán không dùng tiền mặt",
            detect_missing_bank_payment(invoices, payments),
        ),
    )

    case_summary: dict[str, dict] = {}
    alerts: list[dict] = []
    for case_order, (case_id, case_name, case_alerts) in enumerate(
        case_results, start=1
    ):
        case_summary[case_id] = {
            "case_name": case_name,
            "total_alerts": len(case_alerts),
        }
        alerts.extend({**alert, "case_order": case_order} for alert in case_alerts)

    def alert_sort_key(alert: dict) -> tuple[int, str]:
        invoice_id = alert.get("invoice_id")
        if invoice_id is None:
            invoice_ids = alert.get("invoice_ids") or []
            invoice_id = invoice_ids[0] if invoice_ids else ""
        return int(alert["case_order"]), str(invoice_id)

    alerts.sort(key=alert_sort_key)
    return {
        "status": "ok",
        "source_invoice_file": source_invoice_file,
        "source_payment_file": source_payment_file,
        "total_invoices": len(invoices),
        "total_payments": len(payments),
        "total_alerts": len(alerts),
        "case_summary": case_summary,
        "alerts": alerts,
    }


def _validate_xlsx_upload(upload: UploadFile, label: str) -> str:
    filename = Path(upload.filename or "").name
    if not filename:
        raise HTTPException(status_code=400, detail=f"Thiếu tên file {label}.")
    if Path(filename).suffix.casefold() != ALLOWED_UPLOAD_SUFFIX:
        raise HTTPException(
            status_code=400,
            detail=f"File {label} phải có định dạng .xlsx.",
        )
    return filename


@app.post("/demo/scan-uploaded")
async def scan_uploaded_files(
    invoice_file: UploadFile | None = File(default=None),
    payment_file: UploadFile | None = File(default=None),
) -> dict:
    if invoice_file is None or payment_file is None:
        raise HTTPException(
            status_code=400,
            detail="Vui lòng tải lên đủ file hóa đơn và file thanh toán.",
        )

    invoice_filename = _validate_xlsx_upload(invoice_file, "hóa đơn")
    payment_filename = _validate_xlsx_upload(payment_file, "thanh toán")

    with TemporaryDirectory(prefix="taxgpt-upload-") as temporary_directory:
        temporary_path = Path(temporary_directory)
        invoice_path = temporary_path / "invoices.xlsx"
        payment_path = temporary_path / "payments.xlsx"
        invoice_path.write_bytes(await invoice_file.read())
        payment_path.write_bytes(await payment_file.read())

        try:
            invoices = load_invoices_from_excel(str(invoice_path))
        except (FileNotFoundError, InvoiceExcelError) as exc:
            raise HTTPException(
                status_code=400,
                detail=f"File hóa đơn không hợp lệ: {exc}",
            ) from exc

        try:
            payments = load_payments_from_excel(str(payment_path))
        except (FileNotFoundError, PaymentExcelError) as exc:
            raise HTTPException(
                status_code=400,
                detail=f"File thanh toán không hợp lệ: {exc}",
            ) from exc

    result = build_scan_result(
        invoices,
        payments,
        source_invoice_file=invoice_filename,
        source_payment_file=payment_filename,
    )
    result["uploaded_files"] = {
        "invoice_file": invoice_filename,
        "payment_file": payment_filename,
    }
    return result
