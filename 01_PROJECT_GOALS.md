# 01_PROJECT_GOALS.md — Mục tiêu & chia nhỏ dự án

**Cập nhật lần cuối:** 01/09/2026 (sau initial legal source review PARTIAL cho Case 3)
**Mục tiêu tổng thể:** Xây dựng và nộp dự thi TaxGPT — trợ lý AI phát hiện rủi ro thuế và tuân thủ chứng từ cho SMEs — tại AI-Quantum Challenge 2026, HVTC.
**Mốc thời gian cuộc thi:**

> BTC đã hoãn sơ loại/Vòng 1 tới 09/09/2026. Đội chưa thi sơ loại và chưa có kết quả. Lịch Vòng 2, kick-off và hạn nộp sau thay đổi này chưa được BTC xác nhận có dịch theo hay không; không tự giả định các mốc cũ vẫn giữ nguyên.

| Mốc | Ngày | Ghi chú thời điểm |
|---|---|---|
| Hạn nộp hồ sơ Vòng 1 | 30/07/2026 | **21 ngày** |
| Thi sơ loại/Vòng 1 | 09/09/2026 | BTC đã hoãn tới ngày này; đội chưa thi |
| Công bố kết quả Vòng 1 | Chưa xác nhận lịch mới | Chưa thi nên chưa có kết quả |
| Kick-off Vòng 2 | Mốc cũ: 25/08/2026 | Chưa xác nhận lịch mới sau khi Vòng 1 bị hoãn |
| Hạn nộp sản phẩm Vòng 2 | Mốc cũ: 10/10/2026 | Chưa xác nhận có dịch theo Vòng 1 hay không |
| Thuyết trình Vòng 2 | Mốc cũ: 25/10/2026 | Chưa xác nhận có dịch theo Vòng 1 hay không |
| Chung kết | Mốc cũ: 10/11/2026 | Chưa xác nhận có dịch theo Vòng 1 hay không |

**Quy ước Task ID:** `GD<số giai đoạn>-<số thứ tự>`. Trạng thái: `[ ]` chưa làm · `[~]` đang làm · `[x]` xong · `[!]` bị chặn (blocked).

---

## GIAI ĐOẠN 0 — Chuẩn bị nền tảng (đến 12/07)

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GD0-01 | Chốt danh sách đội (3–5 người) + phân vai trò | Con người | Danh sách tên + vai trò ghi vào log | [x] |
| GD0-02 | Tạo repo Git + thư mục tài liệu dùng chung | Con người + VSCode AI | Repo có cấu trúc thư mục cơ bản | [x] |
| GD0-03 | Brainstorm & chốt 3–5 case rủi ro thuế cụ thể | ChatGPT Plus → Con người xác nhận | Danh sách case cuối cùng, có mô tả ngắn mỗi case | [x] |
| GD0-04 | Thu thập & tóm tắt văn bản luật cho các case đã chọn | Gemini Pro | Bảng pháp lý V3 đã có khung logic kỹ thuật, còn cần con người kiểm chứng điều/khoản gốc | [~] |
| GD0-05 | Cài và khôi phục môi trường code cơ bản (Python, FastAPI, Streamlit, ChromaDB) | VSCode AI | Runtime cơ bản đã được xác minh lại ngày 17/08/2026: Python 3.12.10, pip 25.0.1, pytest 1 passed; backend `/health` trả HTTP 200 và frontend tĩnh render được | [x] |
| GD0-06 | Đăng ký đội trên hệ thống (ai-quantum.hvtc.edu.vn/register) | Con người | Đội đã đăng ký, có tài khoản Dashboard cho đội trưởng hoặc email/ảnh xác nhận | [x] Đội đã đăng ký thành công; Dashboard hiển thị mã đội AQ2026-183 và trạng thái hồ sơ APPROVED |

### Trạng thái runtime sau khi khôi phục ngày 17/08/2026

