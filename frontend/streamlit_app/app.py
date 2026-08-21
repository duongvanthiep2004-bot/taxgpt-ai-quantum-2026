import httpx
import pandas as pd
import streamlit as st


SCAN_ALL_URL = "http://127.0.0.1:8000/demo/scan-all"
SCAN_UPLOADED_URL = "http://127.0.0.1:8000/demo/scan-uploaded"
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


def scan_uploaded_files(invoice_file, payment_file) -> dict | None:
    files = {
        "invoice_file": (
            invoice_file.name,
            invoice_file.getvalue(),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ),
        "payment_file": (
            payment_file.name,
            payment_file.getvalue(),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ),
    }
    try:
        response = httpx.post(SCAN_UPLOADED_URL, files=files, timeout=30.0)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError:
        st.error(BACKEND_NOT_RUNNING_MESSAGE)
    except httpx.HTTPStatusError as exc:
        try:
            detail = exc.response.json().get("detail")
        except ValueError:
            detail = None
        st.error(detail or f"Backend trả về lỗi HTTP {exc.response.status_code}.")
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


def get_invoice_reference(alert: dict) -> str:
    invoice_id = alert.get("invoice_id")
    if invoice_id:
        return str(invoice_id)
    return ", ".join(
        str(invoice_id) for invoice_id in alert.get("invoice_ids", [])
    )


def build_alerts_table(alerts: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "case_id": alert.get("case_id", ""),
                "risk_type": alert.get("risk_type", ""),
                "severity": alert.get("severity", ""),
                "invoice_id hoặc invoice_ids": get_invoice_reference(alert),
                "message": alert.get("message", ""),
            }
            for alert in alerts
        ]
    )


st.set_page_config(page_title="TaxGPT Dashboard", layout="wide")
st.title("TaxGPT Dashboard")
st.write("Rà soát 5 nhóm rủi ro trên dữ liệu Excel demo hoặc file tải lên.")
st.info(
    "TaxGPT chỉ hỗ trợ rà soát rủi ro và không thay thế kế toán, luật sư, "
    "đại lý thuế hoặc cơ quan thuế."
)

with st.expander("Cách chạy demo local"):
    st.markdown("**1. Chạy backend:**")
    st.code("uvicorn backend.app.main:app --reload", language="bash")
    st.markdown("**2. Chạy frontend:**")
    st.code("streamlit run frontend/streamlit_app/app.py", language="bash")
    st.warning("Cần bật backend trước khi bấm nút rà soát dữ liệu demo.")

st.subheader("Chế độ 1: Dữ liệu demo cố định")
st.caption("Dùng hai file mẫu có sẵn trong repo để chạy nhanh luồng demo.")
if st.button("Chạy rà soát dữ liệu demo", type="primary"):
    with st.spinner("Đang gọi backend và rà soát dữ liệu demo..."):
        scan_result = fetch_scan_all()
    if scan_result is None:
        st.session_state.pop("scan_result", None)
    else:
        st.session_state["scan_result"] = scan_result

st.divider()
st.subheader("Chế độ 2: File Excel tải lên")
st.caption("Rà soát file Excel tải lên theo sheet, header và schema hiện tại.")
upload_invoice_column, upload_payment_column = st.columns(2)
uploaded_invoice_file = upload_invoice_column.file_uploader(
    "File hóa đơn Excel (.xlsx)",
    type=["xlsx"],
    key="uploaded_invoice_file",
)
uploaded_payment_file = upload_payment_column.file_uploader(
    "File thanh toán Excel (.xlsx)",
    type=["xlsx"],
    key="uploaded_payment_file",
)

if st.button("Chạy rà soát file tải lên"):
    if uploaded_invoice_file is None or uploaded_payment_file is None:
        st.error("Vui lòng chọn đủ file hóa đơn và file thanh toán.")
    else:
        with st.spinner("Đang tải file lên backend và rà soát dữ liệu..."):
            scan_result = scan_uploaded_files(
                uploaded_invoice_file,
                uploaded_payment_file,
            )
        if scan_result is None:
            st.session_state.pop("scan_result", None)
        else:
            st.session_state["scan_result"] = scan_result

result = st.session_state.get("scan_result")
if result is not None:
    st.divider()
    st.subheader("Kết quả rà soát")

    uploaded_files = result.get("uploaded_files")
    if isinstance(uploaded_files, dict):
        st.info("Nguồn kết quả: File tải lên")
        uploaded_invoice_source, uploaded_payment_source = st.columns(2)
        uploaded_invoice_source.write(
            "**File hóa đơn đã tải lên:**",
            uploaded_files.get("invoice_file", ""),
        )
        uploaded_payment_source.write(
            "**File thanh toán đã tải lên:**",
            uploaded_files.get("payment_file", ""),
        )
    else:
        st.info("Nguồn kết quả: Dữ liệu demo cố định")
        source_invoice, source_payment = st.columns(2)
        source_invoice.markdown(
            f"**Nguồn hóa đơn demo:** `{result.get('source_invoice_file', '')}`"
        )
        source_payment.markdown(
            f"**Nguồn thanh toán demo:** `{result.get('source_payment_file', '')}`"
        )

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

    alerts = result.get("alerts", [])
    case_options = list(result.get("case_summary", {}).keys())
    severity_options = sorted(
        {str(alert.get("severity", "")) for alert in alerts if alert.get("severity")}
    )
    case_filter_column, severity_filter_column = st.columns(2)
    selected_case = case_filter_column.selectbox(
        "Lọc theo case_id", ["Tất cả", *case_options]
    )
    selected_severity = severity_filter_column.selectbox(
        "Lọc theo severity", ["Tất cả", *severity_options]
    )
    filtered_alerts = [
        alert
        for alert in alerts
        if (selected_case == "Tất cả" or alert.get("case_id") == selected_case)
        and (
            selected_severity == "Tất cả"
            or alert.get("severity") == selected_severity
        )
    ]

    st.subheader("Chi tiết cảnh báo")
    st.caption(f"Đang hiển thị {len(filtered_alerts)} / {len(alerts)} cảnh báo.")
    st.dataframe(
        build_alerts_table(filtered_alerts),
        width="stretch",
        hide_index=True,
    )

    with st.expander("Xem evidence chi tiết"):
        if not filtered_alerts:
            st.write("Không có cảnh báo phù hợp với bộ lọc hiện tại.")
        for alert in filtered_alerts:
            invoice_reference = get_invoice_reference(alert) or "Không có invoice_id"
            case_id = alert.get("case_id", "Không có case_id")
            with st.expander(f"{invoice_reference} — {case_id}"):
                st.json(alert.get("evidence", {}), expanded=True)
