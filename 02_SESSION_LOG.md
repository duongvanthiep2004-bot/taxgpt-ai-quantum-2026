# 02_SESSION_LOG.md — Nhật ký làm việc

> **QUY TẮC: File này chỉ được THÊM entry mới, không sửa/xóa entry cũ.**
> Đây là nguồn dữ liệu để viết mục khai báo AI (Điều 5 thể lệ) — càng đầy đủ càng tốt.
> Entry mới nhất thêm ở CUỐI file (thứ tự thời gian tăng dần).

## Mẫu entry (copy khối này cho mỗi phiên làm việc mới)

```
### [Ngày] — [Task ID] — [Tên việc ngắn gọn]
- **AI/công cụ dùng:** (ChatGPT Plus / Gemini Pro / VSCode AI / Claude / không dùng AI)
- **Người thực hiện:** 
- **Việc đã làm:** (mô tả ngắn 1-3 câu)
- **Kết quả/Output:** (tóm tắt hoặc đường dẫn file)
- **Vấn đề phát sinh:** (nếu có, ghi rõ để xử lý ở phiên sau)
- **Quyết định:** (Đạt / Cần sửa / Từ chối — ai xác nhận)
```

---

### 09/07/2026 — Thiết lập hệ thống — Xây dựng bộ 4 file điều phối
- **AI/công cụ dùng:** Claude
- **Người thực hiện:** Trưởng nhóm (qua chat với Claude)
- **Việc đã làm:** Thiết kế và tạo bộ 4 file điều phối (00_AGENTS, 01_PROJECT_GOALS, 02_SESSION_LOG, 03_NEXT_ACTIONS) dựa trên đề xuất mô hình làm việc của người dùng, có tối ưu: phân biệt log/state, thêm Task ID xuyên suốt, định nghĩa vai trò điều phối của Claude, thêm system prompt mẫu cho ChatGPT/Gemini.
- **Kết quả/Output:** 4 file trong thư mục `taxgpt-dieuphoi/`.
- **Vấn đề phát sinh:** Chưa có: chưa chốt danh sách đội (GD0-01), chưa có repo Git thực tế (GD0-02).
- **Quyết định:** Đạt — sẵn sàng bắt đầu Giai đoạn 0.

---

### 09/07/2026 — GD0-01 — Chốt danh sách đội & phân vai trò
- **AI/công cụ dùng:** Claude (đề xuất ban đầu), ChatGPT Plus (đề xuất phương án chi tiết hơn, được đội chọn)
- **Người thực hiện:** Dương Văn Thiệp
- **Việc đã làm:** Chốt 3 thành viên và vai trò: Dương Văn Thiệp — Đội trưởng & Phát triển sản phẩm chính; Phạm Đình Khánh (23021022) — Phụ trách nghiệp vụ thuế & dữ liệu; Vũ Thế Anh (24020837) — Phụ trách kiểm thử & thuyết trình.
- **Kết quả/Output:** Đã cập nhật bảng "Danh sách đội đã chốt" trong 01_PROJECT_GOALS.md và mục 3.5 trong 00_AGENTS.md. Đã điền vào form đăng ký chính thức.
- **Vấn đề phát sinh:** Rủi ro nghẽn việc ở đội trưởng do gánh cả vai trò phát triển chính lẫn quản lý — cần san sẻ việc nhắc deadline cho 2 thành viên khi vào Vòng 2.
- **Quyết định:** Đạt — GD0-01 hoàn thành, đã đánh dấu [x].

### 09/07/2026 — GD0-02 — Tạo repo Git và cấu trúc thư mục dự án
- **AI/công cụ dùng:** ChatGPT Plus trong VSCode
- **Người thực hiện:** Dương Văn Thiệp
- **Việc đã làm:** Tạo cấu trúc thư mục cơ bản cho dự án TaxGPT gồm backend, frontend, data-mau, van-ban-luat, docs và scripts. Sao chép 6 file điều phối hiện có vào docs/dieuphoi/ để VSCode AI có thể đọc trực tiếp trong repo.
- **Kết quả/Output:** Đã tạo cây thư mục backend/app/api, core, parsers, rules, rag, backend/tests, frontend/streamlit_app, data-mau, van-ban-luat, docs/proposal, docs/demo, docs/dieuphoi và scripts. Đã tạo README.md mô tả mục tiêu MVP, 5 case rủi ro và nguyên tắc pháp lý. Hash của 6 bản sao trong docs/dieuphoi/ khớp file gốc.
- **Vấn đề phát sinh:** Ban đầu các file điều phối nằm ở thư mục gốc, không nằm trong /docs/dieuphoi/ như kế hoạch ban đầu; đã xử lý bằng cách copy file gốc vào docs/dieuphoi/ thay vì di chuyển.
- **Quyết định:** Đạt — GD0-02 hoàn thành, có thể đánh dấu [x].

### 09/07/2026 — GD0-03 — Brainstorm và chốt 5 case rủi ro thuế MVP
- **AI/công cụ dùng:** ChatGPT Plus + Claude kiểm tra
- **Người thực hiện:** Dương Văn Thiệp
- **Việc đã làm:** Brainstorm 10 rủi ro thuế/kê khai phổ biến mà SMEs Việt Nam hay gặp khi xử lý hóa đơn, chứng từ, VAT và chi phí được trừ. Sau đó lọc theo tiêu chí: dễ demo, dữ liệu rõ, rule phát hiện đơn giản, phù hợp TaxGPT và hạn chế rủi ro pháp lý.
- **Kết quả/Output:** Chốt 5 case MVP cho prototype: (1) Hóa đơn trùng; (2) Sai MST/tên người mua; (3) VAT không khớp phép tính; (4) Hóa đơn đầu vào ngoài kỳ kê khai; (5) Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- **Vấn đề phát sinh:** Các căn cứ pháp lý cho case 2, 4 và 5 cần được kiểm chứng bằng văn bản luật gốc trong GD0-04 trước khi đưa vào hồ sơ hoặc rule engine.
- **Quyết định:** Đạt — GD0-03 hoàn thành, đã đánh dấu [x].