- Môi trường `.venv` đã hoạt động với Python 3.12.10 và pip 25.0.1.
- `pytest` chạy thành công: 1 test passed, 1 warning.
- Backend FastAPI chạy được; endpoint `GET /health` trả HTTP 200 OK.
- Frontend Streamlit chạy và render được trang “TaxGPT Dashboard” với danh sách tĩnh 5 case MVP.
- Đây mới là runtime nền tảng, **không phải prototype nghiệp vụ hoàn chỉnh**. Dashboard chưa upload file, chưa đọc Excel, chưa gọi backend, chưa nhận kết quả rule engine và chưa có bảng cảnh báo.
- Sau bước khôi phục runtime, backend đã có lát cắt nghiệp vụ đầu tiên cho Case 1: `Excel hóa đơn → parser → rule hóa đơn trùng → API JSON`.

### Trạng thái triển khai backend và demo local đến 18/08/2026

- Parser Excel tối thiểu tại `backend/app/parsers/excel_parser.py` đọc sheet `invoices`, tự nhận diện header tại dòng Excel 4 và đọc đúng 12 hóa đơn từ `sample_invoices_mvp.xlsx`.
- Rule Case 1 tại `backend/app/rules/duplicate_invoice.py` đã có code và test; phát hiện 1 nhóm có khả năng trùng gồm `INV-DEMO-003` và `INV-DEMO-004`.
- Backend có endpoint `GET /demo/case-1-duplicates`; kết quả xác minh trả HTTP 200, `total_invoices = 12` và `total_alerts = 1`.
- Rule Case 2 tại `backend/app/rules/buyer_info_mismatch.py`, endpoint `GET /demo/case-2-buyer-info` và test tương ứng đã hoàn thành; phát hiện 2 cảnh báo cho `INV-DEMO-005` và `INV-DEMO-006`.
- Rule Case 3 tại `backend/app/rules/vat_mismatch.py`, endpoint `GET /demo/case-3-vat-mismatch` và test tương ứng đã hoàn thành; phát hiện 2 cảnh báo cho `INV-DEMO-007` và `INV-DEMO-008`.
- Case 4 — hóa đơn ngoài kỳ dữ liệu đang rà soát — đã có backend slice ở mức parser/rule/API/test.
- Case 5 — hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt — đã có backend slice ở mức parser/rule/API/test; phát hiện cảnh báo cho `INV-DEMO-011` và `INV-DEMO-012`. Báo cáo cuối phiên chưa xác nhận commit/push phần thay đổi này.
- Như vậy, **5/5 case MVP đã có backend slice ở mức parser/rule/API/test**. Backend đã có API tổng hợp `GET /demo/scan-all`; toàn bộ test hiện đạt `33 passed, 1 warning`, warning không làm test thất bại.
- Frontend Streamlit đã kết nối `GET /demo/scan-all`. Dashboard có nút “Chạy rà soát dữ liệu demo” và hiển thị 12 hóa đơn, 6 giao dịch thanh toán, 9 cảnh báo, bảng tổng hợp 5 case cùng bảng chi tiết cảnh báo.
- RAG tiếp tục bị khóa cho đến khi nguồn, hiệu lực và điều/khoản pháp lý được con người kiểm chứng; không ingest tài liệu pháp lý chưa kiểm chứng.
- **Prototype demo local không RAG: đạt.** Phạm vi đã xác minh là `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`.
- README hướng dẫn chạy demo local đã hoàn thành tại commit `21976fc`. Repo hiện đã có đủ hướng dẫn để người khác clone, tạo môi trường Windows PowerShell, chạy test, khởi động backend/frontend bằng hai terminal và thực hiện kịch bản demo `12 hóa đơn / 6 giao dịch / 9 cảnh báo`.
- Đây không phải sản phẩm hoàn chỉnh. Upload file thật mới hoàn thành ở mức prototype `.xlsx`; chưa có RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao.
- **Prototype MVP local mức 1 đã đạt:** GD2-02 scan-all, GD2-03 dashboard và GD2-04 upload file thật mức prototype `.xlsx` đã hoàn thành; có README và repo sạch sau commit `f84cc1f` (`Implement uploaded Excel scan workflow`).
- **Phạm vi GD2-04 đã xác minh:** Streamlit cho upload hai file Excel hóa đơn và payment; backend xử lý qua `POST /demo/scan-uploaded`; khi upload hai file demo, kết quả khớp `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`. Endpoint kiểm tra thiếu file, sai định dạng, workbook/schema không hợp lệ và trả lỗi HTTP 400 thân thiện; file tạm được cleanup sau xử lý.
- **Dashboard upload đã được cải thiện ở mức demo:** Tại commit `abd9738` (`Improve dashboard upload result labels`), giao diện phân biệt rõ “Chế độ 1: Dữ liệu demo cố định” và “Chế độ 2: File Excel tải lên”. Phần kết quả cho biết nguồn là dữ liệu demo cố định hoặc file tải lên; với upload, Dashboard hiển thị tên file hóa đơn và file thanh toán từ `uploaded_files`.
- **GD2-04a schema validation đã hoàn thành:** Tại commit `3bd1471` (`Improve uploaded Excel schema validation`), parser phân biệt workbook hỏng, thiếu sheet `invoices`/`payments` và thiếu một hoặc nhiều cột bắt buộc; lỗi tiếng Việt rõ hơn, không lộ traceback hoặc đường dẫn file tạm. Không đổi rule engine, frontend hoặc mở rộng định dạng. Toàn bộ test hiện đạt `50 passed, 1 warning`; upload hai file demo vẫn khớp `12 / 6 / 9`.
- **GD2-04b template Excel cho upload đã hoàn thành:** Tại commit `e45ae30` (`Add Excel upload templates`), repo có template hóa đơn `data-mau/excel/template_invoices_mvp.xlsx` và template thanh toán `data-mau/bank_statements/template_bank_payments_mvp.xlsx`; Dashboard có hai nút tải template và README có hướng dẫn sử dụng. Đây là template phục vụ prototype `.xlsx`, không phải chuẩn dữ liệu pháp lý chính thức. Toàn bộ test hiện đạt `50 passed, 1 warning`; Git working tree sạch sau commit.
- **GD2-04c data quality cơ bản cho upload đã hoàn thành:** Tại commit `eae11a3` (`Add upload data quality checks`), parser từ chối file chỉ có header, bỏ dòng trống hoàn toàn, phát hiện ô bắt buộc trống, kiểm tra ngày và số tiền cơ bản, đồng thời giữ message HTTP 400 thân thiện. Demo vẫn đạt `12 / 6 / 9`, hai template vẫn đọc được và toàn bộ test đạt `50 passed, 1 warning`. Đây mới là validation data quality cơ bản cho upload `.xlsx`, chưa phải validation dữ liệu đầy đủ.
- **GD2-CASE3-FIX đã hoàn thành ở mức kỹ thuật:** Tại commit `a60f7bc` (`Align Case 3 VAT rule with uploaded data`), Case 3 dùng `taxable_amount` làm field nội bộ chuẩn; parser mapping `net_amount` sang `taxable_amount`, báo lỗi khi hai field xung đột; rule không còn phụ thuộc `expected_risk_case`; template và test upload đã được cập nhật. Toàn bộ suite hiện đạt `61 passed, 1 warning`.
- **Trạng thái Case 3 sau commit `3b4eab3`:** Technical alignment: **DONE**; initial legal source review: **PARTIAL**; Legal confidence: **Pending**; independent/cross review: chưa có; RAG/AI explanation: **LOCKED**. Không nâng legal confidence lên High và không mở RAG.
- **Phạm vi initial legal source review Case 3:** Đã ghi nhận trong Luật `48/2024/QH15` các điểm liên quan đến căn cứ tính thuế, giá tính thuế, thuế suất, phương pháp khấu trừ và phương pháp trực tiếp. Điểm b khoản 1 Điều 11 chỉ là cơ sở tham chiếu thận trọng cho cảnh báo kỹ thuật, không dùng để kết luận sai phạm.
- **Giới hạn Case 3 sau alignment/review sơ bộ:** Rule chưa kiểm tra `total_amount = taxable_amount + vat_amount`, chưa xử lý đầy đủ ngoại lệ làm tròn/nhiều dòng/chiết khấu. Luật `149/2025/QH15`, Nghị định `181/2025`, `359/2025`, `144/2026` và các phần chi tiết chưa đọc đủ tin cậy vẫn **Pending**; chưa có rà soát độc lập/kiểm tra chéo và RAG vẫn **LOCKED toàn bộ 5 case**.
- **Giới hạn GD2-04/GD2-04a/GD2-04b/GD2-04c:** Chỉ hỗ trợ `.xlsx` với sheet/header/schema hiện tại; message chưa chỉ rõ số dòng lỗi; chưa giới hạn dung lượng file; chưa hỗ trợ XML/PDF/OCR, RAG, AI explanation hoặc ngoại lệ nghiệp vụ nâng cao.
- **Trạng thái pháp lý:** Có legal draft do VSCode AI tạo theo prompt điều phối của ChatGPT Plus tại `van-ban-luat/processed/GD1_5_P_LEGAL_DRAFT_mapping_5_cases.md`, commit `ee099db` (`Add legal draft mapping for MVP cases`). Case 3 đã có initial legal source review **PARTIAL** tại commit `3b4eab3` (`Update Case 3 legal source review notes`), nhưng Legal confidence vẫn **Pending** và chưa xác nhận pháp lý hoàn tất.
- **Trạng thái kiểm soát:** Initial legal source review Case 3: **PARTIAL**. Independent/cross review: chưa có. RAG/AI explanation: **LOCKED toàn bộ 5 case**, kể cả case có nhãn High confidence.
- **Trạng thái sơ loại/Vòng 1:** BTC hoãn sơ loại/Vòng 1 tới 09/09/2026; đội chưa thi sơ loại và chưa có kết quả. Theo dõi thông báo chính thức và chuẩn bị cho sơ loại ngày 09/09/2026.
- **Tác động kế hoạch:** Khoảng thời gian bổ sung trước 09/09/2026 được dùng để củng cố prototype, tự rà pháp lý sơ bộ trên văn bản gốc và hoàn thiện hồ sơ/lời trình bày; không thay đổi trạng thái legal review hoặc mở RAG.

