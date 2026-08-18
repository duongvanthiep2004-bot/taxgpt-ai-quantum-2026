from math import isfinite
from typing import Any


DEMO_RISK_LABEL = "CASE_5_MISSING_NONCASH_PAYMENT"
CASE_ID = "CASE_5_MISSING_BANK_PAYMENT"
RISK_TYPE = "possible_missing_non_cash_payment_evidence"
SEVERITY = "medium"
MESSAGE = (
    "Chưa tìm thấy chứng từ thanh toán không dùng tiền mặt tương ứng trong "
    "dữ liệu được cung cấp, cần người dùng kiểm tra thêm."
)


def _normalize_reference(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().casefold()
    return normalized or None


def _as_finite_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if isfinite(number) else None


def detect_missing_bank_payment(
    invoices: list[dict],
    payments: list[dict],
    demo_threshold: float | None = None,
) -> list[dict]:
    """Return demo warnings when supplied payment data has no matching reference."""

    numeric_threshold = None
    if demo_threshold is not None:
        numeric_threshold = _as_finite_float(demo_threshold)
        if numeric_threshold is None or numeric_threshold < 0:
            raise ValueError("demo_threshold phải là số hữu hạn không âm")

    payment_references = {
        reference
        for payment in payments
        if (reference := _normalize_reference(payment.get("payment_ref"))) is not None
    }

    alerts: list[dict] = []
    for invoice in invoices:
        risk_label = str(invoice.get("expected_risk_case") or "").strip().upper()
        total_amount = _as_finite_float(invoice.get("total_amount"))
        exceeds_demo_threshold = (
            numeric_threshold is not None
            and total_amount is not None
            and total_amount >= numeric_threshold
        )
        if risk_label != DEMO_RISK_LABEL and not exceeds_demo_threshold:
            continue

        bank_payment_ref = invoice.get("bank_payment_ref")
        normalized_reference = _normalize_reference(bank_payment_ref)
        matched_payment_found = (
            normalized_reference is not None
            and normalized_reference in payment_references
        )
        if matched_payment_found:
            continue

        alerts.append(
            {
                "case_id": CASE_ID,
                "risk_type": RISK_TYPE,
                "severity": SEVERITY,
                "message": MESSAGE,
                "invoice_id": invoice.get("invoice_id"),
                "evidence": {
                    "total_amount": total_amount,
                    "payment_method": invoice.get("payment_method"),
                    "bank_payment_ref": bank_payment_ref,
                    "matched_payment_found": False,
                    "note": invoice.get("note"),
                },
            }
        )

    return alerts
