# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

### 11/09/2026 — UI dashboard đã refactor thành sidebar 6 mục và đã kiểm thử

- **UI refactor: DONE; QA sau UI refactor: DONE** theo kết quả người dùng cung cấp. Commit đã push lên GitHub/main: `e8f8efc0334a57f7caa4abcbf2972b3e2eb29f5f` — `Refactor Streamlit dashboard navigation`.
- **Sidebar 6 mục:** Tổng quan; Chạy demo cố định; Upload file Excel; Kết quả rà soát; Evidence chi tiết; Hướng dẫn & giới hạn. Không còn dồn toàn bộ demo/upload/kết quả/evidence trên một màn hình.
- **Session state:** Chạy demo/upload thành công lưu kết quả để xem ở Kết quả rà soát và Evidence chi tiết. Khi backend/API lỗi, kết quả cũ được xóa, không hiển thị như kết quả mới. Backend-off fallback đã PASS: báo lỗi thân thiện, không giữ 12/6/9 cũ trên màn hình chạy demo.
- **Kiểm thử được báo cáo:** `python -m pytest`: `61 passed, 1 warning`; backend/frontend khởi động được; sidebar, Tổng quan, demo cố định, upload sample, Kết quả rà soát và evidence Case 3 đều PASS. Demo và upload giữ `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`, bảng case `1 / 2 / 2 / 2 / 2`; không thấy wording nguy hiểm.
- **Phạm vi:** Cải tiến UI/UX cho demo; không thay đổi backend, rule, legal hoặc RAG. Legal confidence **Pending**; RAG/AI explanation **LOCKED toàn bộ 5 case**. Đây không phải kiểm chứng pháp lý độc lập.
- **Git trước phiên cập nhật tài liệu:** HEAD khớp commit trên, tracked files sạch; còn untracked `Báo cáo các tài liệu về thuế cho TaxGPT.docx` và `docs/report_assets/`. Không sửa hoặc commit hai mục này.


### Cập nhật điều phối 11/09/2026 — P0 Streamlit upload sample đã hoàn tất

- **P0 `[x]`:** Đã sửa `StreamlitAPIException` khi upload sample tại `frontend/streamlit_app/app.py`. Nguyên nhân là `.write(label, filename)` tạo nhiều phần tử trong một placeholder/column; đã đổi sang `.markdown(f"...")` với một chuỗi duy nhất cho từng cột.
- **Commit đã push:** `bceda11545ce1837499cd33b78ac909d7b499aa1` — `Fix Streamlit upload result placeholder rendering`. Push GitHub thành công: `b5ebb5f..bceda11 main -> main`.
- **Git sau push, trước cập nhật điều phối:** Tracked files sạch. Còn untracked `Báo cáo các tài liệu về thuế cho TaxGPT.docx` và `docs/report_assets/`; không commit hai mục này trong nhiệm vụ hiện tại.
- **Trạng thái giữ nguyên:** Legal confidence **Pending**; RAG/AI explanation **LOCKED toàn bộ 5 case**. Vòng 1: **09/09/2026**; theo thông tin đội trưởng cung cấp, đội chưa thi và chưa có kết quả.
- **Ưu tiên tiếp theo:** P1 tập demo theo script với UI mới; P2 chuẩn bị Q&A giám khảo; P3 nếu còn thời gian nhờ Thế Anh chạy checklist độc lập trên UI mới; P4 sau sơ loại quay lại roadmap bốn giai đoạn.


- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- API tổng hợp `GET /demo/scan-all` đã hoàn thành tại commit `667bf24`; toàn bộ test hồi quy hiện đạt `61 passed, 1 warning`.
- Streamlit Dashboard đã kết nối scan-all tại commit `a13dfd1`, được cải thiện cho thao tác demo tại commit `67d6a4a` và phân biệt nguồn kết quả tại commit `abd9738`. Dashboard hiện dùng sidebar 6 mục tại commit `e8f8efc`, tách demo cố định và upload Excel; kết quả ghi rõ nguồn dữ liệu và hiển thị tên hai file khi có `uploaded_files`.
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