### Ước lượng tiến độ từ sau phiên 17/08/2026

- **Mức 1 — Prototype demo local không RAG:** đã đạt ngày 18/08/2026 với luồng Excel mẫu → `scan-all` → Streamlit hiển thị bảng cảnh báo.
- **Mức 2 — RAG pháp lý + trích dẫn + AI explanation:** phụ thuộc kiểm chứng pháp lý; nếu pháp lý xong trong tuần này thì cần thêm khoảng 2–3 phiên, ước tính 1–1.5 tuần.
- **Tổng mức trình diễn đầy đủ:** khoảng 1.5–2 tuần nếu pháp lý không bị trì hoãn.
- Rủi ro lớn nhất hiện tại là kiểm chứng pháp lý, không phải kỹ thuật backend.

### Danh sách đội đã chốt (cập nhật GD0-01)

| Thành viên | MSSV | Vai trò trong đội (điền form đăng ký) | Phụ trách chính |
|---|---|---|---|
| Dương Văn Thiệp | — | Đội trưởng – Phát triển sản phẩm chính | Kỹ thuật: rule engine, RAG, dashboard; quản lý tiến độ |
| Phạm Đình Khánh | 23021022 | Phụ trách nghiệp vụ thuế & dữ liệu | Chọn case rủi ro, dữ liệu mẫu, kiểm tra logic nghiệp vụ |
| Vũ Thế Anh | 24020837 | Phụ trách kiểm thử & thuyết trình | Test sản phẩm, ghi lỗi, slide, luyện phản biện |

