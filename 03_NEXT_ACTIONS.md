# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test hồi quy hiện đạt `50 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1`, được cải thiện cho thao tác demo tại commit `67d6a4a` và phân biệt nguồn kết quả tại commit `abd9738`. Dashboard hiện có “Chế độ 1: Dữ liệu demo cố định” và “Chế độ 2: File Excel tải lên”; kết quả ghi rõ nguồn dữ liệu và hiển thị tên hai file khi có `uploaded_files`.
- Khi backend chưa chạy, Dashboard hiển thị lỗi thân thiện và không crash. Git working tree sạch sau các commit đã nêu.
- **Prototype demo local không RAG: `[x]` đạt** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- README hướng dẫn clone/cài/test/chạy backend/frontend/demo đã hoàn thành tại commit `21976fc`; repo hiện đủ hướng dẫn để người khác chạy lại prototype local bằng hai terminal.
- **GD2-04 upload file thật: `[x]` hoàn thành ở mức prototype `.xlsx`** tại commit `f84cc1f`. Streamlit nhận file hóa đơn và payment; backend xử lý qua `POST /demo/scan-uploaded`; test với hai file demo cho kết quả `12 / 6 / 9`; toàn bộ suite hồi quy hiện đạt `50 passed, 1 warning`.
- Luồng demo cố định `GET /demo/scan-all` và các endpoint cũ vẫn được giữ nguyên. `requirements.txt` đã có `python-multipart`; Git working tree sạch sau commit.
- Đây chưa phải sản phẩm hoàn chỉnh. Upload hiện chỉ hỗ trợ `.xlsx` với sheet/header/schema hiện tại và mới có data quality cơ bản; message chưa chỉ rõ số dòng lỗi, chưa giới hạn dung lượng file, chưa hỗ trợ XML/PDF/OCR, RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao.
- **GD2-04a schema validation: `[x]` hoàn thành** tại commit `3bd1471`. Backend phân biệt workbook hỏng, thiếu sheet `invoices`/`payments` và thiếu một hoặc nhiều cột bắt buộc; lỗi không lộ traceback hoặc đường dẫn file tạm. Upload demo vẫn đạt `12 / 6 / 9`.
- **GD2-04b template Excel cho upload: `[x]` hoàn thành** tại commit `e45ae30`. Repo có template hóa đơn và thanh toán đúng schema parser; Dashboard có hai nút tải template; README đã cập nhật hướng dẫn. Template chỉ phục vụ prototype `.xlsx`, không phải chuẩn dữ liệu pháp lý chính thức.
- **GD2-04c upload edge cases và data quality: `[x]` hoàn thành** tại commit `eae11a3`. Parser xử lý header-only, dòng trống, ô bắt buộc trống, ngày và số tiền không hợp lệ; demo vẫn đạt `12 / 6 / 9`, template vẫn đọc được và suite hiện đạt `50 passed, 1 warning`.
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
- `[x]` GD2-04b tạo hai template Excel, thêm nút tải trên Dashboard và cập nhật README; commit `e45ae30`; toàn bộ test đạt `42 passed, 1 warning`.
- `[x]` GD2-04c bổ sung edge cases và data quality cơ bản cho upload `.xlsx`; commit `eae11a3`; demo/template không hồi quy; toàn bộ test đạt `50 passed, 1 warning`.

## Thứ tự ưu tiên

### P1 — Kiểm tra kết quả Vòng 1 trên Dashboard/email/nhóm BTC

- Kiểm tra Dashboard cuộc thi, email, nhóm Ban tổ chức và biên nhận chính thức.
- Chỉ cập nhật trạng thái Vòng 1 khi có bằng chứng xác nhận.

### P2 — Giao Khánh rà độc lập legal draft, bắt đầu Case 3 trước

- Bắt đầu từ Case 3, sau đó rà độc lập nguồn tạo, luật hiện hành, điều/khoản, ngoại lệ và các case còn lại.
- Ưu tiên văn bản gốc hoặc nguồn chính thức; Khánh tự đọc và ghi xác nhận.
- **Không mở RAG cho bất kỳ case nào cho đến khi legal draft được rà độc lập.**

### P3 — Cải thiện upload UX nếu cần

- Hiển thị message lỗi rõ hơn trên Dashboard nếu trải nghiệm thực tế cho thấy cần thiết.
- Có thể thêm hướng dẫn ngắn để người dùng sửa file theo lỗi backend trả về.

### P4 — Nếu tiếp tục backend, thêm số dòng lỗi trong validation

- Bổ sung số dòng Excel có lỗi trong message mà không lộ đường dẫn file tạm hoặc traceback.
- Chỉ triển khai nếu tiếp tục ưu tiên backend upload.

### P5 — Chuẩn bị RAG/AI explanation chỉ sau khi legal review sạch

- Chỉ bắt đầu sau khi P2 hoàn tất rà soát độc lập và có đủ căn cứ pháp lý sạch cho phạm vi MVP.
- RAG hiện vẫn `LOCKED`; AI explanation chưa triển khai.

### P6 — XML/PDF/OCR để sau

- Chưa mở rộng định dạng trước khi upload UX, validation số dòng lỗi và legal review được xử lý theo ưu tiên.
- Không gọi prototype hiện tại là hệ thống xử lý mọi định dạng.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** GD2-04c đã bổ sung edge cases và data quality cơ bản cho upload `.xlsx`; commit `eae11a3`. Demo vẫn đạt `12 / 6 / 9`, hai template vẫn đọc được, toàn bộ test đạt `50 passed, 1 warning`; Git working tree sạch sau commit.

**Bước đầu phiên sau:** thực hiện P1 — kiểm tra kết quả Vòng 1 trên Dashboard/email/nhóm BTC. Đồng thời giao Khánh bắt đầu rà độc lập legal draft từ Case 3 theo P2; không mở RAG.

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
