
# Hướng dẫn sử dụng folder project TaxGPT

## 1. Giới thiệu chung

Đây là folder dự án **TaxGPT** — một trợ lý AI hỗ trợ doanh nghiệp nhỏ, hộ kinh doanh và người làm kế toán rà soát sớm một số rủi ro thuế từ hóa đơn, chứng từ và dữ liệu thanh toán.

Dự án phục vụ cuộc thi **AI-Quantum Challenge 2026** của Học viện Tài chính, nhóm chủ đề:

```text
AI cho Quản trị Rủi ro và Tuân thủ
```

TaxGPT không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế. Hệ thống chỉ có vai trò hỗ trợ cảnh báo rủi ro, giải thích lý do và gợi ý người dùng kiểm tra lại.

---

## 2. Trạng thái hiện tại của dự án

Dự án hiện đã hoàn thành các phần nền tảng quan trọng:

```text
- Đã đăng ký đội thi thành công.
- Mã đội: AQ2026-183.
- Đã chốt 5 case MVP.
- Đã có cấu trúc repo.
- Đã có backend FastAPI tối thiểu.
- Đã có frontend Streamlit tối thiểu.
- Đã có dữ liệu mẫu giả lập.
- Đã có bản mô tả ý tưởng Vòng 1.
- Đã có bản DOCX để nộp Dashboard.
```

Các file điều phối tiến độ đã được cập nhật liên tục trong quá trình làm việc.

---

## 3. Cấu trúc thư mục chính

Folder project có cấu trúc tổng quan như sau:

```text
taxGPT/
├── backend/
├── frontend/
├── data-mau/
├── van-ban-luat/
├── docs/
├── scripts/
├── requirements.txt
├── .env.example
├── pytest.ini
├── README.md
├── 00_AGENTS.md
├── 01_PROJECT_GOALS.md
├── 02_SESSION_LOG.md
├── 03_NEXT_ACTIONS.md
├── AI_usage_log.md
└── TaxGPT_Ke_hoach_thuc_hien.md
```

---

## 4. Ý nghĩa từng thư mục

## 4.1. `backend/`

Thư mục chứa phần backend của TaxGPT.

Hiện tại đã có backend FastAPI tối thiểu để kiểm tra hệ thống chạy được.

Các file/thư mục quan trọng:

```text
backend/app/main.py
backend/tests/test_health.py
backend/storage/
backend/storage/chroma/
```

Ý nghĩa:

```text
backend/app/main.py
```

Chứa ứng dụng FastAPI tối thiểu. Hiện có endpoint kiểm tra:

```text
GET /health
```

Kết quả mong đợi:

```json
{"status":"ok","service":"TaxGPT backend"}
```

```text
backend/tests/test_health.py
```

Chứa test kiểm tra endpoint `/health`.

```text
backend/storage/chroma/
```

Thư mục dự kiến dùng để lưu dữ liệu vector database ChromaDB cho phần RAG pháp lý sau này.

Hiện tại backend mới ở mức khung cơ bản, chưa có parser thật, rule engine thật hoặc RAG hoàn chỉnh.

---

## 4.2. `frontend/`

Thư mục chứa giao diện demo.

File chính:

```text
frontend/streamlit_app/app.py
```

Đây là app Streamlit tối thiểu, hiện hiển thị:

```text
TaxGPT Dashboard
Upload hóa đơn/chứng từ để kiểm tra rủi ro thuế MVP
5 case rủi ro MVP
```

Giao diện này dùng để chứng minh hướng dashboard ban đầu. Chưa phải sản phẩm hoàn chỉnh.

---

## 4.3. `data-mau/`

Thư mục chứa dữ liệu mẫu giả lập để demo và kiểm thử.

Cấu trúc chính:

```text
data-mau/
├── excel/
└── bank_statements/
```

Các file quan trọng:

```text
data-mau/excel/sample_invoices_mvp.xlsx
data-mau/bank_statements/sample_bank_payments_mvp.xlsx
```

Ý nghĩa:

```text
sample_invoices_mvp.xlsx
```

Chứa 12 hóa đơn giả lập. Dữ liệu này dùng để minh họa 5 case MVP:

```text
1. Hóa đơn trùng.
2. Sai MST hoặc tên người mua.
3. VAT không khớp phép tính.
4. Hóa đơn ngoài kỳ dữ liệu đang rà soát.
5. Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
```