### Quyết định điều phối mới — 26/08/2026

- Tạm thời đội trưởng/nhóm hiện tại chủ động đảm nhận toàn bộ nhiệm vụ kỹ thuật, tài liệu, rà soát pháp lý sơ bộ và chuẩn bị cuộc thi; không chờ thành viên khác để tránh chậm tiến độ.
- Đây là giải pháp cần thiết để giữ tiến độ nhưng tạo **rủi ro quá tải và tự duyệt ở mức cao** cho đội trưởng. Rủi ro phụ thuộc vào một người, thiếu phân tách người làm/người duyệt đã được cảnh báo từ đầu dự án và nay đã thành hiện thực ở mức cao hơn.
- Nên kích hoạt lại Thế Anh ở mức kiểm tra chéo tối thiểu: đọc bảng đối chiếu Case 3, hỏi lại căn cứ, test 15–20 tình huống và hỗ trợ checklist/demo sơ loại.
- Nếu Thế Anh, Khánh hoặc thành viên khác tham gia lại, họ chỉ giữ vai trò review phụ, đối chiếu hoặc kiểm tra chéo; việc phản hồi hay tham gia lại của họ không phải blocker của tiến độ chính.
- Phần pháp lý do đội trưởng/nhóm hiện tại tự rà chỉ là **internal legal review sơ bộ**, không được gọi là kiểm chứng pháp lý độc lập và không xác nhận pháp lý đã hoàn tất.
- RAG tiếp tục **LOCKED toàn bộ 5 case**. Không mở RAG nếu chưa có bảng đối chiếu và bằng chứng rà văn bản gốc đủ sạch cho phạm vi dự kiến sử dụng.

