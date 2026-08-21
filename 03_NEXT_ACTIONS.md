# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test backend đạt `33 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1` và được cải thiện cho thao tác demo tại commit `67d6a4a`. Dashboard hiển thị 12 hóa đơn, 6 giao dịch thanh toán, 9 cảnh báo, bảng tổng hợp 5 case, bộ lọc và evidence chi tiết.
- Khi backend chưa chạy, Dashboard hiển thị lỗi thân thiện và không crash. Git working tree sạch sau các commit đã nêu.
- **Prototype demo local không RAG: `[x]` đạt** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- README hướng dẫn clone/cài/test/chạy backend/frontend/demo đã hoàn thành tại commit `21976fc`; repo hiện đủ hướng dẫn để người khác chạy lại prototype local bằng hai terminal.
- Chưa có upload file thật, RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao. Đây chưa phải sản phẩm hoàn chỉnh.
- Legal draft đã có tại `van-ban-luat/processed/GD1_5_P_LEGAL_DRAFT_mapping_5_cases.md`, commit `ee099db` (`Add legal draft mapping for MVP cases`). Nguồn tạo là VSCode AI theo prompt điều phối của ChatGPT Plus.
- Chưa có Khánh/Gemini Pro hoặc người có chuyên môn rà soát độc lập; chưa có human/legal final review và chưa xác nhận pháp lý hoàn tất. Nhãn High/Medium/Low trong draft chỉ là đánh giá sơ bộ của AI.
- RAG và AI explanation chưa triển khai. RAG **LOCKED toàn bộ 5 case**, kể cả case có nhãn High confidence, cho đến khi legal draft được rà soát độc lập.
- Ngôn ngữ rule phải tiếp tục chỉ cảnh báo “có dấu hiệu”, “cần rà soát”; không kết luận gian lận, vi phạm, hóa đơn vô hiệu, không được khấu trừ, bị xử phạt hoặc bị loại chi phí.

## Hạng mục vừa hoàn thành

- `[x]` API tổng hợp `GET /demo/scan-all` chạy đủ 5 rule và trả 9 cảnh báo.
- `[x]` Test scan-all và hồi quy các endpoint case riêng; toàn bộ suite đạt `33 passed, 1 warning`.
- `[x]` Streamlit demo local gọi scan-all, hiển thị 3 metric, bảng 5 case và bảng 9 cảnh báo.
- `[x]` Xử lý thân thiện trường hợp backend chưa chạy và thêm disclaimer pháp lý an toàn.
- `[x]` Cải thiện Dashboard với hướng dẫn chạy, nguồn dữ liệu, bộ lọc case/severity và evidence chi tiết.
- `[x]` README hướng dẫn chạy prototype demo local bằng hai terminal; commit `21976fc`.
- `[x]` Có legal draft mapping cho 5 case MVP; commit `ee099db`. Đây chưa phải kiểm chứng pháp lý hoàn tất.

## Thứ tự ưu tiên

### P1 — Rà độc lập nội dung legal draft

- Rà độc lập nội dung legal draft, đặc biệt kiểm tra nguồn tạo, luật hiện hành, điều/khoản và các case Low/Medium.
- Xác nhận rõ phần đã đối chiếu, phần còn thiếu và người chịu trách nhiệm chốt chuyên môn; không coi nhãn High/Medium/Low của AI là kết luận pháp lý.
- **Không mở RAG cho bất kỳ case nào cho đến khi legal draft được rà độc lập.** Không ghi GD1.5-P1 hoàn thành nếu chưa có bằng chứng rà soát.

### P2 — GD2-04: Upload file thật cho Excel hóa đơn và payment

- Cho phép người dùng đưa file hóa đơn và file thanh toán qua Streamlit/API thay cho đường dẫn demo cố định.
- Kiểm tra định dạng, schema và thông báo lỗi an toàn trước khi chạy scan-all.
- Không coi upload là hoàn thành cho đến khi có kiểm tra với cả file hợp lệ và file lỗi.