Ngoài ra có 2 hóa đơn bình thường để kiểm tra hệ thống không cảnh báo sai.

```text
sample_bank_payments_mvp.xlsx
```

Chứa 6 giao dịch thanh toán giả lập. File này dùng để đối chiếu với hóa đơn, đặc biệt phục vụ case 5.

Toàn bộ dữ liệu trong thư mục này là dữ liệu giả lập, không dùng hóa đơn thật, không chứa thông tin doanh nghiệp thật.

---

## 4.4. `van-ban-luat/`

Thư mục chứa tài liệu pháp lý và bản diễn đạt pháp lý an toàn.

Cấu trúc thường gồm:

```text
van-ban-luat/
├── raw/
└── processed/
```

Các file quan trọng trong `processed/`:

```text
GD0-04_legal_basis_5_cases_v3_reviewed.md
GD1-P1_safe_legal_wording_for_round1.md
```

Ý nghĩa:

```text
GD0-04_legal_basis_5_cases_v3_reviewed.md
```

Là bản khung pháp lý V3 cho 5 case MVP. Tuy nhiên file này chưa được coi là kiểm chứng pháp lý tuyệt đối.

```text
GD1-P1_safe_legal_wording_for_round1.md
```

Là bản diễn đạt pháp lý an toàn để dùng trong hồ sơ Vòng 1. File này tránh nêu điều/khoản hoặc ngưỡng cụ thể chưa kiểm chứng đầy đủ.

Lưu ý quan trọng:

```text
Không tự ý đưa điều/khoản/ngưỡng pháp lý cụ thể vào hồ sơ hoặc demo nếu chưa đối chiếu văn bản gốc.
```

---

## 4.5. `docs/`

Đây là thư mục tài liệu chính của dự án.

Cấu trúc:

```text
docs/
├── dieuphoi/
├── proposal/
├── demo/
└── submission/
```

### `docs/dieuphoi/`

Chứa bản sao đồng bộ của các file điều phối:

```text
00_AGENTS.md
01_PROJECT_GOALS.md
02_SESSION_LOG.md
03_NEXT_ACTIONS.md
AI_usage_log.md
TaxGPT_Ke_hoach_thuc_hien.md
```

Thư mục này giúp cộng sự đọc nhanh tiến độ và cách làm việc của dự án.

### `docs/proposal/`

Chứa các tài liệu viết hồ sơ Vòng 1.

Các file quan trọng:

```text
GD1-01_problem_statement.md
GD1-02_solution_overview.md
GD1-03_sample_data_plan.md
GD1-04_technical_architecture.md
GD1-05_round1_idea_description.md
GD1-06_round1_critique.md
GD1-07_round1_idea_description_v2.md
GD1-DASH_dashboard_submission_draft.md
```

Ý nghĩa:

```text
GD1-01_problem_statement.md
```

Mô tả vấn đề thực tế mà TaxGPT giải quyết.

```text
GD1-02_solution_overview.md
```

Mô tả giải pháp TaxGPT, luồng xử lý, 5 chức năng MVP và giới hạn hệ thống.

```text
GD1-03_sample_data_plan.md
```

Mô tả dữ liệu mẫu và cách dữ liệu này minh họa 5 case MVP.

```text
GD1-04_technical_architecture.md
```

Mô tả kiến trúc kỹ thuật, gồm frontend, backend, parser, rule engine, RAG, AI explanation và human review.

```text
GD1-05_round1_idea_description.md
```

Bản master đầu tiên của hồ sơ ý tưởng Vòng 1.

```text
GD1-06_round1_critique.md
```

Bản phản biện thử theo góc nhìn giám khảo.

```text
GD1-07_round1_idea_description_v2.md
```

Bản mô tả ý tưởng Vòng 1 đã chỉnh sửa theo phản biện. Đây là **bản master hiện hành** nên ưu tiên đọc file này khi cần hiểu hồ sơ mới nhất.

```text
GD1-DASH_dashboard_submission_draft.md
```

Bản rút gọn nội dung để copy vào các trường trên Dashboard.

### `docs/submission/`

Chứa file dùng để upload lên Dashboard cuộc thi.

File hiện tại:

```text
TaxGPT_Round1_Submission_AQ2026-183.docx
```

Đây là file DOCX hồ sơ Vòng 1, dung lượng nhỏ hơn 30 MB, dùng để nộp trên Dashboard.

---

## 4.6. `scripts/`

