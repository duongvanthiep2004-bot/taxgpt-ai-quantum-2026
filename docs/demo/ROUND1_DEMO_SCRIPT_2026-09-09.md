# TaxGPT Round 1 Demo Script

Mốc Vòng 1 theo thông tin điều phối: **09/09/2026**. Tài liệu chuẩn bị ngày **11/09/2026**; đội chưa thi, chưa có kết quả theo cập nhật của đội trưởng. Tên file giữ mốc được yêu cầu, không xác nhận buổi thi đã diễn ra.

Bản nháp do Codex hỗ trợ soạn từ README, giao diện và rule hiện tại; đội cần đọc, chỉnh lời và tập trình bày trước khi sử dụng. Các số dưới đây là **kết quả kỳ vọng trên sample**, không phải biên bản chạy QA mới. Legal confidence **Pending**; RAG/AI explanation **LOCKED toàn bộ 5 case**.

## Mục tiêu demo và bối cảnh bài toán

TaxGPT là prototype hỗ trợ rà soát rủi ro thuế/chứng từ cho SMEs. SMEs có nhiều hóa đơn, chứng từ nên dễ bỏ sót lỗi dữ liệu; rà thủ công tốn thời gian và khó nhất quán. TaxGPT giúp gom dữ liệu Excel, chạy rule và hiển thị cảnh báo có dữ liệu hỗ trợ để người dùng kiểm tra lại.

Đây là hệ thống cảnh báo/rà soát nội bộ, không đưa ra kết luận sai phạm pháp lý và không thay thế kế toán, luật sư, chuyên gia thuế hoặc cơ quan thuế. Luồng đang trình diễn dùng rule kỹ thuật; không giới thiệu evidence như giải thích pháp lý do AI sinh ra.

## Chuẩn bị trước khi bấm giờ

- Dùng môi trường đã cài theo [README](../../README.md); mở hai terminal PowerShell tại root repo.
- Terminal 1 chạy backend:

```powershell
.\.venv\Scripts\activate
uvicorn backend.app.main:app --reload
```

- Terminal 2 chạy frontend:

```powershell
.\.venv\Scripts\activate
streamlit run frontend/streamlit_app/app.py
```

- Kiểm tra `http://127.0.0.1:8000/health`, mở `http://localhost:8501`.
- Chuẩn bị đúng hai file sample có sẵn, không sửa nội dung và không nhầm với template:
  - Hóa đơn: `data-mau/excel/sample_invoices_mvp.xlsx`.
  - Thanh toán: `data-mau/bank_statements/sample_bank_payments_mvp.xlsx`.
- Dữ liệu sample là giả lập. Thực hiện [QA checklist](ROUND1_QA_CHECKLIST.md) trước buổi diễn; chuẩn bị screenshot từ lần chạy thật nếu cần dự phòng, ghi rõ thời điểm và nguồn. Phiên soạn tài liệu này chưa tạo screenshot.

## Luồng demo đề xuất — 6 phút 30 giây