### 5 case MVP đã chốt cho TaxGPT (cập nhật GD0-03)

| STT | Case rủi ro | Mô tả ngắn | Lý do chọn cho prototype |
|---|---|---|---|
| 1 | Hóa đơn trùng | Một hóa đơn đầu vào bị ghi nhận nhiều lần trong bảng kê hoặc dữ liệu kế toán. | Rule rõ, dễ demo bằng XML/Excel, ít phụ thuộc diễn giải pháp lý. |
| 2 | Sai MST/tên người mua | Hóa đơn có mã số thuế hoặc tên người mua không khớp với dữ liệu doanh nghiệp. | Rất phổ biến, dễ kiểm tra với master data doanh nghiệp. |
| 3 | VAT không khớp phép tính | Tiền VAT không khớp với giá trị trước thuế nhân thuế suất, hoặc tổng tiền không bằng trước thuế cộng VAT. | Có thể kiểm tra bằng phép tính số học, dễ chứng minh trong dashboard. |
| 4 | Hóa đơn đầu vào ngoài kỳ kê khai | Hóa đơn có ngày phát sinh không thuộc kỳ kê khai đang kiểm tra. | Dễ demo bằng so sánh ngày hóa đơn với kỳ khai báo. |
| 5 | Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt | Hóa đơn từ ngưỡng cấu hình trở lên nhưng chưa tìm thấy chứng từ thanh toán qua ngân hàng tương ứng. | Giá trị nghiệp vụ cao, phù hợp SMEs, cần đối chiếu luật gốc ở GD0-04. |

