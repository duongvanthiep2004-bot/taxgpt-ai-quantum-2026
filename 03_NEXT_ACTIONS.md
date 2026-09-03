# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test hồi quy hiện đạt `61 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1`, được cải thiện cho thao tác demo tại commit `67d6a4a` và phân biệt nguồn kết quả tại commit `abd9738`. Dashboard hiện có “Chế độ 1: Dữ liệu demo cố định” và “Chế độ 2: File Excel tải lên”; kết quả ghi rõ nguồn dữ liệu và hiển thị tên hai file khi có `uploaded_files`.
- Khi backend chưa chạy, Dashboard hiển thị lỗi thân thiện và không crash. Git working tree sạch sau các commit đã nêu.
- **Prototype demo local không RAG: `[x]` đạt** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- README hướng dẫn clone/cài/test/chạy backend/frontend/demo đã hoàn thành tại commit `21976fc`; repo hiện đủ hướng dẫn để người khác chạy lại prototype local bằng hai terminal.
- **GD2-04 upload file thật: `[x]` hoàn thành ở mức prototype `.xlsx`** tại commit `f84cc1f`. Streamlit nhận file hóa đơn và payment; backend xử lý qua `POST /demo/scan-uploaded`; test với hai file demo cho kết quả `12 / 6 / 9`; toàn bộ suite hồi quy hiện đạt `61 passed, 1 warning`.
- Luồng demo cố định `GET /demo/scan-all` và các endpoint cũ vẫn được giữ nguyên. `requirements.txt` đã có `python-multipart`; Git working tree sạch sau commit.
- Đây chưa phải sản phẩm hoàn chỉnh. Upload hiện chỉ hỗ trợ `.xlsx` với sheet/header/schema hiện tại và mới có data quality cơ bản; message chưa chỉ rõ số dòng lỗi, chưa giới hạn dung lượng file, chưa hỗ trợ XML/PDF/OCR, RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao.
- **GD2-04a schema validation: `[x]` hoàn thành** tại commit `3bd1471`. Backend phân biệt workbook hỏng, thiếu sheet `invoices`/`payments` và thiếu một hoặc nhiều cột bắt buộc; lỗi không lộ traceback hoặc đường dẫn file tạm. Upload demo vẫn đạt `12 / 6 / 9`.
- **GD2-04b template Excel cho upload: `[x]` hoàn thành** tại commit `e45ae30`. Repo có template hóa đơn và thanh toán đúng schema parser; Dashboard có hai nút tải template; README đã cập nhật hướng dẫn. Template chỉ phục vụ prototype `.xlsx`, không phải chuẩn dữ liệu pháp lý chính thức.
- **GD2-04c upload edge cases và data quality: `[x]` hoàn thành** tại commit `eae11a3`. Parser xử lý header-only, dòng trống, ô bắt buộc trống, ngày và số tiền không hợp lệ; demo vẫn đạt `12 / 6 / 9`, template vẫn đọc được và suite hiện đạt `61 passed, 1 warning`.
- Legal draft đã có tại `van-ban-luat/processed/GD1_5_P_LEGAL_DRAFT_mapping_5_cases.md`, commit `ee099db` (`Add legal draft mapping for MVP cases`). Nguồn tạo là VSCode AI theo prompt điều phối của ChatGPT Plus.
- Case 3 đã có initial legal source review **PARTIAL** tại commit `3b4eab3` và initial/internal impact review Luật `149/2025/QH15` tại commit `6046577`. Luật 149 sửa khoản 5 Điều 9, liên quan `vat_rate`, và bãi bỏ khoản 3 Điều 12, liên quan phạm vi phương pháp trực tiếp; chưa xác định thấy căn cứ phải đổi công thức kỹ thuật lõi chỉ do Luật 149. Technical alignment **DONE**, Legal confidence **Pending**, independent/cross review chưa có; không gọi Case 3 là hoàn tất pháp lý.
- Theo quyết định ngày 26/08/2026, đội trưởng/nhóm hiện tại chủ động đảm nhận toàn bộ nhiệm vụ để không chậm tiến độ. Khánh, Thế Anh hoặc thành viên khác nếu tham gia lại sẽ review phụ/kiểm tra chéo và không còn là blocker của tiến độ chính.
- RAG và AI explanation chưa triển khai. RAG **LOCKED toàn bộ 5 case**, kể cả case có nhãn High confidence, cho đến khi có bảng đối chiếu và bằng chứng rà văn bản gốc đủ sạch.
- **Trạng thái sơ loại/Vòng 1:** BTC hoãn sơ loại/Vòng 1 tới `09/09/2026`; đội chưa thi nên chưa có kết quả. Đây không phải trường hợp kết quả đã có nhưng chưa được kiểm tra.
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
- `[x]` GD2-CASE3-FIX chuẩn hóa `taxable_amount`/`net_amount`, bỏ phụ thuộc `expected_risk_case`, cập nhật template và test upload; commit `a60f7bc`; toàn bộ suite đạt `61 passed, 1 warning`.
- `[~]` GD1.5-CASE3-LEGAL-SOURCE-REVIEW đã hoàn thành phần initial review ở mức **PARTIAL**; commit `3b4eab3`; Legal confidence vẫn **Pending**.
- `[x]` GD1.5-CASE3-LAW149-IMPACT-REVIEW đã hoàn thành ở mức initial/internal review; commit `6046577`; không nâng Legal confidence và không mở RAG/AI explanation.