| Bước | Thời gian | Thao tác | Lời trình bày gợi ý |
|---|---|---|---|
| 1 | 0:00–0:35 | Mở dashboard Streamlit tại `http://localhost:8501`. | “SMEs cần rà nhiều hóa đơn và chứng từ, dễ bỏ sót lỗi khi đối chiếu thủ công. TaxGPT thử nghiệm luồng Excel → rule → cảnh báo dễ kiểm tra.” |
| 2 | 0:35–1:00 | Chỉ vào disclaimer dưới tiêu đề. | “Hệ thống đưa ra cảnh báo rà soát, không kết luận sai phạm. TaxGPT không thay thế kế toán, luật sư, chuyên gia thuế hoặc cơ quan thuế.” |
| 3 | 1:00–1:25 | Ở “Chế độ 1: Dữ liệu demo cố định”, bấm “Chạy rà soát dữ liệu demo”; chờ kết quả. | “Đây là hai file sample giả lập có sẵn. Nguồn kết quả được ghi rõ là dữ liệu demo cố định.” |
| 4 | 1:25–1:55 | Chỉ lần lượt ba metric. | “Có 12 hóa đơn, 6 giao dịch thanh toán và 9 cảnh báo. Số cảnh báo không phải số doanh nghiệp hay số hóa đơn vi phạm; một hóa đơn có thể liên quan nhiều cảnh báo.” |
| 5 | 1:55–2:45 | Giới thiệu bảng “Tổng hợp theo 5 case”, dùng bảng bên dưới. | “Năm nhóm kiểm tra có số cảnh báo lần lượt 1, 2, 2, 2, 2. Đây là những điểm cần đối chiếu lại dữ liệu và chứng từ.” |
| 6 | 2:45–3:20 | Chọn lần lượt case ở “Lọc theo case_id”; chọn một severity hiện có. Trở về Case 3 và severity “Tất cả”. | “Bộ lọc giúp tập trung vào từng nhóm và mức cảnh báo. Severity là mức phân loại của rule, không phải kết luận pháp lý. Bộ lọc đổi bảng chi tiết và evidence; ba metric và bảng tổng hợp vẫn là toàn bộ kết quả.” |
| 7 | 3:20–4:10 | Chọn `CASE_3_VAT_MISMATCH`; mở “Xem evidence chi tiết”, rồi mở mục hóa đơn `INV-DEMO-007` hoặc `INV-DEMO-008`. | “Evidence cho thấy giá trị tính thuế, thuế suất đầu vào, VAT ghi nhận, VAT tính lại, độ lệch và tolerance. Chúng tôi kiểm tra phép tính cơ bản, chưa xác nhận thuế suất đầu vào đúng về pháp lý.” |
| 8 | 4:10–5:00 | Ở “Chế độ 2: File Excel tải lên”, chọn đúng hai sample vào hai ô; bấm “Chạy rà soát file tải lên”. | “Bây giờ dùng cùng dữ liệu qua luồng upload. Kết quả phải ghi nguồn ‘File tải lên’ và tên hai file.” |
| 9 | 5:00–5:30 | Đặt hai bộ lọc về “Tất cả”; chỉ lại metric và bảng tổng hợp. | “Kết quả kỳ vọng vẫn là 12 hóa đơn, 6 thanh toán, 9 cảnh báo; phân bố theo case vẫn là 1/2/2/2/2. Hai đường nhập liệu được đối chiếu trên cùng sample.” |
| 10 | 5:30–6:30 | Nêu giới hạn và hướng phát triển, kết thúc demo. | “MVP mới hỗ trợ Excel theo schema hiện tại. Legal confidence vẫn Pending, RAG/AI explanation đang LOCKED. Bước tiếp theo là kiểm tra chéo, QA và củng cố dữ liệu; sau sơ loại tiếp tục rà pháp lý sâu. Chỉ xem xét mở RAG khi nguồn và phạm vi pháp lý được rà đủ sạch, có kiểm tra chéo.” |

Nếu thao tác chậm, rút ngắn lời giới thiệu từng case để giữ tổng 5–7 phút; giữ phần disclaimer, evidence và giới hạn MVP.

## 5 case MVP và kết quả kỳ vọng

| Case | Phạm vi trình bày | Số cảnh báo sample |
|---|---|---|
| Case 1 | Hóa đơn trùng; 1 cảnh báo nhóm có thể chứa nhiều hóa đơn. | 1 |
| Case 2 | Thông tin người mua không khớp. | 2 |
| Case 3 | VAT không khớp phép tính cơ bản. | 2 |
| Case 4 | Hóa đơn ngoài kỳ rà soát; không tự kết luận kê khai sai. | 2 |
| Case 5 | Hóa đơn giá trị lớn chưa tìm thấy thanh toán ngân hàng trong dữ liệu cung cấp; không suy ra doanh nghiệp chưa thanh toán hoặc không được khấu trừ. | 2 |

Áp dụng cho cả demo cố định và upload đúng hai sample:

| Trường API / metric | Kỳ vọng |
|---|---|
| `total_invoices` | 12 |
| `total_payments` | 6 |
| `total_alerts` | 9 |

