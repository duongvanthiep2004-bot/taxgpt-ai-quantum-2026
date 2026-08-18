from pathlib import Path

from fastapi import FastAPI, HTTPException

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
