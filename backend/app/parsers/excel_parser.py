from datetime import date, datetime
from pathlib import Path
from zipfile import BadZipFile

import pandas as pd
from openpyxl.utils.exceptions import InvalidFileException


INVOICE_SHEET_NAME = "invoices"
HEADER_SCAN_LIMIT = 25
REQUIRED_INVOICE_COLUMNS = {
    "invoice_id",
    "invoice_no",
    "invoice_date",
    "total_amount",
}


class InvoiceExcelError(ValueError):
    """Raised when an invoice workbook cannot be parsed safely."""


def _find_header_row(preview: pd.DataFrame) -> int:
    for row_index, row in preview.iterrows():
        values = {
            str(value).strip()
            for value in row.tolist()
            if pd.notna(value)
        }
        if "invoice_id" in values:
            return int(row_index)

    raise InvoiceExcelError("Không tìm thấy dòng header chứa cột 'invoice_id'")


def _to_python_value(value: object) -> object:
    if pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date().isoformat()
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if hasattr(value, "item"):
        return value.item()
    return value


def load_invoices_from_excel(file_path: str) -> list[dict]:
    """Load invoice rows from the sample Excel workbook."""

    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file hóa đơn: {path}")

    try:
        preview = pd.read_excel(
            path,
            sheet_name=INVOICE_SHEET_NAME,
            header=None,
            nrows=HEADER_SCAN_LIMIT,
        )
        header_row = _find_header_row(preview)
        invoices_frame = pd.read_excel(
            path,
            sheet_name=INVOICE_SHEET_NAME,
            header=header_row,
        )
    except InvoiceExcelError:
        raise
    except (ValueError, OSError, BadZipFile, InvalidFileException) as exc:
        raise InvoiceExcelError(
            f"Không đọc được sheet '{INVOICE_SHEET_NAME}' từ file {path}: {exc}"
        ) from exc

    invoices_frame.columns = [str(column).strip() for column in invoices_frame.columns]
    missing_columns = REQUIRED_INVOICE_COLUMNS - set(invoices_frame.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise InvoiceExcelError(f"Thiếu cột hóa đơn bắt buộc: {missing}")

    invoices_frame = invoices_frame.dropna(how="all")
    return [
        {column: _to_python_value(value) for column, value in row.items()}
        for row in invoices_frame.to_dict(orient="records")
    ]