Case 3: đối chiếu `taxable_amount`, `vat_rate`, `vat_amount`, `recalculated_vat`, `difference`, `tolerance` trong evidence. Rule chuẩn hóa thuế suất dạng phần trăm khi cần rồi tính VAT; tolerance hiện là `1.0`, chỉ là tham số kỹ thuật, không phải ngưỡng pháp lý.

## Câu nói an toàn khi trình bày

- “Hệ thống đưa ra cảnh báo rà soát, không kết luận sai phạm.”
- “Kết quả phụ thuộc vào dữ liệu được cung cấp.”
- “Các căn cứ pháp lý đang được rà soát, legal confidence hiện vẫn Pending.”
- “RAG/AI explanation đang khóa để tránh sinh giải thích pháp lý chưa kiểm chứng.”

## Không được nói

- Không nói hệ thống kết luận doanh nghiệp vi phạm.
- Không nói pháp lý đã hoàn tất hoặc đã xác minh pháp lý đầy đủ.
- Không nói RAG đã sẵn sàng.
- Không nói thay thế chuyên gia thuế.
- Không biến số cảnh báo, severity hoặc evidence thành bằng chứng khẳng định sai phạm.

## Giới hạn MVP và hướng phát triển

- Chỉ hỗ trợ `.xlsx` theo sheet/header/schema hiện tại; chưa hỗ trợ XML/PDF/OCR hoặc tối ưu file lớn.
- Case 3 chưa kiểm tra `total_amount = taxable_amount + vat_amount`, chưa xử lý đầy đủ làm tròn, nhiều dòng, chiết khấu hoặc xác minh thuế suất pháp lý.
- Chưa xử lý đầy đủ hóa đơn điều chỉnh/thay thế, thanh toán từng phần/gộp và bù trừ công nợ.
- Evidence phục vụ đối chiếu kỹ thuật. Legal confidence **Pending**; RAG/AI explanation **LOCKED**.
- Trước mắt: Thế Anh chạy demo/cross-check, đội tập script và chạy QA. Sau sơ loại mới tiếp tục rà sâu NĐ 359/144 và các case pháp lý còn lại; không hứa thời điểm mở RAG khi chưa đạt điều kiện kiểm chứng.

## Phương án dự phòng khi demo lỗi

| Tình huống | Xử lý nhanh | Cách tiếp tục trình bày |
|---|---|---|
| Backend chưa chạy | Mở Terminal 1, chạy lệnh backend ở trên, kiểm tra `/health` rồi bấm rà soát lại. | Nếu chưa khôi phục, dùng screenshot đã chuẩn bị từ lần chạy thật, nói rõ đây là kết quả lưu trước. |
| Frontend chưa kết nối | Kiểm tra `/health`, địa chỉ backend `127.0.0.1:8000`, terminal Streamlit và `localhost:8501`; tải lại trang hoặc khởi động lại frontend. | Không sửa code trực tiếp giữa phần trình bày; chuyển sang screenshot nếu không khôi phục nhanh. |
| Upload file sai định dạng/thiếu sheet | Chọn lại đúng hai sample `.xlsx`, đúng ô hóa đơn/thanh toán; bấm chạy lại. | Giải thích thông báo kiểm tra đầu vào; không gọi dữ liệu sai schema là dữ liệu đã xử lý thành công. |
| Upload sample vẫn lỗi | Ghi lỗi, trở lại nút “Chạy rà soát dữ liệu demo” và đặt bộ lọc về “Tất cả”. | Dùng demo cố định nếu backend còn hoạt động; nếu cả hai luồng lỗi, dùng screenshot đã chuẩn bị và công khai giới hạn buổi demo. |
| GitHub/mạng lỗi | Dùng repo, môi trường và sample đã chuẩn bị local; không phụ thuộc clone/cài gói ngay tại buổi thi. | Luồng demo local đã cài sẵn không cần truy cập GitHub; dùng screenshot dự phòng nếu môi trường local cũng chưa sẵn sàng. |

Không trình bày screenshot như một lần chạy trực tiếp thành công. Nếu kết quả thực tế lệch kỳ vọng, ghi nhận lỗi và chuyển phương án dự phòng, không sửa số liệu để khớp script.
