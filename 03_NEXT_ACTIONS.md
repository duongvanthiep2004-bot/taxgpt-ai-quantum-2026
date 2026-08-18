# 03_NEXT_ACTIONS — TaxGPT

## Trạng thái hiện tại

- 5/5 case MVP đã có backend slice ở mức parser/rule/API/test: hóa đơn trùng; sai MST/tên người mua; VAT không khớp phép tính; hóa đơn ngoài kỳ dữ liệu đang rà soát; hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt.
- Toàn bộ test hiện đạt `32 passed, 1 warning`.
- Case 5 đã hoàn thành code/test/API, nhưng báo cáo cuối phiên chưa xác nhận commit/push.
- Frontend Streamlit chưa kết nối backend; chưa có upload file thật; chưa có API tổng hợp `GET /demo/scan-all`.
- RAG và AI explanation chưa triển khai. RAG bị khóa cho đến khi nguồn, hiệu lực và điều/khoản pháp lý được Khánh cùng Gemini Pro kiểm chứng.
- Ngôn ngữ rule phải tiếp tục chỉ cảnh báo “có dấu hiệu”, “cần rà soát”; không kết luận gian lận, vi phạm, hóa đơn vô hiệu, không được khấu trừ, bị xử phạt hoặc bị loại chi phí.
- Đây là tiến độ backend tốt nhất từ đầu dự án, nhưng dự án **chưa phải prototype end-to-end**.

## Thứ tự ưu tiên

### P0 — Xác nhận Case 5 đã commit/push

Chạy đầu tiên ở phiên sau:

```bash
git status
```

Nếu còn file `modified` hoặc `untracked` của Case 5 thì thực hiện:

```bash
git add backend/app/main.py backend/app/parsers/payment_parser.py backend/app/rules/missing_bank_payment.py backend/tests/test_case_5_missing_bank_payment.py
git commit -m "Implement backend missing bank payment case"
git push
```

Chỉ đánh dấu hoàn thành sau khi xác nhận working tree và remote phù hợp.

### P1 — API tổng hợp `GET /demo/scan-all`

- Chạy cả 5 rule trên cùng bộ dữ liệu mẫu.
- Trả danh sách cảnh báo thống nhất và tổng hợp số lượng theo case.
- Giữ nguyên ngôn ngữ cảnh báo an toàn pháp lý của từng rule.

### P2 — Test cho scan-all

- Kiểm tra HTTP 200, schema response, tổng số cảnh báo và phân nhóm theo 5 case.
- Chạy toàn bộ suite để bảo đảm không làm hỏng các endpoint riêng lẻ.

### P3 — Kết nối Streamlit gọi scan-all và hiển thị dashboard cảnh báo

- Gọi `GET /demo/scan-all` từ Streamlit.
- Hiển thị bảng cảnh báo theo case, mức độ và hóa đơn liên quan; hiển thị lỗi rõ ràng khi backend không khả dụng.
- Mốc này tạo prototype demo local không RAG trên dữ liệu mẫu, chưa phải luồng upload file thật.

### P4 — Kiểm chứng pháp lý RAG với Khánh + Gemini Pro

- Đối chiếu nguồn gốc, hiệu lực và điều/khoản cho từng nội dung dự kiến ingest.
- Ghi rõ nội dung đã xác minh, chưa xác minh và điểm cần chuyên gia quyết định.
- Không ingest tài liệu chưa kiểm chứng.

### P5 — Upload file thật thay vì file demo cố định

- Cho phép người dùng đưa file đầu vào qua Streamlit/API thay cho đường dẫn demo cố định.
- Kiểm tra định dạng, schema và thông báo lỗi an toàn trước khi chạy scan-all.

### P6 — RAG pháp lý + AI explanation sau khi pháp lý được kiểm chứng

- Chỉ bắt đầu khi P4 đã hoàn tất đủ căn cứ cho phạm vi MVP.
- Trả trích dẫn nguồn và từ chối kết luận khi không đủ căn cứ.
- AI explanation phải giữ vai trò giải thích cảnh báo và gợi ý rà soát, không thay chuyên gia thuế đưa ra kết luận pháp lý.

## Bước tiếp theo cụ thể

**Bước đã hoàn thành:** 5/5 case MVP đã có backend slice ở mức parser/rule/API/test; toàn bộ suite đạt `32 passed, 1 warning`.

**Bước đầu phiên sau:** chạy `git status`, xác nhận Case 5 đã commit/push và lưu thay đổi nếu cần; sau đó triển khai `GET /demo/scan-all` cùng test.

## Ước lượng tiến độ

- **Mức 1 — Prototype demo local không RAG:** Excel mẫu → scan-all → Streamlit hiển thị bảng cảnh báo; ước tính 1–2 phiên, khoảng 2–4 ngày.
- **Mức 2 — RAG pháp lý + trích dẫn + AI explanation:** phụ thuộc kiểm chứng pháp lý; nếu pháp lý xong trong tuần này thì cần thêm khoảng 2–3 phiên, ước tính 1–1.5 tuần.
- **Tổng mức trình diễn đầy đủ:** khoảng 1.5–2 tuần nếu pháp lý không bị trì hoãn.
- **Rủi ro lớn nhất hiện tại:** kiểm chứng pháp lý, không phải kỹ thuật backend.

## Không làm vội trước khi có prototype chạy được

- Ngoại lệ nâng cao như hóa đơn điều chỉnh/thay thế.
- Thanh toán từng phần/gộp.
- Bù trừ công nợ.
- OCR/PDF phức tạp.

Các hạng mục này để sau khi prototype demo local đã chạy được và được kiểm tra ổn định.

## Nguyên tắc thực hiện

- Sau mỗi nhiệm vụ, append kết quả vào `02_SESSION_LOG.md`.
- Chỉ cập nhật task thành `[x]` khi có output và bằng chứng đáp ứng Definition of Done.
- Không tự ý thay đổi phạm vi 5 case MVP khi chưa có xác nhận của đội.
- Không gọi dự án là prototype end-to-end cho đến khi có ít nhất upload file thật, scan-all và frontend kết nối backend; RAG/AI explanation chỉ được tuyên bố khi đã triển khai và kiểm chứng.