## GIAI ĐOẠN 1 — Hồ sơ Vòng 1 (đến 30/07) ⚠️ ưu tiên cao nhất

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GD1-P1 | Kiểm chứng pháp lý và tạo bản diễn đạt an toàn cho hồ sơ Vòng 1 | ChatGPT Plus → Con người kiểm chứng | Bản diễn đạt an toàn cho 5 case MVP; tiếp tục đối chiếu văn bản gốc trước khi dùng pháp lý chi tiết | [~] Đã có bản diễn đạt pháp lý an toàn cho hồ sơ Vòng 1; chưa chốt kiểm chứng pháp lý đầy đủ |
| GD1-01 | Viết draft mô tả vấn đề (SMEs & rủi ro thuế) | ChatGPT Plus | Đoạn mô tả vấn đề, có đánh dấu chỗ cần kiểm chứng số liệu | [ ] |
| GD1-02 | Đối chiếu số liệu/điều luật trong draft GD1-01 | Gemini Pro | Danh sách điểm đã xác minh / chưa xác minh | [x] Đã tạo và review đạt file docs/proposal/GD1-02_solution_overview.md |
| GD1-03 | Hoàn thiện Bản mô tả ý tưởng theo đúng 4 mục Điều 5 | ChatGPT Plus → Con người | File mô tả ý tưởng hoàn chỉnh | [x] Đã tạo và review đạt dữ liệu mẫu cho 5 case MVP |
| GD1-04 | Vẽ sơ đồ kiến trúc + viết mô tả từng bước | ChatGPT Plus + Con người | Sơ đồ + đoạn mô tả cho phiếu đăng ký | [x] Đã tạo và review đạt file docs/proposal/GD1-04_technical_architecture.md |
| GD1-05 | Tổng hợp bản mô tả ý tưởng hoàn chỉnh cho hồ sơ Vòng 1 | VSCode AI | Cấu trúc thư mục backend/frontend sẵn sàng | [x] Đã tạo và review đạt bản master docs/proposal/GD1-05_round1_idea_description.md |
| GD1-06 | Phản biện thử bản mô tả ý tưởng theo đúng bảng tiêu chí Vòng 1 | ChatGPT Plus (đóng vai giám khảo) | Danh sách điểm yếu cần sửa | [x] Đã tạo báo cáo phản biện docs/proposal/GD1-06_round1_critique.md, điểm 7,4/10, có 15 câu hỏi giám khảo |
| GD1-07 | Chỉnh sửa theo phản biện GD1-06 | Con người | Bản mô tả ý tưởng bản 2 | [x] Đã tạo và review đạt bản v2 docs/proposal/GD1-07_round1_idea_description_v2.md; dùng làm master hiện hành |
| GD1-08 | Chuẩn bị dữ liệu mẫu (hóa đơn giả lập) chứng minh tính khả thi dữ liệu | ChatGPT Plus + Con người | File dữ liệu mẫu | [ ] |
| GD1-09 | Viết mục khai báo AI dựa trên 02_SESSION_LOG.md | Con người | Đoạn khai báo AI cho phiếu đăng ký | [ ] |
| GD1-10 | Rà soát cuối & nộp hồ sơ | Con người | Hồ sơ đã nộp trên hệ thống, có biên nhận | [ ] |

## GIAI ĐOẠN CHỜ — Chuẩn bị sơ loại/Vòng 1 (30/07 – 09/09)

**Ưu tiên hiện tại:** Theo dõi thông báo chính thức và chuẩn bị cho sơ loại/Vòng 1 ngày 09/09/2026, đồng thời củng cố prototype, tự rà pháp lý sơ bộ từ Case 3 trên văn bản gốc và hoàn thiện hồ sơ/lời trình bày. Không chờ thành viên khác và không triển khai RAG khi chưa có bằng chứng rà nguồn đủ sạch.

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GDC-01 | Code module đọc XML/PDF hóa đơn | VSCode AI | Module chạy được với dữ liệu mẫu | [ ] |
| GDC-02 | Code rule engine cơ bản cho 5 case | VSCode AI | 5/5 case MVP đã có backend slice ở mức parser/rule/API/test; scan-all đã hoàn thành; Case 3 đã alignment với upload; toàn bộ suite hồi quy hiện đạt 61 passed, 1 warning | [x] |
| GDC-03 | Mở rộng ngân hàng văn bản pháp luật cho case 2–5 | Gemini Pro | Bảng luật mở rộng | [ ] |
| GDC-04 | Luyện phỏng vấn sơ loại ngày 09/09/2026 | Đội trưởng/nhóm hiện tại + ChatGPT Plus (đóng vai giám khảo) | Checklist, lời giới thiệu, ghi âm/ghi chú buổi luyện tập | [ ] |