### P3 — Cải thiện dashboard mức vừa

- Rà soát format bảng và ẩn bớt cột kỹ thuật nếu cần cho kịch bản trình diễn.
- Giữ khả năng xem evidence chi tiết nhưng ưu tiên thông tin người dùng cần đọc ngay.
- Không mở rộng thành redesign lớn trước khi luồng upload hoạt động ổn định.

### P4 — Chuẩn bị video demo ngắn hoặc kịch bản thuyết trình demo

- Chuẩn bị luồng trình diễn: khởi động hai terminal → chạy rà soát → đọc số liệu `12 / 6 / 9` → lọc cảnh báo → mở evidence.
- Có thể ưu tiên kịch bản viết trước; chỉ quay video khi giao diện và luồng demo đã ổn định.
- Nêu rõ đây là prototype local không RAG và không thay thế tư vấn chuyên nghiệp.

### P5 — RAG pháp lý + AI explanation sau khi pháp lý được kiểm chứng

- Chỉ bắt đầu sau khi P1 hoàn tất rà soát độc lập và có đủ căn cứ pháp lý sạch cho phạm vi MVP; không đưa RAG lên trước GD2-04 upload file thật nếu pháp lý chưa sạch.
- Trả trích dẫn nguồn và từ chối kết luận khi không đủ căn cứ.
- AI explanation chỉ giải thích cảnh báo và gợi ý rà soát, không thay chuyên gia thuế đưa ra kết luận pháp lý.

### P6 — Xử lý ngoại lệ nâng cao sau

- Xem xét hóa đơn điều chỉnh/thay thế, thanh toán từng phần/gộp và bù trừ công nợ.
- Chỉ mở rộng sau khi dashboard demo và luồng upload cơ bản đã ổn định.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** prototype demo local không RAG trên dữ liệu Excel cố định; scan-all và Streamlit đã kết nối, toàn bộ test backend đạt `33 passed, 1 warning`.

**Hai luồng có thể làm song song ở đầu phiên sau:**

- **A. Legal review độc lập legal draft:** kiểm tra nguồn tạo, luật hiện hành, hiệu lực, điều/khoản và ưu tiên các case Low/Medium.
- **B. GD2-04 upload file thật:** triển khai upload file Excel hóa đơn và payment, kèm kiểm tra schema và lỗi đầu vào. Đây là ưu tiên kỹ thuật tiếp theo.

Không mở RAG cho bất kỳ case nào cho đến khi luồng A hoàn tất; nếu pháp lý chưa sạch, không đưa RAG lên trước luồng B.

## Ước lượng tiến độ

- **Mức 1 — Prototype demo local không RAG:** `[x]` đạt ngày 18/08/2026.
- **Mức 2 — RAG pháp lý + trích dẫn + AI explanation:** phụ thuộc kiểm chứng pháp lý; nếu pháp lý xong trong tuần này thì cần thêm khoảng 2–3 phiên, ước tính 1–1.5 tuần.
- **Tổng mức trình diễn đầy đủ:** khoảng 1.5–2 tuần nếu pháp lý không bị trì hoãn.
- **Rủi ro lớn nhất hiện tại:** kiểm chứng pháp lý, không phải kỹ thuật backend.

## Chưa ưu tiên ở giai đoạn hiện tại

- OCR/PDF và luồng trích xuất chứng từ phức tạp.
- Ngoại lệ nâng cao như hóa đơn điều chỉnh/thay thế.
- Thanh toán từng phần/gộp và bù trừ công nợ.
- Các mở rộng này xếp sau upload file, ổn định Dashboard và chuẩn bị kịch bản trình diễn.

RAG cũng không được triển khai sớm chỉ để làm đẹp demo; điều kiện bắt buộc vẫn là hoàn tất kiểm chứng pháp lý.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
- Không gọi prototype demo local hiện tại là sản phẩm hoàn chỉnh; RAG/AI explanation chỉ được tuyên bố khi đã triển khai và kiểm chứng.