Thư mục dự kiến chứa script hỗ trợ xử lý dữ liệu, tạo báo cáo hoặc chạy các tác vụ tự động.

Hiện tại chưa phải thư mục trọng tâm.

---

## 5. Các file điều phối quan trọng

## 5.1. `00_AGENTS.md`

File mô tả vai trò của từng công cụ AI và quy tắc phối hợp.

Nên đọc file này nếu muốn hiểu:

```text
- ChatGPT dùng làm gì.
- Gemini dùng làm gì.
- VSCode AI dùng làm gì.
- Quy tắc không bịa pháp lý.
- Quy tắc ghi log và kiểm soát tiến độ.
```

## 5.2. `01_PROJECT_GOALS.md`

Đây là file quan trọng nhất để xem tiến độ tổng thể.

File này chứa:

```text
- Mục tiêu dự án.
- Deadline cuộc thi.
- Task ID từng giai đoạn.
- Trạng thái từng việc.
- Danh sách thành viên.
- 5 case MVP.
- Rủi ro đang mở.
```

Ký hiệu trạng thái:

```text
[ ]  Chưa làm
[~]  Đang làm / cần theo dõi
[x]  Hoàn thành
[!]  Bị chặn
```

## 5.3. `02_SESSION_LOG.md`

Đây là nhật ký làm việc.

Nguyên tắc:

```text
Chỉ thêm log mới ở cuối file.
Không sửa hoặc xóa log cũ.
```

File này dùng để:

```text
- Theo dõi lịch sử làm việc.
- Ghi lại AI/công cụ đã dùng.
- Ghi lại output từng phiên.
- Làm căn cứ viết mục khai báo AI trong hồ sơ.
```

## 5.4. `03_NEXT_ACTIONS.md`

Đây là file xem nhanh việc cần làm tiếp theo.

File này có thể được ghi đè sau mỗi phiên làm việc, nên không dùng để tra lịch sử. Muốn xem lịch sử thì đọc `02_SESSION_LOG.md`.

## 5.5. `AI_usage_log.md`

File dùng để ghi nhận việc sử dụng AI, phục vụ minh bạch trong hồ sơ dự thi.

---

## 6. Cách chạy thử project

## 6.1. Cài môi trường

Mở terminal tại thư mục gốc project:

```powershell
cd "D:\Học hành\taxGPT"
```

Tạo virtual environment nếu chưa có:

```powershell
python -m venv .venv
```

Kích hoạt venv:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn script, chạy:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Cài dependencies:

```powershell
pip install -r requirements.txt
```

---

## 6.2. Chạy test

```powershell
pytest
```

Kết quả mong đợi:

```text
1 test passed
```

---

## 6.3. Chạy backend

```powershell
uvicorn backend.app.main:app --reload
```

Mở trình duyệt:

```text
http://127.0.0.1:8000/health
```

Kết quả mong đợi:

```json
{"status":"ok","service":"TaxGPT backend"}
```

---

## 6.4. Chạy frontend

Mở terminal thứ hai, kích hoạt venv:

```powershell
.\.venv\Scripts\Activate.ps1
```

Chạy Streamlit:

```powershell
streamlit run frontend/streamlit_app/app.py
```

Trình duyệt sẽ mở giao diện TaxGPT Dashboard.

---

## 7. Cách đọc project nhanh cho người mới

Người mới không cần đọc toàn bộ ngay. Nên đọc theo thứ tự sau:

```text
1. 01_PROJECT_GOALS.md
2. 03_NEXT_ACTIONS.md
3. docs/proposal/GD1-07_round1_idea_description_v2.md
4. docs/proposal/GD1-DASH_dashboard_submission_draft.md
5. docs/proposal/GD1-04_technical_architecture.md
6. docs/proposal/GD1-03_sample_data_plan.md
7. data-mau/excel/sample_invoices_mvp.xlsx
8. data-mau/bank_statements/sample_bank_payments_mvp.xlsx
9. README.md
```

Nếu chỉ muốn hiểu dự án trong 10 phút, đọc:

```text
01_PROJECT_GOALS.md
GD1-07_round1_idea_description_v2.md
GD1-DASH_dashboard_submission_draft.md
```

Nếu muốn chạy thử kỹ thuật, đọc:

```text
README.md
backend/app/main.py
frontend/streamlit_app/app.py
```

Nếu muốn kiểm tra dữ liệu mẫu, đọc:

