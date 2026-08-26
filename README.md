# TaxGPT — Trợ lý AI hỗ trợ rà soát rủi ro thuế và tuân thủ chứng từ cho SMEs Việt Nam

TaxGPT hiện là **prototype demo local không RAG**, hỗ trợ rà soát 5 nhóm rủi ro trên dữ liệu Excel demo hoặc hai file Excel do người dùng tải lên. TaxGPT không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế.

Phiên bản hiện tại đã có upload file thật ở mức prototype `.xlsx`. RAG pháp lý vẫn **LOCKED toàn bộ 5 case** và AI explanation chưa được triển khai.

## 5 case MVP

1. **Case 1:** Hóa đơn trùng.
2. **Case 2:** Sai MST/tên người mua.
3. **Case 3:** VAT không khớp phép tính.
4. **Case 4:** Hóa đơn ngoài kỳ dữ liệu đang rà soát.
5. **Case 5:** Thiếu chứng từ thanh toán không dùng tiền mặt.

## Trạng thái hiện tại

| Hạng mục | Trạng thái |
|---|---|
| Backend 5/5 case MVP | Done |
| API tổng hợp `GET /demo/scan-all` | Done |
| Streamlit demo dashboard | Done |
| Test backend | `42 passed, 1 warning` |
| Upload file thật | Done ở mức prototype `.xlsx` qua `POST /demo/scan-uploaded` |
| RAG pháp lý | Chưa có / **LOCKED toàn bộ 5 case** |
| AI explanation | Chưa có |

Dashboard demo được cải thiện tại commit `67d6a4a` (`Improve Streamlit demo dashboard`). Luồng upload được triển khai tại commit `f84cc1f` (`Implement uploaded Excel scan workflow`) và trạng thái điều phối được cập nhật tại commit `bbac7d7` (`Update progress after uploaded Excel workflow`). Đây chưa phải sản phẩm hoàn chỉnh; legal draft chưa phải kiểm chứng pháp lý cuối cùng.

## Cài môi trường trên Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` đã bao gồm `python-multipart` để FastAPI nhận file qua `multipart/form-data`.

Nếu máy có nhiều phiên bản Python, có thể tạo môi trường bằng Python 3.12:

```powershell
py -3.12 -m venv .venv
```

## Chạy test

```powershell
pytest
```

Kết quả kỳ vọng:

```text
42 passed, 1 warning
```

## Chạy backend — Terminal 1

```powershell
.\.venv\Scripts\activate
uvicorn backend.app.main:app --reload
```

Kiểm tra:

- Health: <http://127.0.0.1:8000/health>
- Scan-all: <http://127.0.0.1:8000/demo/scan-all>
- Tài liệu API tương tác: <http://127.0.0.1:8000/docs>

## Chạy frontend — Terminal 2

```powershell
.\.venv\Scripts\activate
streamlit run frontend/streamlit_app/app.py
```

Mở Dashboard tại <http://localhost:8501>.

## Cách demo cố định

1. Bật backend trước.
2. Bật Streamlit sau.
3. Mở Dashboard và bấm **“Chạy rà soát dữ liệu demo”**.
4. Dashboard sẽ hiển thị:

   - Tổng hóa đơn: **12**.
   - Tổng giao dịch thanh toán: **6**.
   - Tổng cảnh báo: **9**.
   - Bảng tổng hợp 5 case.
   - Bảng chi tiết cảnh báo.
   - Bộ lọc theo case/severity và evidence chi tiết.

## Cách rà soát file Excel tải lên

1. Bật backend và Streamlit như hướng dẫn trên.
2. Mở Dashboard tại <http://localhost:8501>.
3. Vào mục **“Rà soát file Excel tải lên”**.
4. Chọn **File hóa đơn Excel (.xlsx)**.
5. Chọn **File thanh toán Excel (.xlsx)**.
6. Bấm **“Chạy rà soát file tải lên”**.
7. Nếu dùng hai file demo của repo, kết quả kỳ vọng là **12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo**.

Luồng upload không thay thế nút **“Chạy rà soát dữ liệu demo”**; người dùng có thể tiếp tục dùng luồng demo cố định.

Có thể dùng hai template `data-mau/excel/template_invoices_mvp.xlsx` và `data-mau/bank_statements/template_bank_payments_mvp.xlsx` để chuẩn bị file đúng định dạng. Các template chỉ phục vụ demo/prototype.

## API demo

- `GET /health`
- `GET /demo/case-1-duplicates`
- `GET /demo/case-2-buyer-info`
- `GET /demo/case-3-vat-mismatch`
- `GET /demo/case-4-out-of-period`
- `GET /demo/case-5-missing-bank-payment`
- `GET /demo/scan-all`
- `POST /demo/scan-uploaded` — nhận `multipart/form-data` với hai trường file:

  - `invoice_file`: file hóa đơn `.xlsx`.
  - `payment_file`: file thanh toán `.xlsx`.

Các endpoint chạy trên địa chỉ mặc định `http://127.0.0.1:8000`.

## Dữ liệu demo

- Hóa đơn: `data-mau/excel/sample_invoices_mvp.xlsx`.
- Thanh toán: `data-mau/bank_statements/sample_bank_payments_mvp.xlsx`.

Hai file trên vừa được dùng cho luồng demo cố định, vừa có thể chọn trực tiếp để thử luồng upload.

Toàn bộ dữ liệu là giả lập, không sử dụng dữ liệu doanh nghiệp thật.

## Giới hạn hiện tại

- Luồng upload chỉ hỗ trợ file `.xlsx`.
- File phải theo sheet/header/schema hiện tại của parser hóa đơn và payment.
- Chưa hỗ trợ XML/PDF/OCR.
- Chưa tối ưu cho file lớn.
- Chưa có RAG pháp lý; RAG vẫn **LOCKED toàn bộ 5 case**.
- Chưa có AI explanation.
- Chưa xử lý các ngoại lệ nâng cao như hóa đơn điều chỉnh/thay thế, thanh toán từng phần, thanh toán gộp hoặc bù trừ công nợ.
- Evidence vẫn ở mức kỹ thuật phục vụ demo.

## Nguyên tắc an toàn

- TaxGPT chỉ cảnh báo dấu hiệu cần rà soát.
- TaxGPT không đưa ra kết luận pháp lý cuối cùng về hóa đơn, chứng từ hoặc nghĩa vụ thuế.
- Không thay thế tư vấn chuyên nghiệp.