- `[x]` Đã tạo [demo script sơ loại 5–7 phút](docs/demo/ROUND1_DEMO_SCRIPT_2026-09-09.md) và [QA checklist 20 kịch bản](docs/demo/ROUND1_QA_CHECKLIST.md) ngày 11/09/2026, có Codex hỗ trợ soạn. Đây là bản chuẩn bị để đội đọc/chỉnh và tập; checklist QA-01–QA-20 đã **Pass** do Dương Văn Thiệp chạy thủ công; smoke test sau refactor UI **PASS** theo cập nhật người dùng. Chưa ghi nhận Thế Anh chạy checklist độc lập. Legal confidence **Pending**; RAG/AI explanation **LOCKED**.

- `[x]` P0 sửa lỗi Streamlit upload sample và push GitHub thành công; commit `bceda11545ce1837499cd33b78ac909d7b499aa1` (`Fix Streamlit upload result placeholder rendering`).

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

### P1 — Tập demo theo script với UI mới

- Tập theo [demo script](docs/demo/ROUND1_DEMO_SCRIPT_2026-09-09.md), mục tiêu 5–7 phút. Khi tập, chuyển bằng sidebar giữa demo/upload, Kết quả rà soát và Evidence chi tiết thay vì tìm toàn bộ nội dung trên một màn hình.
- Luyện kết quả 12/6/9, bảng case 1/2/2/2/2, evidence Case 3 và phương án backend-off; giữ wording an toàn. Vòng 1 vẫn ghi 09/09/2026; chưa có cập nhật đội đã thi hoặc có kết quả.

### P2 — Chuẩn bị Q&A cho giám khảo

- Chuẩn bị câu trả lời về bài toán SMEs, phạm vi 5 case, dữ liệu giả lập, cách đọc cảnh báo/evidence, giới hạn MVP và lý do chưa mở RAG. Không tuyên bố thay thế chuyên gia hoặc kết luận doanh nghiệp vi phạm.

### P3 — Nếu còn thời gian, nhờ Thế Anh chạy checklist độc lập trên UI mới

- Dùng [QA checklist](docs/demo/ROUND1_QA_CHECKLIST.md), ghi rõ người chạy và kết quả thực tế; không sao chép lượt Pass của Thiệp thành lượt kiểm tra độc lập của Thế Anh. Đây là bước bổ sung, không phải kiểm chứng pháp lý độc lập.

### P4 — Sau sơ loại quay lại roadmap bốn giai đoạn

1. Hoàn thiện MVP: củng cố vận hành, QA và xử lý các giới hạn còn lại.
2. Mở rộng dữ liệu XML/PDF/OCR theo phạm vi được chốt sau sơ loại.
3. Tăng năng lực pháp lý: tiếp tục rà sâu NĐ 359/144, đối chiếu NĐ 181 và các case pháp lý còn lại, bổ sung kiểm tra chéo.
4. Sản phẩm hóa theo nhu cầu và phạm vi được đội xác nhận.

Legal confidence vẫn **Pending**; RAG/AI explanation **LOCKED toàn bộ 5 case**. Roadmap không đồng nghĩa cho phép mở RAG; chỉ xem xét khi nguồn và phạm vi pháp lý được rà đủ sạch, có kiểm tra chéo.

## Bước tiếp theo cụ thể

**Đã hoàn thành:** UI refactor **DONE**, QA sau UI refactor **DONE** theo kết quả được báo cáo; commit `e8f8efc` đã push. Demo/upload 12/6/9, evidence Case 3 và backend-off fallback PASS. Kết quả pytest được người dùng cung cấp là `61 passed, 1 warning`; lần thử chạy lại của Codex trong phiên tài liệu bị chặn bởi Python 3.12 thiếu tại đường dẫn .venv cấu hình.

**Bước đầu phiên sau:** Tập demo theo UI sidebar mới và chuẩn bị Q&A; nếu còn thời gian nhờ Thế Anh chạy checklist độc lập. Sau sơ loại mới quay lại roadmap bốn giai đoạn. Legal confidence **Pending**; RAG/AI explanation **LOCKED**.

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