### 26/07/2026 — GD0-04 — Rà soát căn cứ pháp lý cho 5 case MVP
- **AI/công cụ dùng:** Gemini Pro + ChatGPT kiểm tra điều phối
- **Người thực hiện:** Dương Văn Thiệp
- **Việc đã làm:** Dùng Gemini Pro tạo các bản rà soát căn cứ pháp lý cho 5 case MVP. Sau khi phát hiện bản đầu và bản V2 còn mâu thuẫn, tiếp tục yêu cầu Gemini tạo bản V3 an toàn hơn, chỉ giữ vai trò cảnh báo kỹ thuật và tránh kết luận pháp lý quá mức.
- **Kết quả/Output:** Đã tạo file `van-ban-luat/processed/GD0-04_legal_basis_5_cases_v3_reviewed.md`. File V3 phân loại 5 case, mức cảnh báo, rule TaxGPT được phép chạy, ngoại lệ cần xử lý và các kết luận không được đưa vào rule engine.
- **Vấn đề phát sinh:** Gemini tự kết luận rằng các văn bản/điều khoản trong bảng vẫn cần con người kiểm chứng điều/khoản gốc và xác thực trích đoạn nguyên văn. Vì vậy GD0-04 mới hoàn thành phần khung logic kỹ thuật, chưa hoàn thành phần pháp lý chính thức.
- **Quyết định:** Đang làm — cập nhật GD0-04 thành [~], chưa đánh dấu [x] cho đến khi có kiểm chứng nguồn luật gốc.

<!-- Thêm entry mới bên dưới dòng này -->
### 09/07/2026 — GD0-03 — Brainstorm & chốt case rủi ro thuế
- **AI/công cụ dùng:** ChatGPT Plus + Claude kiểm tra
- **Người thực hiện:** Trưởng nhóm
- **Việc đã làm:** Dùng ChatGPT Plus brainstorm 10 rủi ro thuế/kê khai phổ biến cho SMEs khi xử lý hóa đơn, chứng từ, VAT và chi phí được trừ. Claude rà soát lại theo tiêu chí: dễ demo, dữ liệu rõ, rule phát hiện đơn giản, phù hợp TaxGPT và hạn chế rủi ro pháp lý.
- **Kết quả/Output:** Chốt đề xuất 5 case MVP: (1) Hóa đơn trùng; (2) Sai MST/tên người mua; (3) VAT không khớp phép tính; (4) Hóa đơn đầu vào sau kỳ kê khai; (5) Thiếu chứng từ thanh toán không tiền mặt.
- **Vấn đề phát sinh:** Các căn cứ pháp lý cho case 2, 4, 5 cần được Gemini Pro đối chiếu với văn bản luật gốc trước khi dùng trong hồ sơ hoặc prototype.
- **Quyết định:** Đạt — có thể cập nhật GD0-03 thành [x] trong 01_PROJECT_GOALS.md nếu đội xác nhận 5 case trên.

### 26/07/2026 — GD0-05 — Cài môi trường code cơ bản

- Tool/AI: ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- Mục tiêu: Thiết lập môi trường Python tối thiểu cho TaxGPT.
- Việc đã làm:
  - Tạo `requirements.txt`.
  - Tạo `.env.example`.
  - Tạo `backend/storage/` và `backend/storage/chroma/`.
  - Tạo FastAPI app tối thiểu tại `backend/app/main.py`.
  - Tạo endpoint `GET /health`.
  - Tạo test `backend/tests/test_health.py`.
  - Tạo Streamlit app tối thiểu tại `frontend/streamlit_app/app.py`.
  - Cập nhật README.md với hướng dẫn cài đặt/chạy backend/frontend.
  - Tạo `pytest.ini` để pytest import được package `backend`.
- Kết quả kiểm tra:
  - Python trong venv: 3.12.10.
  - Dependencies: cài thành công.
  - Pytest: 1 test passed.
  - Backend `/health`: trả đúng `{"status":"ok","service":"TaxGPT backend"}`.
  - Frontend: Streamlit Dashboard chạy được và hiển thị 5 case MVP.
- Trạng thái: GD0-05 hoàn thành `[x]`.
- Ghi chú: GD0-04 vẫn giữ `[~]` nếu chưa kiểm chứng xong điều/khoản pháp lý gốc.

### 09/07/2026 — GD0-06 — Kiểm tra trạng thái nộp form đăng ký đội

- **AI/công cụ dùng:** ChatGPT Plus/VSCode AI + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Kiểm tra lại trạng thái đăng ký đội trên hệ thống AI-Quantum Challenge. Trang đăng ký vẫn hiển thị nút “Gửi đăng ký”, Dashboard chuyển hướng về trang đăng nhập, chưa có bằng chứng email xác nhận/biên nhận/Dashboard.
- **Kết quả/Output:** Tạm kết luận trạng thái C — chưa có căn cứ chứng minh đã bấm nộp form. GD0-06 giữ `[~]`, chưa đánh dấu `[x]`.
- **Vấn đề phát sinh:** Cần đội trưởng đăng nhập/thử nộp lại form và lưu bằng chứng xác nhận.
- **Quyết định:** Cần xử lý tiếp — chưa hoàn thành GD0-06.

### 09/07/2026 — GD0-06 — Xác nhận đăng ký đội thành công

