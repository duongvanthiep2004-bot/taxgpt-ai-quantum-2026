import streamlit as st


st.title("TaxGPT Dashboard")
st.write("Upload hóa đơn/chứng từ để kiểm tra rủi ro thuế MVP")

st.subheader("5 case rủi ro MVP")
cases = [
    "Hóa đơn trùng",
    "Sai MST/tên người mua",
    "VAT không khớp phép tính",
    "Hóa đơn đầu vào ngoài kỳ kê khai",
    "Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt",
]

for index, case in enumerate(cases, start=1):
    st.write(f"{index}. {case}")