```text
GD1-03_sample_data_plan.md
sample_invoices_mvp.xlsx
sample_bank_payments_mvp.xlsx
```

---

## 8. Những việc không nên tự ý sửa

Cộng sự khi nhận folder cần lưu ý:

```text
Không sửa/xóa log cũ trong 02_SESSION_LOG.md.
Không tự ý đổi trạng thái task nếu chưa báo đội trưởng.
Không đưa dữ liệu thật vào data-mau/.
Không đưa API key vào repo.
Không sửa .env.example thành file chứa key thật.
Không push .venv/ lên GitHub.
Không nêu ngưỡng tiền case 5 nếu chưa kiểm chứng pháp lý.
Không viết TaxGPT thay thế kế toán/cơ quan thuế.
Không cam kết TaxGPT đảm bảo tuân thủ 100%.
```

---

## 9. Những việc cộng sự có thể hỗ trợ

Cộng sự có thể hỗ trợ các việc sau:

```text
1. Kiểm tra lỗi chính tả và logic trong hồ sơ.
2. Kiểm tra file DOCX trước khi upload.
3. Làm slide trình bày.
4. Kiểm tra dữ liệu mẫu có dễ hiểu không.
5. Bổ sung câu hỏi phản biện của giám khảo.
6. Kiểm chứng pháp lý với văn bản gốc.
7. Làm sạch README trước khi public GitHub.
8. Test backend/frontend trên máy khác.
9. Ghi lại lỗi vào file log hoặc báo lại đội trưởng.
```

---

## 10. Trạng thái hồ sơ nộp Dashboard

Dashboard hiện có các trường:

```text
Loại bài nộp
Tên bài dự thi
Tóm tắt bài dự thi
Phương pháp và công nghệ sử dụng
Ghi chú của đội thi
Link báo cáo
Link slide trình bày
Link GitHub / mã nguồn
Link demo sản phẩm
File bài dự thi
```

Nội dung rút gọn để copy vào Dashboard nằm ở:

```text
docs/proposal/GD1-DASH_dashboard_submission_draft.md
```

File DOCX để upload nằm ở:

```text
docs/submission/TaxGPT_Round1_Submission_AQ2026-183.docx
```

---

## 11. Trạng thái GitHub / Demo / Slide

Tại thời điểm hiện tại:

```text
Link báo cáo: cần upload DOCX/PDF lên Google Drive để lấy link.
Link slide: chưa có hoặc cần tạo thêm.
Link GitHub: cần tạo repo public/private tùy quyết định.
Link demo: chưa có demo online, hiện mới có prototype cục bộ.
```

Không nên dán link local như:

```text
http://127.0.0.1:8501
```

vì giám khảo không mở được trên máy của họ.

---

## 12. Gợi ý nội dung gửi kèm khi gửi folder cho cộng sự

Bạn có thể gửi kèm lời nhắn:

```text
Mình gửi folder project TaxGPT. Đây là dự án dự thi AI-Quantum Challenge 2026, chủ đề AI cho Quản trị Rủi ro và Tuân thủ.

Bạn đọc trước các file:
1. 01_PROJECT_GOALS.md để hiểu tiến độ và task.
2. docs/proposal/GD1-07_round1_idea_description_v2.md để hiểu bản mô tả ý tưởng mới nhất.
3. docs/proposal/GD1-DASH_dashboard_submission_draft.md để xem nội dung chuẩn bị nộp Dashboard.
4. docs/proposal/GD1-03_sample_data_plan.md để hiểu dữ liệu mẫu.
5. README.md nếu muốn chạy thử backend/frontend.

Lưu ý: không sửa/xóa log cũ, không đưa dữ liệu thật vào project, không thêm API key vào repo. Nếu phát hiện lỗi hoặc góp ý, hãy ghi rõ file, mục, dòng và nội dung đề xuất sửa.
```

---

## 13. Tóm tắt ngắn cho cộng sự

TaxGPT hiện là một MVP đang chuẩn bị nộp Vòng 1. Dự án đã có tài liệu hồ sơ, dữ liệu mẫu, backend/frontend tối thiểu và bản DOCX để upload. Phần quan trọng nhất cần cộng sự kiểm tra là: hồ sơ có dễ hiểu không, dữ liệu mẫu có hợp lý không, dashboard draft có phù hợp để nộp không, và các nội dung pháp lý có đủ thận trọng không.