- **AI/công cụ dùng:** ChatGPT điều phối + kiểm tra bằng ảnh Dashboard do đội trưởng cung cấp.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Kiểm tra lại Dashboard của cuộc thi AI-Quantum Challenge sau khi đăng ký đội.
- **Kết quả/Output:** Dashboard hiển thị mã đội `AQ2026-183` và trạng thái hồ sơ `APPROVED`. Có thể xác nhận đội đã đăng ký thành công.
- **Vấn đề phát sinh:** Phần nộp hồ sơ/sản phẩm Vòng 1 vẫn chưa hoàn tất, cần xử lý ở các nhiệm vụ Giai đoạn 1.
- **Quyết định:** Đạt — GD0-06 hoàn thành `[x]`.

### 09/07/2026 — GD1-P1 — Tạo bản diễn đạt pháp lý an toàn cho hồ sơ Vòng 1

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tạo bản diễn đạt pháp lý an toàn cho 5 case MVP, phục vụ hồ sơ Vòng 1. Nội dung nhấn mạnh TaxGPT chỉ cảnh báo rủi ro và gợi ý kiểm tra, không kết luận đúng/sai pháp lý tuyệt đối.
- **Kết quả/Output:** Tạo file `van-ban-luat/processed/GD1-P1_safe_legal_wording_for_round1.md`. Case 5 không nêu ngưỡng tiền cụ thể; đoạn có thể đưa vào hồ sơ dài 169 từ.
- **Vấn đề phát sinh:** Chưa hoàn tất kiểm chứng pháp lý đầy đủ với văn bản gốc. Cần chuyên gia/con người đối chiếu tiếp trước khi demo hoặc nộp nội dung pháp lý chi tiết.
- **Quyết định:** Đạt cho phạm vi hồ sơ Vòng 1; GD1-P1 vẫn giữ `[~]` cho mục tiêu kiểm chứng pháp lý đầy đủ.

### 09/07/2026 — GD1-02 — Viết mô tả giải pháp TaxGPT

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tạo và review file mô tả giải pháp TaxGPT cho hồ sơ Vòng 1. Nội dung trình bày tổng quan giải pháp, đối tượng sử dụng, luồng xử lý, 5 chức năng MVP, thành phần kỹ thuật dự kiến, vai trò của AI, điểm khác biệt, giới hạn MVP và kết luận.
- **Kết quả/Output:** Tạo file `docs/proposal/GD1-02_solution_overview.md`. File đủ 9 mục, đủ 5 chức năng MVP, không nêu ngưỡng tiền cụ thể cho case 5, không có tuyên bố tuân thủ tuyệt đối.
- **Vấn đề phát sinh:** Cần tiếp tục kiểm tra tính khả thi của định dạng đầu vào, chất lượng kho RAG và căn cứ pháp lý trước demo chính thức.
- **Quyết định:** Đạt — GD1-02 hoàn thành `[x]`.

### 09/07/2026 — GD1-03 — Chuẩn bị dữ liệu mẫu cho 5 case MVP

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + OpenPyXL + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tạo và review bộ dữ liệu mẫu giả lập cho 5 case MVP của TaxGPT, gồm file hóa đơn mẫu, file thanh toán mẫu và tài liệu mô tả kế hoạch dữ liệu.
- **Kết quả/Output:** Tạo `data-mau/excel/sample_invoices_mvp.xlsx` gồm 12 hóa đơn; tạo `data-mau/bank_statements/sample_bank_payments_mvp.xlsx` gồm 6 giao dịch; tạo `docs/proposal/GD1-03_sample_data_plan.md`. Mỗi case MVP có 2 dòng minh họa và có thêm 2 hóa đơn bình thường.
- **Vấn đề phát sinh:** Cần con người xác nhận hồ sơ tham chiếu case 2, cấu hình ngưỡng demo case 5 và kiểm tra hiển thị trực quan trong Excel trước khi trình diễn.
- **Quyết định:** Đạt — GD1-03 hoàn thành `[x]`.

### 09/07/2026 — GD1-04 — Tạo sơ đồ kiến trúc kỹ thuật TaxGPT

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tạo và review file kiến trúc kỹ thuật TaxGPT cho hồ sơ Vòng 1. Nội dung gồm mục tiêu kiến trúc, sơ đồ Mermaid, mô tả thành phần, luồng xử lý dữ liệu, vai trò rule engine/RAG/AI/human review, khả năng mở rộng, rủi ro kỹ thuật và biện pháp kiểm soát.
- **Kết quả/Output:** Tạo file `docs/proposal/GD1-04_technical_architecture.md`. File đủ 8 mục, có sơ đồ Mermaid, không nêu ngưỡng tiền cụ thể cho case 5, không cam kết tuân thủ tuyệt đối.
- **Vấn đề phát sinh:** Cần con người kiểm tra khả năng render Mermaid trong định dạng hồ sơ cuối, tính khả thi parser/OCR, chất lượng kho RAG và phương án bảo vệ dữ liệu thật.
- **Quyết định:** Đạt — GD1-04 hoàn thành `[x]`.

### 09/07/2026 — GD1-05 — Tổng hợp bản mô tả ý tưởng Vòng 1

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tổng hợp các nội dung GD1-01 đến GD1-04 và bản diễn đạt pháp lý an toàn GD1-P1 thành bản master mô tả ý tưởng Vòng 1 cho TaxGPT.
- **Kết quả/Output:** Tạo file `docs/proposal/GD1-05_round1_idea_description.md`. File có đủ 15 mục, khoảng 2.343 từ, không nêu ngưỡng tiền cụ thể cho case 5, không cam kết tuân thủ tuyệt đối và không mô tả TaxGPT như sản phẩm đã hoàn thiện.
- **Vấn đề phát sinh:** Bản master có thể quá dài để dán nguyên văn vào Dashboard; cần kiểm tra giới hạn ký tự/cấu trúc trường trên Dashboard và có thể tạo bản rút gọn sau.
- **Quyết định:** Đạt — GD1-05 hoàn thành `[x]`.

