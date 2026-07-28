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

**Ghi chú:** GD1-07 đã hoàn thành; bản v2 là master hiện hành nhưng cần rút gọn trước khi nộp Dashboard.

## Thứ tự ưu tiên

### Việc 1 — Kiểm tra Dashboard để xác định cấu trúc trường và giới hạn ký tự

- Đăng nhập Dashboard cuộc thi và ghi lại cấu trúc các trường cần nhập.
- Xác nhận giới hạn ký tự, định dạng được hỗ trợ và yêu cầu tệp đính kèm nếu có.
- Lưu ảnh hoặc ghi chú làm bằng chứng trước khi biên tập bản nộp.

### Việc 2 — Tạo bản rút gọn Dashboard từ GD1-07

- Rút gọn từ bản master GD1-07 theo đúng cấu trúc và giới hạn đã xác định.
- Giữ đủ vấn đề, giải pháp, năm case MVP, tính khả thi, giới hạn pháp lý và vai trò con người.
- Không sửa hoặc thay thế bản master hiện hành.

### Việc 3 — GD1-08: Viết mục khai báo AI dựa trên log

- Đọc `02_SESSION_LOG.md` và tổng hợp vai trò của từng công cụ AI đã sử dụng.
- Phân biệt nội dung do AI hỗ trợ với phần do con người kiểm tra, quyết định và chịu trách nhiệm.
- Viết nội dung khai báo ngắn, trung thực và phù hợp với trường trên Dashboard.

### Việc 4 — GD1-P1: Tiếp tục kiểm chứng pháp lý chi tiết song song

- Mở `van-ban-luat/processed/GD0-04_legal_basis_5_cases_v3_reviewed.md` và bản diễn đạt an toàn GD1-P1.
- Đối chiếu từng văn bản, điều, khoản, hiệu lực, quy định chuyển tiếp và trích đoạn với nguồn pháp luật gốc.
- Ghi rõ nội dung đã xác minh, nội dung cần sửa và nội dung còn chờ chuyên gia xác nhận.
- Không đưa ngưỡng hoặc kết luận pháp lý chi tiết chưa được kiểm chứng vào hồ sơ hay rule engine.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
