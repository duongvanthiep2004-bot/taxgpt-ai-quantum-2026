# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test hồi quy hiện đạt `37 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1`, được cải thiện cho thao tác demo tại commit `67d6a4a` và phân biệt nguồn kết quả tại commit `abd9738`. Dashboard hiện có “Chế độ 1: Dữ liệu demo cố định” và “Chế độ 2: File Excel tải lên”; kết quả ghi rõ nguồn dữ liệu và hiển thị tên hai file khi có `uploaded_files`.
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
- `[x]` Cải thiện Dashboard upload result labels: phân biệt Chế độ 1/Chế độ 2, ghi rõ nguồn kết quả và tên file upload; commit `abd9738`; test đạt `37 passed, 1 warning`.

## Thứ tự ưu tiên

### P1 — Chuẩn bị kịch bản demo/video ngắn

- Chuẩn bị luồng trình diễn hai chế độ: demo cố định và upload hai file `.xlsx`.
- Trong mỗi luồng, đọc số liệu `12 / 6 / 9`, chỉ rõ nguồn kết quả, lọc cảnh báo và mở evidence.
- Nêu rõ đây là prototype local không RAG và không thay thế tư vấn chuyên nghiệp; chỉ quay video khi kịch bản đã được chạy thử ổn định.

### P2 — Rà độc lập nội dung legal draft, không mở RAG

- Rà độc lập nguồn tạo, luật hiện hành, điều/khoản, ngoại lệ và các case Low/Medium.
- Xác nhận rõ phần đã đối chiếu, phần còn thiếu và người chịu trách nhiệm chốt chuyên môn; không coi nhãn High/Medium/Low của AI là kết luận pháp lý.
- **Không mở RAG cho bất kỳ case nào cho đến khi legal draft được rà độc lập.** Không ghi pháp lý hoàn tất nếu chưa có bằng chứng rà soát.

### P3 — Cải thiện schema validation và upload file lỗi nếu cần

- Rà lại thông báo lỗi cho thiếu sheet, sai header, thiếu cột, workbook hỏng và file không phải `.xlsx`.
- Chỉ bổ sung khi có tình huống lỗi cụ thể; không thay đổi rule engine hoặc mở rộng định dạng ngoài phạm vi.

### P4 — Chuẩn bị dữ liệu demo bổ sung hoặc tình huống lỗi

- Chuẩn bị file mẫu nhỏ cho các trường hợp thiếu sheet/header/cột hoặc workbook không hợp lệ nếu cần trình diễn error handling.
- Không dùng dữ liệu doanh nghiệp thật và không tự thêm rule nghiệp vụ mới.

### P5 — RAG pháp lý + AI explanation chỉ sau khi legal review sạch

- Chỉ bắt đầu sau khi P2 hoàn tất rà soát độc lập và có đủ căn cứ pháp lý sạch cho phạm vi MVP.
- Trả trích dẫn nguồn và từ chối kết luận khi không đủ căn cứ.
- AI explanation chỉ giải thích cảnh báo và gợi ý rà soát, không thay chuyên gia thuế đưa ra kết luận pháp lý.

### P6 — Xử lý ngoại lệ nâng cao sau

- Xem xét hóa đơn điều chỉnh/thay thế, thanh toán từng phần/gộp và bù trừ công nợ.
- Chỉ mở rộng sau khi dashboard demo và luồng upload cơ bản đã ổn định.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** Dashboard đã phân biệt hai chế độ demo/upload và hiển thị đúng nguồn kết quả, tên file upload; commit `abd9738`. Upload hai file demo vẫn đạt `12 / 6 / 9`; toàn bộ test đạt `37 passed, 1 warning`.

**Bước đầu phiên sau:** thực hiện P1 — chuẩn bị và chạy thử kịch bản demo/video ngắn cho cả hai chế độ. P2 legal review độc lập có thể tiến hành song song nhưng vẫn là điều kiện bắt buộc trước RAG.

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