### 09/07/2026 — GD1-06 — Phản biện thử hồ sơ Vòng 1

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tạo báo cáo phản biện thử bản mô tả ý tưởng TaxGPT theo góc nhìn giám khảo Vòng 1. Báo cáo đánh giá mức độ phù hợp chủ đề, vấn đề thực tế, tính mới, tính khả thi, rủi ro pháp lý, rủi ro AI, dữ liệu/demo và khả năng thuyết trình.
- **Kết quả/Output:** Tạo file `docs/proposal/GD1-06_round1_critique.md`. Điểm tổng quan 7,4/10; có 15 câu hỏi giám khảo khó, 10 khuyến nghị chỉnh sửa và bản pitch 60 giây.
- **Vấn đề phát sinh:** Cần chỉnh GD1-05 ở nhiệm vụ tiếp theo, tập trung vào bằng chứng nhu cầu người dùng, điểm khác biệt, phạm vi demo và tiêu chí kiểm thử.
- **Quyết định:** Đạt — GD1-06 hoàn thành `[x]`.

### 09/07/2026 — GD1-07 — Chỉnh bản mô tả ý tưởng theo phản biện

- **AI/công cụ dùng:** ChatGPT Plus trong VSCode + điều phối bởi ChatGPT.
- **Người thực hiện:** Đội trưởng.
- **Việc đã làm:** Tạo và review bản v2 mô tả ý tưởng Vòng 1 dựa trên phản biện GD1-06. Nội dung cải thiện định vị khác biệt, phạm vi demo MVP, tiêu chí kiểm thử, bằng chứng nhu cầu định tính và mức độ trung thực về hiện trạng kỹ thuật.
- **Kết quả/Output:** Tạo file `docs/proposal/GD1-07_round1_idea_description_v2.md`. File có đủ 15 mục và phụ lục cải tiến, khoảng 2.814 từ, không nêu ngưỡng tiền cụ thể cho case 5 và không cam kết tuân thủ tuyệt đối. Bản này được dùng làm master hiện hành; GD1-05 giữ làm bản gốc đối chiếu.
- **Vấn đề phát sinh:** Bản v2 quá dài để dán nguyên văn lên Dashboard; cần kiểm tra cấu trúc trường/giới hạn ký tự và tạo bản rút gọn để nộp.
- **Quyết định:** Đạt — GD1-07 hoàn thành `[x]`.

### 17/08/2026 — GD1.5-ENV — Khôi phục môi trường và xác minh runtime cơ bản

- **AI/công cụ dùng:** Python, pip, pytest, Uvicorn, FastAPI và Streamlit; AI hỗ trợ cập nhật tài liệu điều phối theo kết quả xác minh.
- **Người thực hiện:** Đội TaxGPT.
- **Việc đã làm:** Khôi phục môi trường Python trong `.venv` và chạy lại các kiểm tra runtime cơ bản cho test, backend FastAPI, endpoint health và frontend Streamlit.
- **Kết quả/Output:** Python 3.12.10 chạy được; pip 25.0.1 chạy được; `pytest` hoàn tất với 1 passed, 1 warning; backend chạy bằng `uvicorn backend.app.main:app --reload`; endpoint `GET /health` trả HTTP 200 OK; frontend chạy bằng `streamlit run frontend/streamlit_app/app.py` và render được trang “TaxGPT Dashboard” với danh sách tĩnh 5 case MVP.
- **Giới hạn:** Dashboard chưa có upload file, chưa đọc Excel và chưa gọi backend. Chưa có parser, chưa có rule engine, chưa có bảng cảnh báo và chưa có prototype nghiệp vụ end-to-end.
- **Vấn đề phát sinh:** Runtime nền tảng đã ổn định nhưng mới chỉ xác minh khung ứng dụng. Các chức năng nghiệp vụ cốt lõi vẫn phải được triển khai và kiểm thử bằng dữ liệu mẫu.
- **Quyết định:** Đạt cho phạm vi môi trường runtime cơ bản — đủ điều kiện bắt đầu triển khai P1/P2/P3. Không triển khai RAG trước khi rule engine hoạt động và căn cứ pháp lý được con người kiểm chứng.

### 17/08/2026 — GD1.5-CASE1 — Hoàn thành backend slice Case 1

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, pandas, openpyxl, FastAPI, Uvicorn và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Tạo `backend/app/parsers/excel_parser.py`, tạo `backend/app/rules/duplicate_invoice.py`, sửa `backend/app/main.py` để thêm endpoint `GET /demo/case-1-duplicates`, và tạo `backend/tests/test_case_1_duplicates.py`. Chỉ triển khai lát cắt Case 1, không triển khai RAG hoặc AI explanation.
- **Kết quả/Output:** Parser đọc sheet `invoices`, nhận diện header ở dòng Excel 4 và đọc đúng 12 hóa đơn từ `sample_invoices_mvp.xlsx`. Rule Case 1 phát hiện 1 nhóm hóa đơn có khả năng trùng gồm `INV-DEMO-003` và `INV-DEMO-004`. API `/demo/case-1-duplicates` trả HTTP 200 với `total_invoices = 12` và `total_alerts = 1`. Toàn bộ test đạt `7 passed, 1 warning`; warning TestClient không làm test thất bại.
- **Giới hạn:** Chưa có upload file, chưa kết nối frontend Streamlit, chưa triển khai Case 2–5, chưa có RAG hoặc AI explanation. Kết quả hiện tại là backend slice Case 1, chưa phải prototype end-to-end.
- **Vấn đề phát sinh:** Rule duplicate hiện dùng khóa kỹ thuật tối thiểu theo dữ liệu mẫu; các ngoại lệ như hóa đơn điều chỉnh/thay thế cần được xử lý ở bước mở rộng sau.
- **Quyết định:** Đạt cho phạm vi backend slice Case 1. Bước tiếp theo là triển khai Case 2 hoặc kết nối Dashboard tối thiểu; tiếp tục giữ RAG sau rule engine và kiểm chứng pháp lý.

