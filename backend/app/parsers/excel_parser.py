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
    best_row_index: int | None = None
    best_match_count = 0
    for row_index, row in preview.iterrows():
        values = {
            str(value).strip()
            for value in row.tolist()
            if pd.notna(value)
        }
        match_count = len(values & REQUIRED_INVOICE_COLUMNS)
        if match_count > best_match_count:
            best_row_index = int(row_index)
            best_match_count = match_count

    if best_row_index is not None:
        return best_row_index
    raise InvoiceExcelError("Không tìm thấy dòng header phù hợp trong file hóa đơn.")


def _missing_columns_message(missing_columns: set[str]) -> str:
    missing = ", ".join(sorted(missing_columns))
    if len(missing_columns) == 1:
        return f"File hóa đơn thiếu cột bắt buộc: {missing}"
    return f"File hóa đơn thiếu các cột bắt buộc: {missing}"


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
        with pd.ExcelFile(path, engine="openpyxl") as workbook:
            if INVOICE_SHEET_NAME not in workbook.sheet_names:
                raise InvoiceExcelError(
                    "Không tìm thấy sheet invoices trong file hóa đơn."
                )
            preview = pd.read_excel(
                workbook,
                sheet_name=INVOICE_SHEET_NAME,
                header=None,
                nrows=HEADER_SCAN_LIMIT,
            )
            header_row = _find_header_row(preview)
            invoices_frame = pd.read_excel(
                workbook,
                sheet_name=INVOICE_SHEET_NAME,
                header=header_row,
            )
    except InvoiceExcelError:
        raise
    except (ValueError, OSError, BadZipFile, InvalidFileException) as exc:
        raise InvoiceExcelError("Không đọc được file hóa đơn Excel.") from exc

    invoices_frame.columns = [str(column).strip() for column in invoices_frame.columns]
    missing_columns = REQUIRED_INVOICE_COLUMNS - set(invoices_frame.columns)
    if missing_columns:
        raise InvoiceExcelError(_missing_columns_message(missing_columns))

    invoices_frame = invoices_frame.dropna(how="all")
    return [
        {column: _to_python_value(value) for column, value in row.items()}
        for row in invoices_frame.to_dict(orient="records")
    ]
