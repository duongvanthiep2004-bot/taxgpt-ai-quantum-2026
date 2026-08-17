# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- GD0-01: `[x]` Chốt đội thi.
- GD0-02: `[x]` Tạo cấu trúc repo.
- GD0-03: `[x]` Chốt 5 case MVP.
- GD0-04: `[~]` Đã có khung pháp lý V3, chưa kiểm chứng đầy đủ điều/khoản gốc.
- GD0-05: `[x]` Môi trường code cơ bản đã chạy được.
- GD0-06: `[x]` Đội đã đăng ký thành công; Dashboard hiển thị mã đội AQ2026-183 và trạng thái hồ sơ APPROVED.
- GD1-P1: `[~]` Đã có bản diễn đạt pháp lý an toàn cho hồ sơ Vòng 1; chưa chốt kiểm chứng pháp lý đầy đủ.
- GD1-02: `[x]` Đã tạo và review đạt file mô tả giải pháp TaxGPT cho hồ sơ Vòng 1.
- GD1-03: `[x]` Đã tạo và review đạt dữ liệu mẫu giả lập cho 5 case MVP.
- GD1-04: `[x]` Đã tạo và review đạt file kiến trúc kỹ thuật TaxGPT cho hồ sơ Vòng 1.
- GD1-05: `[x]` Đã tạo và review đạt bản master mô tả ý tưởng Vòng 1.
- GD1-06: `[x]` Đã tạo báo cáo phản biện thử hồ sơ Vòng 1.
- GD1-07: `[x]` Đã tạo và review đạt bản v2 mô tả ý tưởng Vòng 1; dùng làm master hiện hành.
- P0-ENV: `[x]` Đã khôi phục runtime cơ bản ngày 17/08/2026: Python 3.12.10, pip 25.0.1, pytest 1 passed; backend `/health` HTTP 200 và frontend tĩnh render được.
- P1-CASE1: `[x]` Đã hoàn thành luồng `Đọc Excel → rule Case 1 → API JSON`; parser đọc 12 hóa đơn, API trả HTTP 200 và phát hiện 1 nhóm duplicate.

**Ghi chú:** Backend đã có lát cắt Case 1 và test đạt 7 passed, 1 warning. Dashboard vẫn là trang tĩnh, chưa upload hoặc gọi backend; Case 2–5 và RAG chưa triển khai. Chưa có prototype end-to-end.

## Thứ tự ưu tiên

### P0 — Khôi phục và xác minh môi trường `[x]`

- Python 3.12.10 và pip 25.0.1 trong `.venv` chạy được.
- `pytest`: 1 passed, 1 warning.
- Backend FastAPI và endpoint `/health` chạy được, trả HTTP 200 OK.
- Streamlit render được Dashboard tĩnh.

### P1 — Đọc Excel → rule Case 1 → API JSON `[x]`

- Parser đọc đúng 12 hóa đơn từ sheet `invoices` của file mẫu.
- Rule Case 1 phát hiện 1 nhóm có khả năng trùng: `INV-DEMO-003`, `INV-DEMO-004`.
- Endpoint `GET /demo/case-1-duplicates` trả HTTP 200 và danh sách cảnh báo JSON.
- Test health, parser, xử lý lỗi, rule và API đạt `7 passed, 1 warning`.

### P2 — Triển khai Case 2 sai MST/tên người mua

- Chốt dữ liệu doanh nghiệp tham chiếu dùng để so sánh MST và tên người mua.
- Tách cảnh báo sai MST khỏi sai lệch nhỏ trong tên; chỉ đưa cảnh báo rà soát, không kết luận hóa đơn vô hiệu.
- Viết unit test và API test cho dữ liệu bình thường, sai MST và sai tên.

### P3 — Triển khai Case 3 VAT lệch phép tính

- Tính lại VAT từ `taxable_amount × vat_rate` và so sánh với `vat_amount`.
- Chốt tolerance kỹ thuật cho sai số làm tròn và ghi rõ đây không phải ngưỡng pháp lý.
- Viết test cho giá trị đúng, lệch và trường hợp biên làm tròn.

### P4 — Kết nối Dashboard Streamlit

- Gọi backend API và hiển thị danh sách/bảng cảnh báo cho các case đã triển khai.
- Sau khi luồng gọi API ổn định, bổ sung upload Excel thay cho file demo cố định.
- Hiển thị trạng thái lỗi rõ ràng khi file thiếu, sai định dạng hoặc backend không khả dụng.

### P5 — Triển khai Case 4 và Case 5

- Case 4 chỉ nhắc rà soát hóa đơn ngoài kỳ dữ liệu đang kiểm tra, không kết luận vi phạm.
- Case 5 chỉ triển khai sau khi ngưỡng, ngoại lệ và logic liên kết thanh toán được người phụ trách nghiệp vụ xác nhận.
- Duy trì unit test và API test cho từng case trước khi đánh dấu hoàn thành.

### P6 — RAG pháp lý sau

- Chỉ bắt đầu sau khi parser, rule engine, API và Dashboard đã tạo được luồng end-to-end ổn định.
- Chỉ ingest nội dung pháp lý đã được con người kiểm chứng nguồn, hiệu lực và điều/khoản.
- Thiết kế citation và cơ chế từ chối khi không đủ căn cứ trước khi tích hợp phần giải thích AI.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** đọc `sample_invoices_mvp.xlsx` → chạy rule Case 1 → trả danh sách cảnh báo JSON.

**Bước tiếp theo:** triển khai Case 2 sai MST/tên người mua với dữ liệu doanh nghiệp tham chiếu được xác nhận; sau đó triển khai Case 3 và kết nối Dashboard Streamlit tối thiểu.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
