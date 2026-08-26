from datetime import date, datetime
from math import isfinite
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
REQUIRED_PAYMENT_VALUE_COLUMNS = (
    "payment_ref",
    "payment_date",
    "amount",
)


class PaymentExcelError(ValueError):
    """Raised when a payment workbook cannot be parsed safely."""


def _find_header_row(preview: pd.DataFrame) -> int:
    best_row_index: int | None = None
    best_match_count = 0
    for row_index, row in preview.iterrows():
        values = {
            str(value).strip()
            for value in row.tolist()
            if pd.notna(value)
        }
        match_count = len(values & REQUIRED_PAYMENT_COLUMNS)
        if match_count > best_match_count:
            best_row_index = int(row_index)
            best_match_count = match_count

    if best_row_index is not None:
        return best_row_index
    raise PaymentExcelError("Không tìm thấy dòng header phù hợp trong file thanh toán.")


def _missing_columns_message(missing_columns: set[str]) -> str:
    missing = ", ".join(sorted(missing_columns))
    if len(missing_columns) == 1:
        return f"File thanh toán thiếu cột bắt buộc: {missing}"
    return f"File thanh toán thiếu các cột bắt buộc: {missing}"


def _is_blank(value: object) -> bool:
    return bool(pd.isna(value)) or (
        isinstance(value, str) and not value.strip()
    )


def _parse_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not isinstance(value, str) or not value.strip():
        return None

    parsed = pd.to_datetime(value.strip(), errors="coerce")
    if pd.isna(parsed):
        return None
    return parsed.date()


def _parse_number(value: object) -> int | float | None:
    if isinstance(value, bool):
        return None
    parsed = pd.to_numeric(value, errors="coerce")
    if pd.isna(parsed) or not isfinite(float(parsed)):
        return None
    return parsed.item() if hasattr(parsed, "item") else parsed


def _validate_payment_data(payments_frame: pd.DataFrame) -> pd.DataFrame:
    payments_frame = payments_frame.dropna(how="all").copy()
    if payments_frame.empty:
        raise PaymentExcelError("File thanh toán không có dòng dữ liệu.")

    for column in REQUIRED_PAYMENT_VALUE_COLUMNS:
        if payments_frame[column].map(_is_blank).any():
            raise PaymentExcelError(
                f"File thanh toán có dữ liệu trống ở cột bắt buộc: {column}"
            )

    parsed_dates = payments_frame["payment_date"].map(_parse_date)
    if parsed_dates.isna().any():
        raise PaymentExcelError(
            "File thanh toán có ngày không hợp lệ ở cột payment_date."
        )
    payments_frame["payment_date"] = parsed_dates

    parsed_amounts = payments_frame["amount"].map(_parse_number)
    if parsed_amounts.isna().any():
        raise PaymentExcelError(
            "File thanh toán có số tiền không hợp lệ ở cột amount."
        )
    payments_frame["amount"] = parsed_amounts

    return payments_frame


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
        with pd.ExcelFile(path, engine="openpyxl") as workbook:
            if PAYMENT_SHEET_NAME not in workbook.sheet_names:
                raise PaymentExcelError(
                    "Không tìm thấy sheet payments trong file thanh toán."
                )
            preview = pd.read_excel(
                workbook,
                sheet_name=PAYMENT_SHEET_NAME,
                header=None,
                nrows=HEADER_SCAN_LIMIT,
            )
            header_row = _find_header_row(preview)
            payments_frame = pd.read_excel(
                workbook,
                sheet_name=PAYMENT_SHEET_NAME,
                header=header_row,
            )
    except PaymentExcelError:
        raise
    except (ValueError, OSError, BadZipFile, InvalidFileException) as exc:
        raise PaymentExcelError("Không đọc được file thanh toán Excel.") from exc

    payments_frame.columns = [str(column).strip() for column in payments_frame.columns]
    missing_columns = REQUIRED_PAYMENT_COLUMNS - set(payments_frame.columns)
    if missing_columns:
        raise PaymentExcelError(_missing_columns_message(missing_columns))

    payments_frame = _validate_payment_data(payments_frame)
    return [
        {column: _to_python_value(value) for column, value in row.items()}
        for row in payments_frame.to_dict(orient="records")
    ]
