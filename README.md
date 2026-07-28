# TaxGPT

TaxGPT là dự án AI hỗ trợ phát hiện rủi ro thuế và tuân thủ chứng từ cho SMEs Việt Nam, tham gia AI-Quantum Challenge 2026.

## Mục tiêu MVP

Prototype tập trung vào 5 case rủi ro:
1. Hóa đơn trùng
2. Sai MST/tên người mua
3. VAT không khớp phép tính
4. Hóa đơn đầu vào ngoài kỳ kê khai
5. Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt

## Cấu trúc thư mục

- backend/: API, parser, rule engine, RAG pipeline
- frontend/: dashboard demo
- data-mau/: dữ liệu hóa đơn, Excel, sao kê mẫu
- van-ban-luat/: văn bản pháp luật dùng cho RAG
- docs/: tài liệu dự án, hồ sơ dự thi, file điều phối
- scripts/: script hỗ trợ

## Nguyên tắc

AI chỉ hỗ trợ xây dựng và phản biện. Nội dung pháp lý phải được đối chiếu với văn bản gốc trước khi đưa vào sản phẩm hoặc hồ sơ nộp thi.

## Cài đặt môi trường

### 1. Tạo virtual environment

```bash
python -m venv .venv
```

Kích hoạt môi trường:

- Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Cài dependencies

```bash
pip install -r requirements.txt
```

### 3. Chạy backend

```bash
uvicorn backend.app.main:app --reload
```

Backend mặc định chạy tại `http://127.0.0.1:8000`; endpoint kiểm tra: `http://127.0.0.1:8000/health`.

### 4. Chạy frontend

```bash
streamlit run frontend/streamlit_app/app.py
```
