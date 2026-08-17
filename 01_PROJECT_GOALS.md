# 01_PROJECT_GOALS.md — Mục tiêu & chia nhỏ dự án

**Cập nhật lần cuối:** 17/08/2026
**Mục tiêu tổng thể:** Xây dựng và nộp dự thi TaxGPT — trợ lý AI phát hiện rủi ro thuế và tuân thủ chứng từ cho SMEs — tại AI-Quantum Challenge 2026, HVTC.
**Ràng buộc thời gian cứng (từ thể lệ, không thay đổi được):**

| Mốc | Ngày | Còn lại (từ 09/07) |
|---|---|---|
| Hạn nộp hồ sơ Vòng 1 | 30/07/2026 | **21 ngày** |
| Phỏng vấn sơ loại | 09/08/2026 | 31 ngày |
| Công bố kết quả Vòng 1 | 20/08/2026 | 42 ngày |
| Kick-off Vòng 2 | 25/08/2026 | 47 ngày |
| Hạn nộp sản phẩm Vòng 2 | 10/10/2026 | 93 ngày |
| Thuyết trình Vòng 2 | 25/10/2026 | 108 ngày |
| Chung kết | 10/11/2026 | 124 ngày |

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
- Đây mới là runtime nền tảng, **không phải prototype nghiệp vụ hoàn chỉnh**. Dashboard chưa upload file, chưa đọc Excel, chưa gọi backend, chưa có rule engine và chưa có bảng cảnh báo.
- Sau bước khôi phục runtime, backend đã có lát cắt nghiệp vụ đầu tiên cho Case 1: `Excel hóa đơn → parser → rule hóa đơn trùng → API JSON`.

### Trạng thái triển khai backend Case 1 ngày 17/08/2026

- Parser Excel tối thiểu tại `backend/app/parsers/excel_parser.py` đọc sheet `invoices`, tự nhận diện header tại dòng Excel 4 và đọc đúng 12 hóa đơn từ `sample_invoices_mvp.xlsx`.
- Rule Case 1 tại `backend/app/rules/duplicate_invoice.py` đã có code và test; phát hiện 1 nhóm có khả năng trùng gồm `INV-DEMO-003` và `INV-DEMO-004`.
- Backend có endpoint `GET /demo/case-1-duplicates`; kết quả xác minh trả HTTP 200, `total_invoices = 12` và `total_alerts = 1`.
- Test hiện có gồm health, parser, xử lý lỗi parser, rule Case 1 và API; toàn bộ đạt `7 passed, 1 warning`. Warning TestClient không làm test thất bại.
- Case 2–5 chưa triển khai. Frontend vẫn là trang tĩnh, chưa upload file, chưa gọi backend và chưa hiển thị bảng cảnh báo. RAG và AI explanation chưa triển khai.
- Đây là **backend slice cho Case 1**, chưa phải prototype end-to-end.

### Danh sách đội đã chốt (cập nhật GD0-01)

| Thành viên | MSSV | Vai trò trong đội (điền form đăng ký) | Phụ trách chính |
|---|---|---|---|
| Dương Văn Thiệp | — | Đội trưởng – Phát triển sản phẩm chính | Kỹ thuật: rule engine, RAG, dashboard; quản lý tiến độ |
| Phạm Đình Khánh | 23021022 | Phụ trách nghiệp vụ thuế & dữ liệu | Chọn case rủi ro, dữ liệu mẫu, kiểm tra logic nghiệp vụ |
| Vũ Thế Anh | 24020837 | Phụ trách kiểm thử & thuyết trình | Test sản phẩm, ghi lỗi, slide, luyện phản biện |

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

## GIAI ĐOẠN CHỜ — Chuẩn bị trước cho Vòng 2 (30/07 – 20/08)

**Ưu tiên kỹ thuật hiện tại:** triển khai luồng tối thiểu đọc hai file Excel mẫu, chạy rule engine và đưa kết quả lên Dashboard. Không triển khai RAG trước khi rule engine hoạt động và căn cứ pháp lý được kiểm chứng.

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GDC-01 | Code module đọc XML/PDF hóa đơn | VSCode AI | Module chạy được với dữ liệu mẫu | [ ] |
| GDC-02 | Code rule engine cơ bản cho 5 case | VSCode AI | Case 1 đã có code và test; Case 2–5 chưa triển khai | [~] |
| GDC-03 | Mở rộng ngân hàng văn bản pháp luật cho case 2–5 | Gemini Pro | Bảng luật mở rộng | [ ] |
| GDC-04 | Luyện phỏng vấn sơ loại (nếu được gọi 09/08) | ChatGPT Plus (đóng vai giám khảo) | Ghi âm/ghi chú buổi luyện tập | [ ] |

## GIAI ĐOẠN 2 — Vòng 2: Prototype (25/08 – 10/10)

| ID | Việc | Phụ trách | Output/DoD | Trạng thái |
|---|---|---|---|---|
| GD2-01 | Chốt phạm vi cuối cùng sau kick-off | Con người | Tài liệu phạm vi đã chốt | [ ] |
| GD2-02 | Hoàn thiện module đọc dữ liệu (XML/PDF/Excel) | VSCode AI | Đã có parser Excel tối thiểu cho file hóa đơn mẫu; XML/PDF và parser tổng quát chưa triển khai | [~] |
| GD2-03 | Hoàn thiện rule engine 5 case | VSCode AI | Case 1 đã pass test; Case 2–5 chưa triển khai | [~] |
| GD2-04 | Xây RAG: nạp luật vào ChromaDB, tách chunk, gắn metadata | Gemini Pro + VSCode AI | Pipeline RAG trả kết quả đúng câu hỏi mẫu | [ ] |
| GD2-05 | Xây dashboard 3 màn hình | VSCode AI | Dashboard chạy demo được | [ ] |
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
