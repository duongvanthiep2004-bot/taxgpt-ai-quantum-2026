from datetime import date, datetime
from typing import Any


DEMO_RISK_LABEL = "CASE_4_OUTSIDE_REVIEW_PERIOD"
CASE_ID = "CASE_4_OUT_OF_REVIEW_PERIOD"
RISK_TYPE = "possible_out_of_review_period_invoice"
SEVERITY = "medium"
MESSAGE = (
    "Ngày hóa đơn có dấu hiệu nằm ngoài kỳ dữ liệu đang rà soát, "
    "cần người dùng kiểm tra lại kỳ dữ liệu hoặc kỳ kê khai phù hợp."
)


def _parse_invoice_date(value: Any) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        return None

    normalized = value.strip()
    if not normalized:
        return None
    try:
        return date.fromisoformat(normalized)
    except ValueError:
        try:
            return datetime.fromisoformat(normalized).date()
        except ValueError:
            return None


def _parse_review_period(value: Any) -> tuple[int, int] | None:
    if not isinstance(value, str):
        return None

    normalized = value.strip()
    try:
        parsed = datetime.strptime(normalized, "%Y-%m")
    except ValueError:
        return None
    return parsed.year, parsed.month


def detect_out_of_review_period(
    invoices: list[dict], review_period: str | None = None
) -> list[dict]:
    """Return review warnings for labelled invoices outside the selected month."""

    requested_period = None
    if review_period is not None:
        requested_period = _parse_review_period(review_period)
        if requested_period is None:
            raise ValueError("review_period phải có định dạng YYYY-MM")

    alerts: list[dict] = []
    for invoice in invoices:
        risk_label = str(invoice.get("expected_risk_case") or "").strip().upper()
        if risk_label != DEMO_RISK_LABEL:
            continue

        invoice_date = _parse_invoice_date(invoice.get("invoice_date"))
        row_period_value = invoice.get("declaration_period")
        effective_period = requested_period or _parse_review_period(row_period_value)
        if invoice_date is None or effective_period is None:
            continue
        if (invoice_date.year, invoice_date.month) == effective_period:
            continue

        effective_period_text = f"{effective_period[0]:04d}-{effective_period[1]:02d}"
        alerts.append(
            {
                "case_id": CASE_ID,
                "risk_type": RISK_TYPE,
                "severity": SEVERITY,
                "message": MESSAGE,
                "invoice_id": invoice.get("invoice_id"),
                "evidence": {
                    "invoice_date": invoice_date.isoformat(),
                    "declaration_period": row_period_value,
                    "review_period": effective_period_text,
                    "note": invoice.get("note"),
                },
            }
        )

    return alerts
