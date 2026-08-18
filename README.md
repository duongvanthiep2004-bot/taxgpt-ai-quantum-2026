# TaxGPT — Trợ lý AI hỗ trợ rà soát rủi ro thuế và tuân thủ chứng từ cho SMEs Việt Nam

TaxGPT hiện là **prototype demo local không RAG**, hỗ trợ rà soát 5 nhóm rủi ro trên dữ liệu Excel demo. TaxGPT không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế.

Phiên bản hiện tại chưa có RAG pháp lý và chưa hỗ trợ upload file thật.

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
| Test backend | `33 passed, 1 warning` |
| Upload file thật | Chưa có |
| RAG pháp lý | Chưa có |
| AI explanation | Chưa có |

Dashboard demo được cải thiện tại commit `67d6a4a` (`Improve Streamlit demo dashboard`). Đây chưa phải sản phẩm hoàn chỉnh.

## Cài môi trường trên Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

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
33 passed, 1 warning
```

## Chạy backend — Terminal 1

```powershell
.\.venv\Scripts\activate
uvicorn backend.app.main:app --reload
```

Kiểm tra:

- Health: <http://127.0.0.1:8000/health>
- Scan-all: <http://127.0.0.1:8000/demo/scan-all>

## Chạy frontend — Terminal 2

```powershell
.\.venv\Scripts\activate
streamlit run frontend/streamlit_app/app.py
```

Mở Dashboard tại <http://localhost:8501>.

## Cách demo

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

## API demo

- `GET /health`
- `GET /demo/case-1-duplicates`
- `GET /demo/case-2-buyer-info`
- `GET /demo/case-3-vat-mismatch`
- `GET /demo/case-4-out-of-period`
- `GET /demo/case-5-missing-bank-payment`
- `GET /demo/scan-all`

Các endpoint chạy trên địa chỉ mặc định `http://127.0.0.1:8000`.

## Dữ liệu demo

- Hóa đơn: `data-mau/excel/sample_invoices_mvp.xlsx`
- Thanh toán: `data-mau/bank_statements/sample_bank_payments_mvp.xlsx`

Toàn bộ dữ liệu là giả lập, không sử dụng dữ liệu doanh nghiệp thật.

## Giới hạn hiện tại

- API đang sử dụng hai file demo cố định.
- Chưa có upload file thật.
- Chưa có RAG pháp lý.
- Chưa có AI explanation.
- Chưa xử lý các ngoại lệ nâng cao như hóa đơn điều chỉnh/thay thế, thanh toán từng phần, thanh toán gộp hoặc bù trừ công nợ.
- Evidence vẫn ở mức kỹ thuật phục vụ demo.

## Nguyên tắc an toàn

- TaxGPT chỉ cảnh báo dấu hiệu cần rà soát.
- Không kết luận gian lận.
- Không kết luận vi phạm pháp luật.
- Không kết luận hóa đơn vô hiệu.
- Không thay thế tư vấn chuyên nghiệp.