### 17/08/2026 — GD1.5-CASE2 — Hoàn thành backend slice Case 2

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, pandas, FastAPI, Uvicorn và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Tạo rule Case 2 tại `backend/app/rules/buyer_info_mismatch.py`, thêm endpoint `GET /demo/case-2-buyer-info` vào backend và tạo test tại `backend/tests/test_case_2_buyer_info.py`.
- **Kết quả/Output:** Backend slice Case 2 phát hiện 2 cảnh báo thông tin người mua cần rà soát cho `INV-DEMO-005` và `INV-DEMO-006`; endpoint trả HTTP 200 trên dữ liệu mẫu. Thay đổi đã được lưu tại commit `934d3e3` (`Implement backend buyer info mismatch case`).
- **Giới hạn:** Rule hiện phục vụ dữ liệu demo có nhãn rõ ràng; chưa có upload file, chưa kết nối frontend, chưa có API scan-all, chưa triển khai Case 4–5, RAG hoặc AI explanation. Đây chưa phải prototype end-to-end.
- **Vấn đề phát sinh:** Cần cấu hình hồ sơ doanh nghiệp tham chiếu đã được xác nhận trước khi mở rộng logic so khớp MST/tên cho dữ liệu thực.
- **Quyết định:** Đạt cho phạm vi backend slice Case 2.

### 17/08/2026 — GD1.5-CASE3 — Hoàn thành backend slice Case 3

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, pandas, FastAPI, Uvicorn và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Tạo rule Case 3 tại `backend/app/rules/vat_mismatch.py`, thêm endpoint `GET /demo/case-3-vat-mismatch` vào backend và tạo test tại `backend/tests/test_case_3_vat_mismatch.py`.
- **Kết quả/Output:** Backend slice Case 3 phát hiện 2 cảnh báo phép tính VAT cần rà soát cho `INV-DEMO-007` và `INV-DEMO-008`; endpoint trả HTTP 200 trên dữ liệu mẫu. Toàn bộ suite đạt `16 passed, 1 warning`; warning TestClient không làm test thất bại. Thay đổi đã được lưu tại commit `7570404` (`Implement backend VAT mismatch case`).
- **Giới hạn:** Chưa có upload file, chưa kết nối frontend, chưa có API scan-all, chưa triển khai Case 4–5, RAG hoặc AI explanation. Đây chưa phải prototype end-to-end.
- **Vấn đề phát sinh:** Tolerance hiện là cấu hình kỹ thuật; quy tắc làm tròn cần được chốt trước khi dùng với dữ liệu thực.
- **Quyết định:** Đạt cho phạm vi backend slice Case 3. Ưu tiên tiếp theo là Case 4, sau đó Case 5 và API tổng hợp scan-all; RAG tiếp tục để sau rule engine và kiểm chứng pháp lý.

### 17/08/2026 — GD1.5-CASE5 — Hoàn thành backend slice Case 5

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, pandas, openpyxl, FastAPI và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Tạo `backend/app/parsers/payment_parser.py`, tạo `backend/app/rules/missing_bank_payment.py`, tạo `backend/tests/test_case_5_missing_bank_payment.py` và sửa `backend/app/main.py` để thêm endpoint `GET /demo/case-5-missing-bank-payment`.
- **Kết quả/Output:** Parser đọc file thanh toán có sheet `payments`, header tại dòng Excel 4 và 6 giao dịch. Rule Case 5 phát hiện 2 cảnh báo cần rà soát cho `INV-DEMO-011` và `INV-DEMO-012`. API trả HTTP 200. Toàn bộ suite `pytest` đạt `32 passed, 1 warning`.
- **Giới hạn:** Rule chỉ cảnh báo chưa tìm thấy chứng từ thanh toán không dùng tiền mặt phù hợp trong dữ liệu đang đối chiếu; không kết luận gian lận, vi phạm, hóa đơn vô hiệu, không được khấu trừ, bị xử phạt hoặc bị loại chi phí. Chưa có upload file thật, API tổng hợp scan-all, kết nối frontend, RAG hoặc AI explanation; đây chưa phải prototype end-to-end.
- **Vấn đề phát sinh:** Báo cáo cuối phiên chưa xác nhận commit/push thay đổi Case 5. Đầu phiên sau phải chạy `git status` và commit/push nếu còn `modified` hoặc `untracked`.
- **Quyết định:** Đạt cho phạm vi code/test/API của backend slice Case 5; trạng thái lưu trên Git cần được xác nhận ở đầu phiên sau.

### 17/08/2026 — GD1.5-SUMMARY — Tổng kết phiên backend MVP

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, FastAPI và pytest; AI hỗ trợ tổng hợp trạng thái dự án.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Hoàn thiện và rà soát tiến độ các lát cắt backend của 5 case MVP theo chuỗi parser/rule/API/test. Đây là phiên có tiến độ kỹ thuật tốt nhất từ đầu dự án.
- **Kết quả/Output:** 5/5 case backend đã có code/test/API; toàn bộ suite đạt `32 passed, 1 warning`. Ngôn ngữ pháp lý an toàn được giữ: các rule chỉ nêu “có dấu hiệu”, “cần rà soát”, không đưa ra kết luận pháp lý bất lợi.
- **Giới hạn:** Dự án chưa phải prototype end-to-end vì frontend chưa kết nối backend, chưa có upload file thật, chưa có API tổng hợp scan-all, chưa có RAG và chưa có AI explanation.
- **Vấn đề phát sinh:** Kiểm chứng nguồn, hiệu lực và điều/khoản pháp lý vẫn là rủi ro lớn nhất. RAG tiếp tục hoãn; không ingest tài liệu pháp lý chưa kiểm chứng.
- **Quyết định:** Đạt cho phạm vi backend MVP. Ưu tiên tiếp theo là xác nhận commit/push Case 5, hoàn thành scan-all và kết nối dashboard Streamlit; chỉ triển khai RAG sau khi pháp lý được kiểm chứng.

