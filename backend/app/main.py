from pathlib import Path

from fastapi import FastAPI, HTTPException

from backend.app.parsers.excel_parser import InvoiceExcelError, load_invoices_from_excel
from backend.app.rules.buyer_info_mismatch import detect_buyer_info_mismatch
from backend.app.rules.duplicate_invoice import detect_duplicate_invoices


app = FastAPI(title="TaxGPT Backend")

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEMO_INVOICE_FILE = PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"


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
