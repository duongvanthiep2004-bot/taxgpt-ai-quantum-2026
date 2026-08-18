from datetime import date, datetime
from pathlib import Path
from zipfile import BadZipFile

import pandas as pd
from openpyxl.utils.exceptions import InvalidFileException


PAYMENT_SHEET_NAME = "payments"
HEADER_SCAN_LIMIT = 25
REQUIRED_PAYMENT_COLUMNS = {
    "payment_ref",
    "payment_date",
    "amount",
    "payment_method",
    "related_invoice_no",
}


class PaymentExcelError(ValueError):
    """Raised when a payment workbook cannot be parsed safely."""


def _find_header_row(preview: pd.DataFrame) -> int:
    for row_index, row in preview.iterrows():
        values = {
            str(value).strip()
            for value in row.tolist()
            if pd.notna(value)
        }
        if "payment_ref" in values:
            return int(row_index)

    raise PaymentExcelError("Không tìm thấy dòng header chứa cột 'payment_ref'")


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


def load_payments_from_excel(file_path: str) -> list[dict]:
    """Load payment rows from the bank payment Excel workbook."""

    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file thanh toán: {path}")

    try:
        preview = pd.read_excel(
            path,
            sheet_name=PAYMENT_SHEET_NAME,
            header=None,
            nrows=HEADER_SCAN_LIMIT,
        )
        header_row = _find_header_row(preview)
        payments_frame = pd.read_excel(
            path,
            sheet_name=PAYMENT_SHEET_NAME,
            header=header_row,
        )
    except PaymentExcelError:
        raise
    except (ValueError, OSError, BadZipFile, InvalidFileException) as exc:
        raise PaymentExcelError(
            f"Không đọc được sheet '{PAYMENT_SHEET_NAME}' từ file {path}: {exc}"
        ) from exc

    payments_frame.columns = [str(column).strip() for column in payments_frame.columns]
    missing_columns = REQUIRED_PAYMENT_COLUMNS - set(payments_frame.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise PaymentExcelError(f"Thiếu cột thanh toán bắt buộc: {missing}")

    payments_frame = payments_frame.dropna(how="all")
    return [
        {column: _to_python_value(value) for column, value in row.items()}
        for row in payments_frame.to_dict(orient="records")
    ]
