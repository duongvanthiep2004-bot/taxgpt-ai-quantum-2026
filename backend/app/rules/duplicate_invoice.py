from collections import defaultdict
from typing import Any


CASE_ID = "CASE_1_DUPLICATE_INVOICE"
RISK_TYPE = "possible_duplicate_invoice"
MESSAGE = (
    "Phát hiện nhóm hóa đơn có thông tin trùng nhau, "
    "cần người dùng kiểm tra chứng từ gốc."
)

BASE_KEY_FIELDS = ("invoice_no", "invoice_date", "total_amount")
OPTIONAL_KEY_FIELDS = ("invoice_symbol", "seller_tax_code")


def _normalize_key_value(value: Any) -> Any:
    if isinstance(value, str):
        normalized = value.strip()
        return normalized.casefold() if normalized else None
    return value


def detect_duplicate_invoices(invoices: list[dict]) -> list[dict]:
    """Return review warnings for invoice rows sharing the same technical key."""

    key_fields = list(BASE_KEY_FIELDS)
    for field in OPTIONAL_KEY_FIELDS:
        if any(invoice.get(field) not in (None, "") for invoice in invoices):
            key_fields.append(field)

    grouped_invoices: dict[tuple[Any, ...], list[dict]] = defaultdict(list)
    for invoice in invoices:
        normalized_key = tuple(
            _normalize_key_value(invoice.get(field)) for field in key_fields
        )
        if any(value is None for value in normalized_key):
            continue
        grouped_invoices[normalized_key].append(invoice)

    alerts: list[dict] = []
    for matches in grouped_invoices.values():
        if len(matches) < 2:
            continue

        matched_key = {field: matches[0].get(field) for field in key_fields}
        evidence = [
            {
                "invoice_id": invoice.get("invoice_id"),
                **{field: invoice.get(field) for field in key_fields},
            }
            for invoice in matches
        ]
        alerts.append(
            {
                "case_id": CASE_ID,
                "risk_type": RISK_TYPE,
                "severity": "medium",
                "message": MESSAGE,
                "matched_key": matched_key,
                "invoice_ids": [invoice.get("invoice_id") for invoice in matches],
                "evidence": evidence,
            }
        )

    return alerts
