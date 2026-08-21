# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test hồi quy hiện đạt `41 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1`, được cải thiện cho thao tác demo tại commit `67d6a4a` và phân biệt nguồn kết quả tại commit `abd9738`. Dashboard hiện có “Chế độ 1: Dữ liệu demo cố định” và “Chế độ 2: File Excel tải lên”; kết quả ghi rõ nguồn dữ liệu và hiển thị tên hai file khi có `uploaded_files`.
- Khi backend chưa chạy, Dashboard hiển thị lỗi thân thiện và không crash. Git working tree sạch sau các commit đã nêu.
- **Prototype demo local không RAG: `[x]` đạt** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- README hướng dẫn clone/cài/test/chạy backend/frontend/demo đã hoàn thành tại commit `21976fc`; repo hiện đủ hướng dẫn để người khác chạy lại prototype local bằng hai terminal.
- **GD2-04 upload file thật: `[x]` hoàn thành ở mức prototype `.xlsx`** tại commit `f84cc1f`. Streamlit nhận file hóa đơn và payment; backend xử lý qua `POST /demo/scan-uploaded`; test với hai file demo cho kết quả `12 / 6 / 9`; toàn bộ suite hồi quy hiện đạt `41 passed, 1 warning`.
- Luồng demo cố định `GET /demo/scan-all` và các endpoint cũ vẫn được giữ nguyên. `requirements.txt` đã có `python-multipart`; Git working tree sạch sau commit.
- Đây chưa phải sản phẩm hoàn chỉnh. Upload hiện chỉ hỗ trợ `.xlsx` với sheet/header/schema hiện tại; chưa kiểm tra sâu kiểu dữ liệu từng ô, chưa giới hạn dung lượng file, chưa hỗ trợ XML/PDF/OCR, RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao.
- **GD2-04a schema validation: `[x]` hoàn thành** tại commit `3bd1471`. Backend phân biệt workbook hỏng, thiếu sheet `invoices`/`payments` và thiếu một hoặc nhiều cột bắt buộc; lỗi không lộ traceback hoặc đường dẫn file tạm. Upload demo vẫn đạt `12 / 6 / 9`.
- Legal draft đã có tại `van-ban-luat/processed/GD1_5_P_LEGAL_DRAFT_mapping_5_cases.md`, commit `ee099db` (`Add legal draft mapping for MVP cases`). Nguồn tạo là VSCode AI theo prompt điều phối của ChatGPT Plus.
- Chưa có Khánh/Gemini Pro hoặc người có chuyên môn rà soát độc lập; chưa có human/legal final review và chưa xác nhận pháp lý hoàn tất. Nhãn High/Medium/Low trong draft chỉ là đánh giá sơ bộ của AI.
- RAG và AI explanation chưa triển khai. RAG **LOCKED toàn bộ 5 case**, kể cả case có nhãn High confidence, cho đến khi legal draft được rà soát độc lập.
- **Kết quả Vòng 1:** Chưa xác nhận; cần kiểm tra Dashboard cuộc thi và email/biên nhận chính thức.
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
- `[x]` Cải thiện Dashboard upload result labels: phân biệt Chế độ 1/Chế độ 2, ghi rõ nguồn kết quả và tên file upload; commit `abd9738`; test đạt `37 passed, 1 warning`.
- `[x]` GD2-04a củng cố schema validation cho upload `.xlsx`; commit `3bd1471`; toàn bộ test đạt `41 passed, 1 warning`.

## Thứ tự ưu tiên

### P1 — Tạo template Excel mẫu hoặc thêm nút tải template

- Chuẩn bị template hóa đơn và thanh toán đúng sheet/header/schema hiện tại để người dùng điền dữ liệu.
- Có thể bổ sung nút tải template trên Dashboard sau khi chốt cấu trúc; không thay đổi rule engine.

### P2 — Tạo dữ liệu lỗi hoặc edge cases bổ sung nếu cần

- Bổ sung tình huống sai kiểu dữ liệu, ô trống quan trọng, file lớn hoặc cấu trúc gần đúng nếu cần kiểm tra thực tế.
- Ưu tiên tạo trong test hoặc tempfile; không dùng dữ liệu doanh nghiệp thật.

### P3 — Rà độc lập legal draft với Khánh, không mở RAG

- Rà độc lập nguồn tạo, luật hiện hành, điều/khoản, ngoại lệ và các case Low/Medium.
- Ưu tiên mở văn bản gốc trên Cổng văn bản Chính phủ hoặc nguồn chính thức. Có thể dùng Thư Viện Pháp Luật để tra cứu phụ, nhưng không dùng làm nguồn chốt cuối.
- Khánh phải tự đọc điều/khoản trên văn bản gốc và ghi xác nhận; không copy nguyên văn nội dung AI làm kết quả rà soát.
- **Không mở RAG cho bất kỳ case nào cho đến khi legal draft được rà độc lập.** Không ghi pháp lý hoàn tất nếu chưa có bằng chứng rà soát.

### P4 — Kiểm tra kết quả Vòng 1 trên Dashboard/email

- Kiểm tra Dashboard cuộc thi, email và biên nhận chính thức.
- Chỉ cập nhật trạng thái Vòng 1 khi có bằng chứng xác nhận.

### P5 — Chuẩn bị RAG/AI explanation chỉ sau khi legal review sạch

- Chỉ bắt đầu sau khi P3 hoàn tất rà soát độc lập và có đủ căn cứ pháp lý sạch cho phạm vi MVP.
- RAG hiện vẫn `LOCKED`; AI explanation chưa triển khai.

### P6 — XML/PDF/OCR để sau

- Chưa mở rộng định dạng trước khi template `.xlsx`, dữ liệu lỗi và legal review được xử lý theo ưu tiên.
- Không gọi prototype hiện tại là hệ thống xử lý mọi định dạng.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** GD2-04a đã củng cố schema validation cho upload `.xlsx`; commit `3bd1471`. Upload hai file demo vẫn đạt `12 / 6 / 9`; toàn bộ test đạt `41 passed, 1 warning`.

**Bước đầu phiên sau:** thực hiện P1 — tạo template Excel mẫu cho hóa đơn và thanh toán hoặc thiết kế nút tải template trên Dashboard. P3 legal review độc lập có thể tiến hành song song nhưng vẫn là điều kiện bắt buộc trước RAG.

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
