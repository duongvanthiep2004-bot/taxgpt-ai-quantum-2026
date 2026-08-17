from pathlib import Path

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.parsers.excel_parser import InvoiceExcelError, load_invoices_from_excel
from backend.app.rules.duplicate_invoice import detect_duplicate_invoices


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_INVOICE_FILE = (
    PROJECT_ROOT / "data-mau" / "excel" / "sample_invoices_mvp.xlsx"
)
client = TestClient(app)


def test_parser_loads_12_sample_invoices() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    assert len(invoices) == 12
    assert invoices[0]["invoice_id"] == "INV-DEMO-001"


def test_parser_rejects_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.xlsx"

    with pytest.raises(FileNotFoundError):
        load_invoices_from_excel(str(missing_file))


def test_parser_rejects_missing_invoice_sheet(tmp_path: Path) -> None:
    workbook = tmp_path / "wrong-sheet.xlsx"
    pd.DataFrame({"invoice_id": ["INV-001"]}).to_excel(
        workbook,
        sheet_name="other",
        index=False,
    )

    with pytest.raises(InvoiceExcelError, match="invoices"):
        load_invoices_from_excel(str(workbook))


def test_parser_rejects_missing_important_column(tmp_path: Path) -> None:
    workbook = tmp_path / "missing-column.xlsx"
    pd.DataFrame(
        {
            "invoice_id": ["INV-001"],
            "invoice_no": ["0001"],
            "invoice_date": ["2026-07-01"],
        }
    ).to_excel(workbook, sheet_name="invoices", index=False)

    with pytest.raises(InvoiceExcelError, match="total_amount"):
        load_invoices_from_excel(str(workbook))


def test_duplicate_rule_finds_sample_duplicate_group() -> None:
    invoices = load_invoices_from_excel(str(SAMPLE_INVOICE_FILE))

    alerts = detect_duplicate_invoices(invoices)

    assert len(alerts) == 1
    assert alerts[0]["risk_type"] == "possible_duplicate_invoice"
    assert set(alerts[0]["invoice_ids"]) == {"INV-DEMO-003", "INV-DEMO-004"}


def test_case_1_demo_api_returns_alerts() -> None:
    response = client.get("/demo/case-1-duplicates")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["total_invoices"] == 12
    assert payload["total_alerts"] == 1
    assert isinstance(payload["alerts"], list)
