# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test backend đạt `33 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1` và được cải thiện cho thao tác demo tại commit `67d6a4a`. Dashboard hiển thị 12 hóa đơn, 6 giao dịch thanh toán, 9 cảnh báo, bảng tổng hợp 5 case, bộ lọc và evidence chi tiết.
- Khi backend chưa chạy, Dashboard hiển thị lỗi thân thiện và không crash. Git working tree sạch sau các commit đã nêu.
- **Prototype demo local không RAG: `[x]` đạt** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- README hướng dẫn clone/cài/test/chạy backend/frontend/demo đã hoàn thành tại commit `21976fc`; repo hiện đủ hướng dẫn để người khác chạy lại prototype local bằng hai terminal.
- **GD2-04 upload file thật: `[x]` hoàn thành ở mức prototype `.xlsx`** tại commit `f84cc1f`. Streamlit nhận file hóa đơn và payment; backend xử lý qua `POST /demo/scan-uploaded`; test với hai file demo cho kết quả `12 / 6 / 9`; toàn bộ suite đạt `37 passed, 1 warning`.
- Luồng demo cố định `GET /demo/scan-all` và các endpoint cũ vẫn được giữ nguyên. `requirements.txt` đã có `python-multipart`; Git working tree sạch sau commit.
- Đây chưa phải sản phẩm hoàn chỉnh. Upload hiện chỉ hỗ trợ `.xlsx` với sheet/header/schema hiện tại; chưa tối ưu file lớn, chưa hỗ trợ XML/PDF/OCR, RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao.
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
- `[x]` GD2-04 upload hai file Excel thật ở mức prototype qua Streamlit và `POST /demo/scan-uploaded`; kết quả kiểm tra `12 / 6 / 9`; commit `f84cc1f`.

## Thứ tự ưu tiên

### P1 — Cập nhật README hướng dẫn upload file thật

- Bổ sung cách chọn hai file `.xlsx`, thao tác nút “Chạy rà soát file tải lên” và kết quả kỳ vọng `12 / 6 / 9` với hai file demo.
- Ghi rõ yêu cầu sheet/header/schema hiện tại, các lỗi đầu vào được hỗ trợ và giới hạn kích thước/định dạng.
- Giữ riêng hướng dẫn luồng demo cố định; không mô tả prototype upload như sản phẩm hoàn chỉnh.

### P2 — Cải thiện dashboard sau upload

- Phân biệt rõ hai luồng “demo cố định” và “file tải lên” trên giao diện.
- Hiển thị `uploaded_files` thân thiện hơn và giúp người dùng nhận biết kết quả đang xem thuộc nguồn nào.
- Không mở rộng thành redesign lớn trước khi luồng upload hiện tại được dùng thử ổn định.

### P3 — Rà độc lập nội dung legal draft, không mở RAG

- Rà độc lập nguồn tạo, luật hiện hành, điều/khoản, ngoại lệ và các case Low/Medium.
- Xác nhận rõ phần đã đối chiếu, phần còn thiếu và người chịu trách nhiệm chốt chuyên môn; không coi nhãn High/Medium/Low của AI là kết luận pháp lý.
- **Không mở RAG cho bất kỳ case nào cho đến khi legal draft được rà độc lập.** Không ghi pháp lý hoàn tất nếu chưa có bằng chứng rà soát.

### P4 — Chuẩn bị video demo ngắn hoặc kịch bản thuyết trình demo

- Chuẩn bị luồng trình diễn: khởi động hai terminal → chạy rà soát → đọc số liệu `12 / 6 / 9` → lọc cảnh báo → mở evidence.
- Có thể ưu tiên kịch bản viết trước; chỉ quay video khi giao diện và luồng demo đã ổn định.
- Nêu rõ đây là prototype local không RAG và không thay thế tư vấn chuyên nghiệp.

### P5 — RAG pháp lý + AI explanation sau khi pháp lý được kiểm chứng

- Chỉ bắt đầu sau khi P3 hoàn tất rà soát độc lập và có đủ căn cứ pháp lý sạch cho phạm vi MVP.
- Trả trích dẫn nguồn và từ chối kết luận khi không đủ căn cứ.
- AI explanation chỉ giải thích cảnh báo và gợi ý rà soát, không thay chuyên gia thuế đưa ra kết luận pháp lý.

### P6 — Xử lý ngoại lệ nâng cao sau

- Xem xét hóa đơn điều chỉnh/thay thế, thanh toán từng phần/gộp và bù trừ công nợ.
- Chỉ mở rộng sau khi dashboard demo và luồng upload cơ bản đã ổn định.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** GD2-04 upload hai file Excel thật ở mức prototype; endpoint `POST /demo/scan-uploaded` và Streamlit đã hoạt động, kết quả kiểm tra đạt `12 / 6 / 9`, toàn bộ test đạt `37 passed, 1 warning`.

**Bước đầu phiên sau:** thực hiện P1 — cập nhật README hướng dẫn upload file thật. P2 cải thiện cách hiển thị nguồn upload có thể chuẩn bị song song; P3 legal review độc lập tiếp tục là điều kiện bắt buộc trước RAG.

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
