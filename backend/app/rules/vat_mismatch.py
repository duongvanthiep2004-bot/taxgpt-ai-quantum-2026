from math import isfinite
from typing import Any


DEMO_RISK_LABEL = "CASE_3_VAT_CALC_MISMATCH"
CASE_ID = "CASE_3_VAT_MISMATCH"
RISK_TYPE = "possible_vat_calculation_mismatch"
SEVERITY = "medium"
MESSAGE = (
    "Số tiền VAT có dấu hiệu không khớp với phép tính kỹ thuật từ giá trị "
    "tính thuế và thuế suất, cần người dùng rà soát lại."
)


def _as_finite_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if isfinite(number) else None


def detect_vat_mismatch(
    invoices: list[dict], tolerance: float = 1.0
) -> list[dict]:
    """Return technical VAT calculation warnings for labelled MVP demo rows."""

    numeric_tolerance = _as_finite_float(tolerance)
    if numeric_tolerance is None or numeric_tolerance < 0:
        raise ValueError("tolerance phải là số hữu hạn không âm")

    alerts: list[dict] = []
    for invoice in invoices:
        risk_label = str(invoice.get("expected_risk_case") or "").strip().upper()
        if risk_label != DEMO_RISK_LABEL:
            continue

        taxable_amount = _as_finite_float(invoice.get("taxable_amount"))
        vat_rate = _as_finite_float(invoice.get("vat_rate"))
        vat_amount = _as_finite_float(invoice.get("vat_amount"))
        if taxable_amount is None or vat_rate is None or vat_amount is None:
            continue

        normalized_vat_rate = vat_rate / 100 if vat_rate > 1 else vat_rate
        recalculated_vat = taxable_amount * normalized_vat_rate
        difference = abs(vat_amount - recalculated_vat)
        if difference <= numeric_tolerance:
            continue

        alerts.append(
            {
                "case_id": CASE_ID,
                "risk_type": RISK_TYPE,
                "severity": SEVERITY,
                "message": MESSAGE,
                "invoice_id": invoice.get("invoice_id"),
                "evidence": {
                    "taxable_amount": taxable_amount,
                    "vat_rate": vat_rate,
                    "vat_amount": vat_amount,
                    "recalculated_vat": recalculated_vat,
                    "difference": difference,
                    "tolerance": numeric_tolerance,
                    "note": invoice.get("note"),
                },
            }
        )

    return alerts
