CASE_ID = "CASE_2_BUYER_INFO_MISMATCH"
RISK_TYPE = "possible_buyer_info_mismatch"
SEVERITY = "medium"
MESSAGE = (
    "Thông tin người mua có dấu hiệu không khớp hoặc cần rà soát lại "
    "với hồ sơ tham chiếu."
)


def detect_buyer_info_mismatch(invoices: list[dict]) -> list[dict]:
    """Build Case 2 warnings from the explicit label in the MVP demo dataset.

    A future business rule must accept a verified buyer reference profile instead
    of inferring the correct tax code or company name from invoice rows.
    """

    alerts: list[dict] = []
    for invoice in invoices:
        risk_label = str(invoice.get("expected_risk_case") or "").strip().upper()
        if risk_label != CASE_ID:
            continue

        alerts.append(
            {
                "case_id": CASE_ID,
                "risk_type": RISK_TYPE,
                "severity": SEVERITY,
                "message": MESSAGE,
                "invoice_id": invoice.get("invoice_id"),
                "evidence": {
                    "buyer_tax_code": invoice.get("buyer_tax_code"),
                    "buyer_name": invoice.get("buyer_name"),
                    "note": invoice.get("note"),
                },
            }
        )

    return alerts