### 18/08/2026 — GD1.5-SCANALL — Hoàn thành API tổng hợp scan-all

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, FastAPI, pandas, httpx và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Thêm endpoint tổng hợp `GET /demo/scan-all` để đọc hai file Excel demo, chạy đủ 5 rule MVP và trả một response thống nhất gồm số liệu tổng quan, `case_summary` và danh sách cảnh báo giữ nguyên evidence.
- **Kết quả/Output:** Endpoint trả `total_invoices = 12`, `total_payments = 6`, `total_alerts = 9`. `case_summary` có đủ 5 case với số cảnh báo lần lượt `1, 2, 2, 2, 2`. Toàn bộ suite đạt `33 passed, 1 warning`. Thay đổi được lưu tại commit `667bf24` (`Implement backend scan-all demo endpoint`).
- **Giới hạn:** API vẫn đọc file demo cố định; chưa nhận file upload thật, chưa có RAG pháp lý hoặc AI explanation và chưa xử lý ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Evidence của các case có schema khác nhau và được giữ nguyên để tránh mất dữ liệu; phần frontend cần định dạng lại nếu muốn trình bày thân thiện hơn.
- **Quyết định:** Đạt cho phạm vi backend scan-all demo.

### 18/08/2026 — GD1.5-FRONTEND-DEMO — Kết nối Streamlit với scan-all

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Streamlit, pandas và httpx.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Sửa `frontend/streamlit_app/app.py` để Dashboard gọi backend `/demo/scan-all` khi người dùng bấm nút “Chạy rà soát dữ liệu demo”.
- **Kết quả/Output:** Dashboard hiển thị 3 metric tổng quan gồm 12 hóa đơn, 6 giao dịch thanh toán và 9 cảnh báo; có bảng tổng hợp đủ 5 case và bảng chi tiết 9 cảnh báo. Dashboard có disclaimer: TaxGPT chỉ hỗ trợ rà soát rủi ro và không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế. Khi backend chưa chạy, giao diện hiển thị lỗi thân thiện: “Backend chưa chạy. Vui lòng chạy uvicorn backend.app.main:app --reload”. Thay đổi được lưu tại commit `a13dfd1` (`Connect Streamlit dashboard to scan-all endpoint`). Git working tree sạch sau commit.
- **Giới hạn:** Chưa có upload file thật, RAG pháp lý hoặc AI explanation; evidence còn hiển thị dạng JSON thô và chưa xử lý ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Giao diện hiện ưu tiên rõ ràng và dễ demo; chưa có lọc theo case, màu severity hoặc định dạng evidence thân thiện.
- **Quyết định:** **Đạt prototype demo local không RAG** với phạm vi `Excel demo cố định → backend scan-all → Streamlit dashboard hiển thị bảng cảnh báo`. Đây chưa phải sản phẩm hoàn chỉnh.

### 18/08/2026 — GD1.5-README — Cập nhật README hướng dẫn chạy demo local

- **AI/công cụ dùng:** AI hỗ trợ kỹ thuật tài liệu trong VSCode/Codex và Markdown.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật tài liệu.
- **Việc đã làm:** Cập nhật `README.md` để mô tả prototype demo local không RAG, 5 case MVP, trạng thái hiện tại, cách cài môi trường Windows PowerShell, chạy test, khởi động backend/frontend bằng hai terminal và thao tác demo.
- **Kết quả/Output:** README ghi rõ kết quả demo kỳ vọng `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`, danh sách API, hai file dữ liệu giả lập, giới hạn hiện tại và nguyên tắc an toàn pháp lý. Thay đổi được lưu tại commit `21976fc` (`Update README with local demo instructions`). Git working tree sạch sau commit.
- **Giới hạn:** Hướng dẫn hiện phục vụ prototype local dùng file demo cố định; chưa có upload file thật, RAG pháp lý, AI explanation hoặc xử lý ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Không có. README hiện đủ để người khác clone repo, cài môi trường và chạy lại kịch bản demo local theo hai terminal.
- **Quyết định:** Đạt cho phạm vi tài liệu hướng dẫn demo local. Prototype demo local không RAG hiện đã có thể trình diễn, nhưng chưa phải sản phẩm hoàn chỉnh.

### 21/08/2026 — GD1.5-P-LEGAL-DRAFT — Tạo legal draft mapping cho 5 case MVP

- **AI/công cụ dùng:** VSCode AI theo prompt điều phối của ChatGPT Plus; chưa có Khánh/Gemini Pro rà soát độc lập.
- **Người thực hiện:** Đội trưởng điều phối việc tạo bản nháp bằng AI; chưa có người có chuyên môn thực hiện rà soát pháp lý cuối cùng.
- **Việc đã làm:** Tạo legal draft mapping cho 5 case MVP, tổng hợp nguồn dự kiến, điều/khoản cần đối chiếu và mức độ tin cậy sơ bộ để làm đầu vào cho bước rà soát độc lập.
- **Kết quả/Output:** File legal draft được tạo tại `van-ban-luat/processed/GD1_5_P_LEGAL_DRAFT_mapping_5_cases.md`. Thay đổi được lưu tại commit `ee099db` (`Add legal draft mapping for MVP cases`).
- **Giới hạn:** Đây là bản nháp do AI tạo, chưa phải nội dung đã kiểm chứng pháp lý. Chưa có Khánh/Gemini Pro hoặc người có chuyên môn rà soát độc lập. Nhãn High/Medium/Low là đánh giá sơ bộ của AI, chưa phải xác nhận pháp lý cuối cùng.
- **Vấn đề phát sinh:** Cần kiểm tra độc lập nguồn tạo, luật hiện hành, hiệu lực, điều/khoản và ưu tiên các case có nhãn Low/Medium trước khi dùng nội dung cho RAG hoặc tuyên bố pháp lý.
- **Quyết định:** RAG vẫn **LOCKED cho cả 5 case, kể cả case có nhãn High confidence**. Không ghi nhận Khánh đã hoàn thành GD1.5-P1 và chưa xác nhận pháp lý hoàn tất.

