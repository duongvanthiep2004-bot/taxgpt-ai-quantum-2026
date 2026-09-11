# TaxGPT Round 1 QA Checklist

Ngày soạn: **11/09/2026**. Mốc Vòng 1 theo điều phối: **09/09/2026**; đội chưa thi, chưa có kết quả. Bản checklist do Codex hỗ trợ soạn; Dương Văn Thiệp đã chạy thủ công toàn bộ QA-01 đến QA-20, kết quả Pass theo thông tin người dùng cung cấp. Legal confidence **Pending**; RAG/AI explanation **LOCKED toàn bộ 5 case**.

## Chuẩn bị và cách ghi kết quả

- Khởi động backend/frontend và dùng đúng hai sample theo [demo script](ROUND1_DEMO_SCRIPT_2026-09-09.md#chuẩn-bị-trước-khi-bấm-giờ); không sửa sample Excel.
- Backend: `http://127.0.0.1:8000`; Dashboard: `http://localhost:8501`.
- Trong PowerShell, lấy kết quả cho QA-02 đến QA-10 bằng `$scan = Invoke-RestMethod http://127.0.0.1:8000/demo/scan-all`. Chạy lại nếu khởi động lại backend hoặc đổi phiên kiểm tra.
- Các con số là kỳ vọng trên sample, không áp dụng cho mọi file người dùng upload. QA-19 tắt backend chỉ thực hiện trong buổi QA local, sau các kiểm tra cần backend; bật lại khi xong.
- Trạng thái chỉ dùng **Not run / Pass / Fail**. Kết quả lần chạy được báo cáo: **20/20 Pass**; chỉ đổi thành Pass khi có quan sát thực tế. Với dòng có nhiều bước, chỉ Pass khi mọi bước đạt.
- Điền người thực sự kiểm tra, thời điểm, kết quả thực tế và tham chiếu ảnh lỗi vào Ghi chú. Phân công bên dưới chưa phải bằng chứng đã chạy hoặc đã kiểm tra chéo.

Thông tin lần chạy: ngày/giờ: ___; commit (`git rev-parse HEAD`): ___; máy/môi trường: ___; người chạy: **Dương Văn Thiệp**. Ngày/giờ, commit và máy/môi trường của lần chạy chưa được cung cấp.

## Kết quả QA thủ công

- **Người kiểm tra:** Dương Văn Thiệp.
- **Kết quả:** QA-01 đến QA-20 đều **Pass**; Pass **20/20**, Fail **0/20**, Not run **0/20**.
- **Ghi chú tổng quát:** Đã chạy backend, `/health`, `/demo/scan-all`, Streamlit dashboard, demo cố định, bộ lọc `case_id`, bộ lọc severity, evidence expander, upload file Excel sample, upload file sai schema, backend-off fallback. Không thấy wording nguy hiểm.
- **Nguồn ghi nhận:** Kết quả chạy thủ công do người dùng cung cấp; Codex cập nhật tài liệu, không chạy lại ứng dụng trong phiên này. Không ghi nhận đây là lượt kiểm tra độc lập của Thế Anh.
- **Trạng thái giữ nguyên:** Legal confidence **Pending**; RAG/AI explanation **LOCKED toàn bộ 5 case**. Kết quả QA không đồng nghĩa pháp lý đã hoàn tất.

## 20 kịch bản QA nhanh

| ID | Mục tiêu | Cách chạy | Kết quả kỳ vọng | Trạng thái | Người kiểm tra | Ghi chú |
|---|---|---|---|---|---|---|
| QA-01 | Backend health | Chạy `Invoke-RestMethod http://127.0.0.1:8000/health` hoặc mở URL trên trình duyệt. | HTTP 200; JSON có `status = ok`, `service = TaxGPT backend`. | Pass | Dương Văn Thiệp | — |
| QA-02 | Endpoint scan-all | Chạy lệnh gán `$scan` ở trên; xem JSON qua `$scan` và `$scan.case_summary`. | HTTP 200; `status = ok`; có `case_summary` đủ 5 case và `alerts` gồm 9 phần tử. | Pass | Dương Văn Thiệp | — |
| QA-03 | Tổng hóa đơn | Xem `$scan.total_invoices`. | `12`. | Pass | Dương Văn Thiệp | — |
| QA-04 | Tổng thanh toán | Xem `$scan.total_payments`. | `6`. | Pass | Dương Văn Thiệp | — |
| QA-05 | Tổng cảnh báo | Xem `$scan.total_alerts` và `$scan.alerts.Count`. | Cả hai bằng `9`. | Pass | Dương Văn Thiệp | — |
| QA-06 | Case 1 | Xem `$scan.case_summary.CASE_1_DUPLICATE_INVOICE.total_alerts`. | `1` cảnh báo nhóm hóa đơn trùng. | Pass | Dương Văn Thiệp | — |
| QA-07 | Case 2 | Xem `$scan.case_summary.CASE_2_BUYER_INFO_MISMATCH.total_alerts`. | `2` cảnh báo thông tin người mua không khớp. | Pass | Dương Văn Thiệp | — |
| QA-08 | Case 3 | Xem `$scan.case_summary.CASE_3_VAT_MISMATCH.total_alerts`. | `2` cảnh báo VAT không khớp phép tính cơ bản. | Pass | Dương Văn Thiệp | — |
| QA-09 | Case 4 | Xem `$scan.case_summary.CASE_4_OUT_OF_REVIEW_PERIOD.total_alerts`. | `2` cảnh báo ngoài kỳ rà soát. | Pass | Dương Văn Thiệp | — |
| QA-10 | Case 5 | Xem `$scan.case_summary.CASE_5_MISSING_BANK_PAYMENT.total_alerts`. | `2` cảnh báo chưa tìm thấy thanh toán ngân hàng cho hóa đơn giá trị lớn trong dữ liệu cung cấp. | Pass | Dương Văn Thiệp | — |
| QA-11 | Dashboard mở được | Mở `http://localhost:8501`. | Hiện “TaxGPT Dashboard”, hai chế độ demo cố định/upload; không có exception. | Pass | Dương Văn Thiệp | — |
| QA-12 | Disclaimer | Đọc phần thông báo dưới tiêu đề dashboard. | Nêu chỉ hỗ trợ rà soát rủi ro; không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế. | Pass | Dương Văn Thiệp | — |
| QA-13 | Chạy demo cố định | Bấm “Chạy rà soát dữ liệu demo”; đặt hai bộ lọc về “Tất cả”. | Nguồn là “Dữ liệu demo cố định”; metric 12/6/9; bảng 5 case có 1/2/2/2/2; chi tiết hiển thị 9/9 cảnh báo. | Pass | Dương Văn Thiệp | — |
| QA-14 | Upload sample và hồi quy P0 | Chọn `data-mau/excel/sample_invoices_mvp.xlsx` vào ô hóa đơn và `data-mau/bank_statements/sample_bank_payments_mvp.xlsx` vào ô thanh toán; bấm “Chạy rà soát file tải lên”; đặt bộ lọc về “Tất cả”. | Không `StreamlitAPIException`; nguồn “File tải lên”; đúng tên hai file; metric 12/6/9; bảng case 1/2/2/2/2; 9/9 cảnh báo chi tiết. | Pass | Dương Văn Thiệp | — |
| QA-15 | Upload sai file/thiếu sheet/thiếu file | (a) Bỏ một file rồi bấm chạy. (b) Thử chọn file không phải `.xlsx` có sẵn. (c) Chọn sample thanh toán vào cả hai ô rồi chạy, để ô hóa đơn thiếu sheet `invoices`; sau đó chọn sample hóa đơn vào cả hai ô để ô thanh toán thiếu sheet `payments`. Khôi phục đúng hai sample khi xong. | (a) Báo cần chọn đủ hai file. (b) Uploader từ chối định dạng không hỗ trợ. (c) Backend trả HTTP 400, UI báo thiếu sheet thân thiện; không traceback/đường dẫn tạm. Không đánh đồng kết quả cũ còn trên màn hình với lần upload lỗi. | Pass | Dương Văn Thiệp | Ghi kết quả từng bước a/b/c; không sửa sample. |
| QA-16 | Bộ lọc case | Chạy lại demo hợp lệ, severity “Tất cả”; chọn lần lượt 5 case rồi về “Tất cả”. | Chi tiết lần lượt có 1/2/2/2/2 cảnh báo đúng case; về “Tất cả” có 9; metric và bảng tổng hợp không đổi. | Pass | Dương Văn Thiệp | — |
| QA-17 | Bộ lọc severity | Case “Tất cả”; chọn từng severity có trong dropdown, đối chiếu cột severity và số dòng với dữ liệu đầy đủ; thử kết hợp Case 3 và `medium`, sau đó reset. | Mỗi dòng khớp severity đã chọn; số dòng khớp dữ liệu nguồn; Case 3 + medium có 2; reset có 9. Nếu tổ hợp rỗng, hiển thị 0 cảnh báo, không crash. | Pass | Dương Văn Thiệp | — |
| QA-18 | Evidence expander | Chọn Case 3, severity “Tất cả”; mở “Xem evidence chi tiết”, mở mục `INV-DEMO-007` và `INV-DEMO-008`. | Có JSON evidence đúng hóa đơn với `taxable_amount`, `vat_rate`, `vat_amount`, `recalculated_vat`, `difference`, `tolerance`; đối chiếu phép tính với thuế suất đã chuẩn hóa, độ lệch vượt tolerance. Không có giải thích pháp lý tự sinh. | Pass | Dương Văn Thiệp | — |
| QA-19 | Backend tắt | Trong terminal backend local dùng Ctrl+C; bấm demo cố định, rồi thử upload hai sample. Sau đó bật lại backend, kiểm tra `/health` và chạy lại demo. | Hai thao tác khi backend tắt báo thân thiện “Backend chưa chạy…” kèm lệnh khởi động; không traceback/crash. Khi bật lại, demo hoạt động trở lại. | Pass | Dương Văn Thiệp | — |
| QA-20 | Wording an toàn | Đọc disclaimer, message của cả 9 cảnh báo, evidence và lời tập demo. | Không có khẳng định “vi phạm chắc chắn”, “kết luận sai phạm”, “đã xác minh pháp lý đầy đủ”; không tuyên bố thay thế chuyên gia hoặc RAG sẵn sàng. Legal confidence Pending, RAG/AI explanation LOCKED trong lời trình bày. | Pass | Dương Văn Thiệp | Câu phủ định “không kết luận sai phạm” và danh sách “Không được nói” là phù hợp; đánh giá theo ngữ cảnh, không chỉ tìm chuỗi. |

## Phân công

- **Dương Văn Thiệp:** chạy kỹ thuật, kiểm tra môi trường và sửa lỗi nếu có trong nhiệm vụ sửa lỗi riêng được giao; phiên tạo tài liệu này không thay đổi code.
- **Vũ Thế Anh:** chạy checklist độc lập, tự thao tác demo/cross-check 5 case, ghi Pass/Fail và chụp màn hình lỗi; không sao chép kết quả của người khác để coi là đã chạy độc lập.
- **Phạm Đình Khánh:** rà lại wording pháp lý an toàn nếu có thời gian. Việc rà wording hoặc QA kỹ thuật không nâng Legal confidence và không thay thế kiểm chứng pháp lý độc lập.

## Nguyên tắc

- Không mở RAG; RAG/AI explanation vẫn **LOCKED toàn bộ 5 case**.
- Không thêm giải thích pháp lý tự động; Legal confidence vẫn **Pending**.
- Không thay đổi rule trước demo nếu không cần. Lỗi chặn demo giao Thiệp xử lý trong phạm vi riêng, rồi chạy lại các kịch bản liên quan.
- Nếu lỗi không chặn demo, ghi vào **Known limitations**; giữ dòng kiểm tra là Fail nếu chưa đạt, không chuyển Pass chỉ vì có phương án dự phòng.
- Không sửa dữ liệu sample để làm kết quả khớp kỳ vọng. Không kết luận đã qua QA khi còn Not run; không gọi việc soạn hai tài liệu là hoàn tất cross-check.

## Known limitations

Giới hạn đã biết của MVP: chỉ `.xlsx` theo schema hiện tại; chưa XML/PDF/OCR, chưa xử lý đầy đủ ngoại lệ nghiệp vụ nâng cao; Case 3 chỉ đối chiếu phép tính cơ bản và chưa xác minh thuế suất pháp lý. Legal confidence Pending; RAG/AI explanation LOCKED.

Bảng dưới dành cho phát hiện từ lần QA thực tế; lượt chạy do Dương Văn Thiệp báo cáo đạt 20/20 Pass, không ghi nhận lỗi mới. Các giới hạn MVP nêu trên vẫn giữ nguyên:

| QA ID | Hiện tượng/kết quả thực tế | Chặn demo? | Phương án dự phòng | Người xử lý | Kết quả kiểm tra lại |
|---|---|---|---|---|---|
| — | Không ghi nhận lỗi mới trong kết quả QA thủ công được cung cấp. | — | — | — | — |

Kết thúc lần chạy: **Pass 20/20; Fail 0/20; Not run 0/20**. Người kiểm tra: **Dương Văn Thiệp**; thời điểm: chưa được cung cấp. Liệt kê lỗi chặn demo và xác nhận phương án dự phòng trước khi tập script.
