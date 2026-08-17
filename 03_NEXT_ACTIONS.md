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
- P2-CASE2: `[x]` Đã hoàn thành backend slice Case 2; API trả 2 cảnh báo cho `INV-DEMO-005` và `INV-DEMO-006`.
- P3-CASE3: `[x]` Đã hoàn thành backend slice Case 3; API trả 2 cảnh báo cho `INV-DEMO-007` và `INV-DEMO-008`; toàn bộ suite đạt 16 passed, 1 warning.

**Ghi chú:** Backend đã có code, API và test cho Case 1–3. Dashboard vẫn là trang tĩnh, chưa upload hoặc gọi backend; Case 4–5, API scan-all và RAG chưa triển khai. Chưa có prototype end-to-end.

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

### P2 — Triển khai Case 2 sai MST/tên người mua `[x]`

- Rule `buyer_info_mismatch.py`, endpoint `GET /demo/case-2-buyer-info` và test Case 2 đã hoàn thành.
- Phát hiện 2 cảnh báo demo: `INV-DEMO-005`, `INV-DEMO-006`.
- Commit: `934d3e3` (`Implement backend buyer info mismatch case`).

### P3 — Triển khai Case 3 VAT lệch phép tính `[x]`

- Rule `vat_mismatch.py`, endpoint `GET /demo/case-3-vat-mismatch` và test Case 3 đã hoàn thành.
- Phát hiện 2 cảnh báo demo: `INV-DEMO-007`, `INV-DEMO-008`.
- Commit: `7570404` (`Implement backend VAT mismatch case`); toàn bộ suite đạt 16 passed, 1 warning.

### P4 — Case 4: Hóa đơn ngoài kỳ dữ liệu đang rà soát

- So sánh `invoice_date` với kỳ dữ liệu đang rà soát.
- Chỉ nhắc người dùng rà soát hóa đơn ngoài kỳ, không kết luận vi phạm hoặc sai kỳ pháp lý.
- Bổ sung rule, endpoint demo và test tự động trước khi đánh dấu hoàn thành.

### P5 — Case 5: Đối chiếu hóa đơn giá trị lớn với dữ liệu thanh toán

- Đọc file `sample_bank_payments_mvp.xlsx` và xác minh schema trước khi code.
- Chốt ngưỡng cấu hình, ngoại lệ và logic liên kết thanh toán với người phụ trách nghiệp vụ.
- Chỉ cảnh báo chưa tìm thấy chứng từ phù hợp; không tự kết luận hóa đơn không hợp lệ.

### P6 — API tổng hợp `/demo/scan-all`

- Chạy các rule Case 1–5 đã hoàn thành trên cùng dữ liệu mẫu.
- Trả danh sách cảnh báo thống nhất và tổng hợp số lượng theo case.
- Không coi scan-all là hoàn thành cho đến khi Case 4–5 có test đạt.

### P7 — Kết nối Streamlit hiển thị bảng cảnh báo

- Gọi API scan-all và hiển thị bảng cảnh báo theo case, mức độ và invoice liên quan.
- Sau khi luồng gọi API ổn định, bổ sung upload Excel thay cho file demo cố định.
- Hiển thị lỗi rõ ràng khi file sai định dạng hoặc backend không khả dụng.

### P8 — RAG pháp lý sau

- Chỉ bắt đầu sau khi parser, rule engine, API và Dashboard đã tạo được luồng end-to-end ổn định.
- Chỉ ingest nội dung pháp lý đã được con người kiểm chứng nguồn, hiệu lực và điều/khoản.
- Thiết kế citation và cơ chế từ chối khi không đủ căn cứ trước khi tích hợp phần giải thích AI.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** backend code, API và test cho Case 1–3; toàn bộ suite đạt `16 passed, 1 warning`.

**Bước tiếp theo:** triển khai Case 4 — hóa đơn ngoài kỳ dữ liệu đang rà soát — với thông điệp chỉ nhắc rà soát; sau đó mới triển khai Case 5, API scan-all và kết nối Streamlit.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