### 21/08/2026 — GD2-04 — Upload file Excel thật cho hóa đơn và payment

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, FastAPI, Streamlit, httpx, pytest và `python-multipart`.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Sửa `backend/app/main.py`, `frontend/streamlit_app/app.py`, `requirements.txt` và thêm `backend/tests/test_scan_uploaded.py`. Backend có endpoint mới `POST /demo/scan-uploaded`, nhận `invoice_file` và `payment_file`; Streamlit có mục “Rà soát file Excel tải lên” để chọn hai file `.xlsx`. Endpoint dùng file tạm, cleanup sau xử lý và trả lỗi HTTP 400 thân thiện khi thiếu file, sai định dạng hoặc workbook/schema không hợp lệ.
- **Kết quả/Output:** Response giữ cấu trúc gần giống `/demo/scan-all`, gồm `total_invoices`, `total_payments`, `total_alerts`, `case_summary`, `alerts`, `source_invoice_file`, `source_payment_file` và `uploaded_files`. Test thủ công với `data-mau/excel/sample_invoices_mvp.xlsx` và `data-mau/bank_statements/sample_bank_payments_mvp.xlsx` cho kết quả `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`. Toàn bộ suite đạt `37 passed, 1 warning`. Thay đổi được lưu tại commit `f84cc1f` (`Implement uploaded Excel scan workflow`); Git working tree sạch sau commit.
- **Giới hạn:** Đây là upload mức prototype `.xlsx` theo sheet/header/schema hiện tại, chưa phải xử lý dữ liệu mọi định dạng. Chưa tối ưu file lớn; chưa hỗ trợ XML/PDF/OCR, RAG, AI explanation hoặc ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** FastAPI upload cần `python-multipart`; dependency đã được bổ sung vào `requirements.txt`. Warning pytest hiện tại là cảnh báo deprecation của TestClient và không làm test thất bại.
- **Quyết định:** Đạt GD2-04 ở mức prototype `.xlsx`. Giữ nguyên luồng demo cố định và toàn bộ endpoint cũ. RAG tiếp tục **LOCKED toàn bộ 5 case**; legal draft vẫn chỉ là AI draft, chưa phải kiểm chứng pháp lý cuối cùng.

### 21/08/2026 — GD2-04-UI — Cải thiện Dashboard phân biệt demo và upload

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Streamlit và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Sửa `frontend/streamlit_app/app.py` để phân biệt rõ “Chế độ 1: Dữ liệu demo cố định” và “Chế độ 2: File Excel tải lên”. Phần kết quả xác định và hiển thị nguồn là dữ liệu demo cố định hoặc file tải lên; khi response có `uploaded_files`, Dashboard hiển thị tên file hóa đơn và file thanh toán đã tải lên.
- **Kết quả/Output:** Giữ nguyên metric, bảng tổng hợp 5 case, bộ lọc case/severity, cảnh báo và evidence. Upload hai file demo vẫn cho kết quả `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`. Toàn bộ suite trước commit đạt `37 passed, 1 warning`. Thay đổi được lưu tại commit `abd9738` (`Improve dashboard upload result labels`); Git working tree sạch sau commit.
- **Giới hạn:** Đây là cải thiện nhãn và nguồn kết quả ở mức demo, không phải redesign lớn hoặc sản phẩm hoàn chỉnh. Upload vẫn chỉ hỗ trợ `.xlsx` theo sheet/header/schema hiện tại; chưa hỗ trợ XML/PDF/OCR, file lớn, RAG, AI explanation hoặc ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Không có lỗi hồi quy được ghi nhận; warning pytest hiện tại không làm test thất bại.
- **Quyết định:** Đạt GD2-04-UI ở mức demo. RAG tiếp tục **LOCKED toàn bộ 5 case**; legal draft vẫn chỉ là AI draft, chưa phải kiểm chứng pháp lý cuối cùng.

### 21/08/2026 — GD2-04a — Củng cố schema validation cho upload Excel

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, pandas, openpyxl, FastAPI và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Sửa `backend/app/parsers/excel_parser.py`, `backend/app/parsers/payment_parser.py` và `backend/tests/test_scan_uploaded.py`. Validation mới phân biệt workbook hỏng, thiếu sheet `invoices`, thiếu sheet `payments`, thiếu một cột hoặc nhiều cột bắt buộc; thông báo lỗi tiếng Việt rõ hơn và response không lộ traceback hoặc đường dẫn file tạm.
- **Kết quả/Output:** Bổ sung test upload cho workbook hỏng, thiếu từng sheet và thiếu cột bắt buộc. Upload hai file demo vẫn trả `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`. Toàn bộ suite đạt `41 passed, 1 warning`. Thay đổi được lưu tại commit `3bd1471` (`Improve uploaded Excel schema validation`); Git working tree sạch sau commit.
- **Giới hạn:** GD2-04a chỉ củng cố validation cho `.xlsx` theo sheet/header/schema hiện tại, không mở rộng định dạng. Chưa kiểm tra sâu kiểu dữ liệu từng ô, chưa giới hạn dung lượng file và chưa hỗ trợ XML/PDF/OCR hoặc ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Warning pytest hiện tại là cảnh báo deprecation của TestClient và không làm test thất bại. Không đổi rule engine, frontend hoặc legal draft.
- **Quyết định:** Đạt GD2-04a. RAG tiếp tục **LOCKED toàn bộ 5 case**; chưa triển khai AI explanation và chưa xác nhận pháp lý hoàn tất.