## Thứ tự ưu tiên

### P1 — Rà sâu Nghị định 181/2025/NĐ-CP cho Case 3 bằng bản đọc được/tin cậy

- Đối chiếu trực tiếp các quy định liên quan đến giá tính thuế, thuế suất và phương pháp khấu trừ; ghi rõ điều/khoản, hiệu lực và điểm còn chưa chắc chắn.

### P2 — Rà Nghị định 359/2025/NĐ-CP và 144/2026/NĐ-CP xem có sửa đổi ảnh hưởng Case 3 không

- Rà trên bản đọc được/tin cậy, đối chiếu với Nghị định `181/2025/NĐ-CP` và giữ **Pending** cho phần chưa xác minh đủ.

### P3 — Xác định rõ phạm vi phương pháp khấu trừ vs phương pháp trực tiếp

- Chốt đối tượng và điều kiện áp dụng của từng phương pháp trước khi mở rộng logic hoặc tuyên bố phạm vi Case 3.

### P4 — Nhờ Thế Anh hoặc người khác kiểm tra chéo file Case 3 nếu có thể

- Đề nghị Thế Anh hoặc một người khác đọc và hỏi lại căn cứ trong file Case 3. Đây là review phụ/kiểm tra chéo; hiện chưa có và không được ghi nhận là đã hoàn thành.

### P5 — Chuẩn bị checklist/script sơ loại 09/09

- Chuẩn bị script giới thiệu, luồng demo, checklist vận hành và phương án demo dự phòng; bổ sung slide ngắn nếu BTC yêu cầu.
- Không gọi tài liệu chuẩn bị là hồ sơ đã được BTC chấp thuận nếu chưa có xác nhận.

### P6 — RAG/AI explanation vẫn LOCKED cho đến khi legal review sạch và có kiểm tra chéo

- Chỉ xem xét RAG/AI explanation sau khi bảng đối chiếu đủ sạch và đã có kiểm tra chéo; RAG hiện vẫn **LOCKED toàn bộ 5 case**.
- XML/PDF/OCR để sau; không gọi prototype hiện tại là hệ thống xử lý mọi định dạng.

Khánh và Thế Anh nếu tham gia lại chỉ giữ vai trò review phụ/kiểm tra chéo; họ không phải blocker của tiến độ chính.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** GD2-CASE3-FIX đã chuẩn hóa `taxable_amount`/`net_amount`, bỏ phụ thuộc `expected_risk_case`, cập nhật template/test upload tại commit `a60f7bc`. Initial legal source review Case 3 đã đạt **PARTIAL** tại commit `3b4eab3`; initial/internal impact review Luật 149 đã hoàn thành tại commit `6046577`. Legal confidence vẫn **Pending**; toàn bộ suite hiện đạt `61 passed, 1 warning`.

**Bước đầu phiên sau:** thực hiện P1 — rà sâu Nghị định `181/2025/NĐ-CP` bằng bản đọc được/tin cậy, sau đó rà các nghị định sửa đổi theo P2 và xác định phạm vi hai phương pháp theo P3. Song song, nhờ Thế Anh hoặc người khác kiểm tra chéo nếu có thể và chuẩn bị checklist/script sơ loại 09/09; RAG/AI explanation vẫn **LOCKED**.

## Ước lượng tiến độ

- **Mức 1 — Prototype demo local không RAG:** `[x]` đạt ngày 18/08/2026.
- **Mức 2 — RAG pháp lý + trích dẫn + AI explanation:** phụ thuộc chất lượng bảng đối chiếu và bằng chứng rà văn bản gốc; internal legal review sơ bộ không được coi là kiểm chứng pháp lý độc lập.
- **Tổng mức trình diễn đầy đủ:** khoảng 1.5–2 tuần nếu pháp lý không bị trì hoãn.
- **Rủi ro lớn nhất hiện tại:** chất lượng và khả năng kiểm tra lại căn cứ pháp lý, không phải kỹ thuật backend.

## Chưa ưu tiên ở giai đoạn hiện tại

- OCR/PDF và luồng trích xuất chứng từ phức tạp.
- Ngoại lệ nâng cao như hóa đơn điều chỉnh/thay thế.
- Thanh toán từng phần/gộp và bù trừ công nợ.
- Các mở rộng này xếp sau upload file, ổn định Dashboard và chuẩn bị kịch bản trình diễn.

RAG cũng không được triển khai sớm chỉ để làm đẹp demo; điều kiện bắt buộc vẫn là có bảng đối chiếu và bằng chứng rà văn bản gốc đủ sạch cho phạm vi sử dụng.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
- Không gọi prototype demo local hiện tại là sản phẩm hoàn chỉnh; RAG/AI explanation chỉ được tuyên bố khi đã triển khai và kiểm chứng.
