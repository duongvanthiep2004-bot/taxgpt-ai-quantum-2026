import json

import httpx
import pandas as pd
import streamlit as st


SCAN_ALL_URL = "http://127.0.0.1:8000/demo/scan-all"
BACKEND_NOT_RUNNING_MESSAGE = (
    "Backend chưa chạy. Vui lòng chạy "
    "uvicorn backend.app.main:app --reload"
)


def fetch_scan_all() -> dict | None:
    try:
        response = httpx.get(SCAN_ALL_URL, timeout=10.0)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError:
        st.error(BACKEND_NOT_RUNNING_MESSAGE)
    except httpx.HTTPStatusError as exc:
        st.error(f"Backend trả về lỗi HTTP {exc.response.status_code}.")
    except ValueError:
        st.error("Backend trả về dữ liệu không đúng định dạng JSON.")
    return None


def build_case_summary_table(case_summary: dict) -> pd.DataFrame:
    rows = [
        {
            "case_id": case_id,
            "case_name": summary.get("case_name", ""),
            "total_alerts": summary.get("total_alerts", 0),
        }
        for case_id, summary in case_summary.items()
    ]
    return pd.DataFrame(rows)


def build_alerts_table(alerts: list[dict]) -> pd.DataFrame:
    rows = []
    for alert in alerts:
        invoice_reference = alert.get("invoice_id")
        if not invoice_reference:
            invoice_reference = ", ".join(
                str(invoice_id) for invoice_id in alert.get("invoice_ids", [])
            )
        rows.append(
            {
                "case_id": alert.get("case_id", ""),
                "risk_type": alert.get("risk_type", ""),
                "severity": alert.get("severity", ""),
                "invoice_id hoặc invoice_ids": invoice_reference,
                "message": alert.get("message", ""),
                "evidence": json.dumps(
                    alert.get("evidence", {}), ensure_ascii=False, default=str
                ),
            }
        )
    return pd.DataFrame(rows)


st.set_page_config(page_title="TaxGPT Dashboard", layout="wide")
st.title("TaxGPT Dashboard")
st.write("Rà soát 5 nhóm rủi ro trên bộ dữ liệu Excel demo.")
st.info(
    "TaxGPT chỉ hỗ trợ rà soát rủi ro và không thay thế kế toán, luật sư, "
    "đại lý thuế hoặc cơ quan thuế."
)

if st.button("Chạy rà soát dữ liệu demo", type="primary"):
    with st.spinner("Đang gọi backend và rà soát dữ liệu demo..."):
        result = fetch_scan_all()

    if result is not None:
        invoice_metric, payment_metric, alert_metric = st.columns(3)
        invoice_metric.metric("Tổng số hóa đơn", result.get("total_invoices", 0))
        payment_metric.metric(
            "Tổng số giao dịch thanh toán", result.get("total_payments", 0)
        )
        alert_metric.metric("Tổng số cảnh báo", result.get("total_alerts", 0))

        st.subheader("Tổng hợp theo 5 case")
        st.dataframe(
            build_case_summary_table(result.get("case_summary", {})),
            width="stretch",
            hide_index=True,
        )

        st.subheader("Chi tiết cảnh báo")
        st.dataframe(
            build_alerts_table(result.get("alerts", [])),
            width="stretch",
            hide_index=True,
        )