### 21/08/2026 — GD2-04b — Tạo template Excel cho upload

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, openpyxl, Streamlit và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Tạo `data-mau/excel/template_invoices_mvp.xlsx` với sheet `invoices` và `data-mau/bank_statements/template_bank_payments_mvp.xlsx` với sheet `payments`, đúng header/schema bắt buộc của parser hiện tại. Sửa `frontend/streamlit_app/app.py` để thêm nút tải template hóa đơn và template thanh toán, đồng thời hiển thị cảnh báo thân thiện nếu file template chưa tồn tại. Cập nhật `README.md` với hướng dẫn dùng template và bổ sung test nhẹ trong `backend/tests/test_scan_uploaded.py` để xác nhận parser đọc được hai file.
- **Kết quả/Output:** Hai template phục vụ prototype `.xlsx` đã được thêm; Dashboard cho phép tải trực tiếp từng template; README đã có đường dẫn và lưu ý phạm vi demo/prototype. Toàn bộ suite đạt `42 passed, 1 warning`. Thay đổi được lưu tại commit `e45ae30` (`Add Excel upload templates`); Git working tree sạch sau commit.
- **Giới hạn:** Template bám theo sheet/header/schema hiện tại và không phải chuẩn dữ liệu pháp lý chính thức. Upload vẫn chỉ hỗ trợ `.xlsx`; chưa kiểm tra sâu kiểu dữ liệu từng ô, chưa giới hạn dung lượng file, chưa hỗ trợ XML/PDF/OCR, AI explanation hoặc ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Không có lỗi hồi quy được ghi nhận; warning pytest hiện tại không làm test thất bại. Legal draft vẫn chưa được rà soát độc lập.
- **Quyết định:** Đạt GD2-04b. RAG tiếp tục **LOCKED toàn bộ 5 case** và chỉ được xem xét sau khi legal review sạch.

### 21/08/2026 — GD2-04c — Upload edge cases and data quality checks

- **AI/công cụ dùng:** AI kỹ thuật triển khai trong VSCode/Codex, Python, pandas, openpyxl, FastAPI và pytest.
- **Người thực hiện:** Đội TaxGPT phối hợp với AI kỹ thuật.
- **Việc đã làm:** Sửa `backend/app/parsers/excel_parser.py`, `backend/app/parsers/payment_parser.py` và `backend/tests/test_scan_uploaded.py`. Parser mới từ chối sheet đúng header nhưng không có dòng dữ liệu, bỏ dòng trống hoàn toàn, phát hiện giá trị bắt buộc bị trống, kiểm tra ngày cơ bản tại `invoice_date`/`payment_date` và kiểm tra số tiền cơ bản tại `net_amount`/`vat_amount`/`total_amount`/`amount`.
- **Kết quả/Output:** Message HTTP 400 vẫn thân thiện, không lộ traceback hoặc đường dẫn file tạm. Không đổi API response field, rule engine, frontend hoặc legal draft. Luồng demo vẫn đạt `12 hóa đơn / 6 giao dịch thanh toán / 9 cảnh báo`; hai template vẫn đọc được. Toàn bộ suite đạt `50 passed, 1 warning`. Thay đổi được lưu tại commit `eae11a3` (`Add upload data quality checks`); Git working tree sạch sau commit.
- **Giới hạn:** Đây là kiểm tra data quality cơ bản cho upload `.xlsx`, chưa phải validation dữ liệu đầy đủ. Message chưa chỉ rõ số dòng lỗi; chưa giới hạn dung lượng file; chưa hỗ trợ XML/PDF/OCR, AI explanation hoặc ngoại lệ nghiệp vụ nâng cao.
- **Vấn đề phát sinh:** Không có lỗi hồi quy được ghi nhận; warning pytest hiện tại không làm test thất bại. Legal draft vẫn chưa được rà soát độc lập.
- **Quyết định:** Đạt GD2-04c. RAG tiếp tục **LOCKED toàn bộ 5 case**.

### 26/08/2026 — Quyết định tự đảm nhận toàn bộ nhiệm vụ để tăng tốc

- **AI/công cụ dùng:** ChatGPT/Codex hỗ trợ điều phối và cập nhật tài liệu dự án.
- **Người thực hiện:** Đội trưởng/nhóm TaxGPT hiện tại.
- **Lý do:** Nhóm không muốn tiếp tục mất thời gian chờ đợi; tiến độ rà soát pháp lý của Khánh sau thời gian dài chưa có kết quả thực chất để làm đầu vào cho bước tiếp theo.
- **Quyết định:** Đội trưởng/nhóm hiện tại chủ động làm tiếp toàn bộ phần kỹ thuật, rà soát pháp lý sơ bộ, tài liệu, hồ sơ và chuẩn bị cuộc thi. Khánh, Thế Anh hoặc thành viên khác nếu tham gia lại sẽ review phụ hoặc kiểm tra chéo sau, không còn là blocker của tiến độ chính.
- **Giới hạn:** Phần pháp lý tự rà chỉ là **internal legal review sơ bộ**, không được gọi là independent legal review hoặc kiểm chứng pháp lý độc lập; không ghi nhận pháp lý đã hoàn tất nếu chưa có bằng chứng phù hợp.
- **Ưu tiên trước mắt:** Kiểm tra kết quả Vòng 1 trên Dashboard/email/nhóm Ban tổ chức, sau đó đội trưởng/nhóm hiện tại tự rà Case 3 trên văn bản gốc chính thức trước khi tiếp tục các case khác.
- **Trạng thái kiểm soát:** RAG vẫn **LOCKED toàn bộ 5 case** và chỉ được xem xét sau khi có bảng đối chiếu cùng bằng chứng rà văn bản gốc đủ sạch.