## GIAI ĐOẠN 2 — Prototype/Vòng 2 (lịch cũ 25/08 – 10/10; chờ BTC cập nhật sau sơ loại)

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GD2-01 | Chốt phạm vi cuối cùng sau kick-off | Con người | Tài liệu phạm vi đã chốt | [ ] |
| GD2-02 | Hoàn thiện API tổng hợp scan-all cho 5 case MVP | VSCode AI | 5/5 case MVP và API `GET /demo/scan-all` đã có code/test; toàn bộ suite hồi quy hiện đạt 50 passed, 1 warning | [x] |
| GD2-03 | Hoàn thiện dashboard demo local | VSCode AI | Dashboard local đã gọi scan-all, hiển thị tổng quan/bảng cảnh báo; phân biệt chế độ demo cố định và file tải lên, đồng thời hiển thị nguồn kết quả và tên file upload; commit `abd9738` | [x] Hoàn thành ở mức demo |
| GD2-04 | Upload file thật cho Excel hóa đơn và payment | VSCode AI | Streamlit nhận hai file `.xlsx`; backend xử lý qua `POST /demo/scan-uploaded`, kiểm tra đầu vào và trả kết quả khớp `12 / 6 / 9` với hai file demo; commit `f84cc1f`; suite hồi quy hiện đạt `50 passed, 1 warning` | [x] Hoàn thành ở mức prototype `.xlsx` |
| GD2-04a | Củng cố schema validation và xử lý file upload lỗi | VSCode AI | Phân biệt workbook hỏng, thiếu sheet `invoices`/`payments`, thiếu một hoặc nhiều cột; lỗi tiếng Việt không lộ traceback/đường dẫn file tạm; commit `3bd1471`; test đạt `41 passed, 1 warning` | [x] Hoàn thành, không mở rộng định dạng |
| GD2-04b | Tạo template Excel cho upload | VSCode AI | Hai template hóa đơn/thanh toán đúng sheet/header/schema parser; Dashboard có nút tải, README có hướng dẫn; commit `e45ae30`; suite hiện đạt `42 passed, 1 warning` | [x] Hoàn thành ở mức prototype `.xlsx` |
| GD2-04c | Kiểm tra edge cases và data quality cơ bản cho upload | VSCode AI | Từ chối header-only, bỏ dòng trống, kiểm tra ô bắt buộc, ngày và số tiền; commit `eae11a3`; demo/template không hồi quy; suite hiện đạt `50 passed, 1 warning` | [x] Hoàn thành ở mức validation cơ bản `.xlsx` |
| GD2-05 | Xây RAG: nạp luật vào ChromaDB, tách chunk, gắn metadata | Đội trưởng/nhóm hiện tại + AI kỹ thuật | Chỉ xem xét sau khi có bảng đối chiếu và bằng chứng rà văn bản gốc đủ sạch; hiện **LOCKED toàn bộ 5 case** | [!] |
| GD2-06 | Test 15–20 tình huống thực tế | Con người + VSCode AI | Bảng kết quả test | [ ] |
| GD2-07 | Viết báo cáo giải pháp 8–12 trang | ChatGPT Plus → Con người | File báo cáo hoàn chỉnh | [ ] |
| GD2-08 | Làm slide + quay video demo dự phòng | Con người | Slide + video | [ ] |
| GD2-09 | Nộp sản phẩm Vòng 2 | Con người | Đã nộp, có biên nhận | [ ] |

## GIAI ĐOẠN 3 — Thuyết trình Vòng 2 (đến 25/10)

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GD3-01 | Luyện pitch + phản biện theo tiêu chí Vòng 2 | ChatGPT Plus (giám khảo) | Ghi chú các câu hỏi khó + cách trả lời | [ ] |
| GD3-02 | Chuẩn bị demo dự phòng | Con người | Video/backup sẵn sàng | [ ] |

## GIAI ĐOẠN 4 — Chung kết (đến 10/11)

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GD4-01 | Luyện phản biện: đạo đức AI, thương mại hóa, SHTT | ChatGPT Plus (giám khảo) | Ghi chú câu trả lời chuẩn bị sẵn | [ ] |
| GD4-02 | Chuẩn bị khu vực demo + phương án dự phòng mạng | Con người | Checklist thiết bị | [ ] |
