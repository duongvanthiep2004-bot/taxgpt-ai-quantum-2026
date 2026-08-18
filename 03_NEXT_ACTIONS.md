# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test backend đạt `33 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1`. Dashboard hiển thị 12 hóa đơn, 6 giao dịch thanh toán, 9 cảnh báo, bảng tổng hợp 5 case và bảng chi tiết cảnh báo.
- Khi backend chưa chạy, Dashboard hiển thị lỗi thân thiện và không crash. Git working tree sạch sau hai commit.
- **Prototype demo local không RAG: `[x]` đạt** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- Chưa có upload file thật, RAG pháp lý hoặc AI explanation; evidence còn là JSON thô và chưa xử lý ngoại lệ nghiệp vụ nâng cao. Đây chưa phải sản phẩm hoàn chỉnh.
- RAG và AI explanation chưa triển khai. RAG bị khóa cho đến khi nguồn, hiệu lực và điều/khoản pháp lý được Khánh cùng Gemini Pro kiểm chứng.
- Ngôn ngữ rule phải tiếp tục chỉ cảnh báo “có dấu hiệu”, “cần rà soát”; không kết luận gian lận, vi phạm, hóa đơn vô hiệu, không được khấu trừ, bị xử phạt hoặc bị loại chi phí.

## Hạng mục vừa hoàn thành

- `[x]` API tổng hợp `GET /demo/scan-all` chạy đủ 5 rule và trả 9 cảnh báo.
- `[x]` Test scan-all và hồi quy các endpoint case riêng; toàn bộ suite đạt `33 passed, 1 warning`.
- `[x]` Streamlit demo local gọi scan-all, hiển thị 3 metric, bảng 5 case và bảng 9 cảnh báo.
- `[x]` Xử lý thân thiện trường hợp backend chưa chạy và thêm disclaimer pháp lý an toàn.

## Thứ tự ưu tiên

### P1 — Làm đẹp dashboard cơ bản

- Format evidence thành nội dung dễ đọc thay cho JSON thô.
- Thêm lọc theo case, màu/nhãn severity và hướng dẫn ngắn cách chạy demo.
- Giữ giao diện gọn, ổn định và không diễn đạt như một bản tư vấn pháp lý.

### P2 — Upload file thật cho Excel hóa đơn và payment

- Cho phép người dùng đưa file hóa đơn và file thanh toán qua Streamlit/API thay cho đường dẫn demo cố định.
- Kiểm tra định dạng, schema và thông báo lỗi an toàn trước khi chạy scan-all.
- Không coi upload là hoàn thành cho đến khi có kiểm tra với cả file hợp lệ và file lỗi.

### P3 — Cập nhật README hướng dẫn chạy backend/frontend/demo

- Ghi rõ lệnh chạy Uvicorn và Streamlit, URL truy cập và thứ tự thao tác demo.
- Ghi rõ phạm vi dữ liệu demo, kết quả kỳ vọng `12 / 6 / 9` và cách xử lý khi backend chưa chạy.
- Nêu rõ giới hạn: chưa có RAG, AI explanation và xử lý ngoại lệ nâng cao.

### P4 — Kiểm chứng pháp lý với Khánh + Gemini Pro

- Đối chiếu nguồn gốc, hiệu lực và điều/khoản cho từng nội dung dự kiến ingest.
- Ghi rõ nội dung đã xác minh, chưa xác minh và điểm cần chuyên gia quyết định.
- **Không làm RAG và không ingest tài liệu trước khi nội dung pháp lý được kiểm chứng.**

### P5 — RAG pháp lý + AI explanation sau khi pháp lý được kiểm chứng

- Chỉ bắt đầu khi P4 đã hoàn tất đủ căn cứ cho phạm vi MVP.
- Trả trích dẫn nguồn và từ chối kết luận khi không đủ căn cứ.
- AI explanation chỉ giải thích cảnh báo và gợi ý rà soát, không thay chuyên gia thuế đưa ra kết luận pháp lý.

### P6 — Xử lý ngoại lệ nâng cao sau khi prototype ổn

- Xem xét hóa đơn điều chỉnh/thay thế, thanh toán từng phần/gộp và bù trừ công nợ.
- Chỉ mở rộng sau khi dashboard demo và luồng upload cơ bản đã ổn định.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** prototype demo local không RAG trên dữ liệu Excel cố định; scan-all và Streamlit đã kết nối, toàn bộ test backend đạt `33 passed, 1 warning`.

**Bước đầu phiên sau:** thực hiện P1 — định dạng evidence, thêm lọc case, màu severity và hướng dẫn chạy demo — trước khi mở rộng sang upload file thật.

## Ước lượng tiến độ

- **Mức 1 — Prototype demo local không RAG:** `[x]` đạt ngày 18/08/2026.
- **Mức 2 — RAG pháp lý + trích dẫn + AI explanation:** phụ thuộc kiểm chứng pháp lý; nếu pháp lý xong trong tuần này thì cần thêm khoảng 2–3 phiên, ước tính 1–1.5 tuần.
- **Tổng mức trình diễn đầy đủ:** khoảng 1.5–2 tuần nếu pháp lý không bị trì hoãn.
- **Rủi ro lớn nhất hiện tại:** kiểm chứng pháp lý, không phải kỹ thuật backend.

## Không ưu tiên trước khi dashboard demo ổn

- OCR/PDF và luồng trích xuất chứng từ phức tạp.
- Ngoại lệ nâng cao như hóa đơn điều chỉnh/thay thế.
- Thanh toán từng phần/gộp và bù trừ công nợ.
- Các mở rộng này không được ưu tiên trước khi dashboard demo cơ bản ổn định.

RAG cũng không được triển khai sớm chỉ để làm đẹp demo; điều kiện bắt buộc vẫn là hoàn tất kiểm chứng pháp lý.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
- Không gọi prototype demo local hiện tại là sản phẩm hoàn chỉnh; RAG/AI explanation chỉ được tuyên bố khi đã triển khai và kiểm chứng.
