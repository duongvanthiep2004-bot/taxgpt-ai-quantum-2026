# GD1.5 — Case 3 Internal Legal Review sơ bộ: VAT calculation mismatch

## 1. Trạng thái kiểm soát

- Loại review: Internal legal review sơ bộ.
- Người/nhóm thực hiện: Đội trưởng/nhóm hiện tại với hỗ trợ AI.
- Independent legal review: Chưa có.
- Cross-check bởi Thế Anh/Khánh/người khác: Chưa có.
- RAG status: LOCKED.
- AI explanation status: LOCKED.
- Trạng thái kết luận: Chưa chốt pháp lý cuối cùng.

## 2. Mục tiêu Case 3

TaxGPT phát hiện dấu hiệu số tiền thuế GTGT không khớp với phép tính cơ bản từ tiền trước thuế, thuế suất, tiền thuế và tổng thanh toán trong dữ liệu được cung cấp.

- Đây là cảnh báo rà soát dữ liệu.
- Đây không phải kết luận sai phạm.
- Cảnh báo không thay thế đánh giá của kế toán, luật sư, đại lý thuế hoặc cơ quan thuế.

## 3. Logic kỹ thuật hiện tại

Ở mức khái quát, Case 3 hướng tới kiểm tra các quan hệ số học sau:

- So sánh `vat_amount` với `net_amount × vat_rate`.
- So sánh `total_amount` với `net_amount + vat_amount`.

Qua đối chiếu rule hiện tại tại `backend/app/rules/vat_mismatch.py`:

- Code đang dùng trường `taxable_amount` thay cho `net_amount` để tính lại tiền thuế.
- Thuế suất lớn hơn `1` được hiểu theo dạng phần trăm và chia cho `100`; thuế suất không lớn hơn `1` được dùng trực tiếp.
- Rule phát cảnh báo khi `abs(vat_amount - taxable_amount × vat_rate)` lớn hơn ngưỡng sai lệch.
- Ngưỡng sai lệch mặc định hiện tại là `1.0` theo đơn vị số tiền trong dữ liệu.
- Rule hiện chưa kiểm tra quan hệ `total_amount = net_amount + vat_amount`.
- Cần đối chiếu lại sự khác nhau giữa `taxable_amount` trong rule và `net_amount` trong dữ liệu upload trước khi mở rộng hoặc diễn giải logic.

Ngưỡng `1.0` là tham số kỹ thuật hiện tại, không được mô tả là ngưỡng pháp luật. Việc làm tròn theo nghiệp vụ hoặc theo hóa đơn gốc chưa được xác minh pháp lý trong review này.

## 4. Bảng đối chiếu văn bản gốc

| Nhóm vấn đề | Văn bản cần kiểm tra | Điều/khoản/điểm | Nội dung liên quan rút ra | Trạng thái xác minh | Ghi chú/rủi ro |
|---|---|---|---|---|---|
| Giá tính thuế GTGT | Luật 48/2024/QH15 | Pending | Pending | Chưa xác minh trực tiếp trên văn bản gốc | Cần đọc văn bản gốc |
| Thuế suất GTGT | Luật 48/2024/QH15 | Pending | Pending | Chưa xác minh trực tiếp trên văn bản gốc | Cần đọc văn bản gốc |
| Hướng dẫn chi tiết thi hành | Nghị định 181/2025/NĐ-CP | Pending | Pending | Chưa xác minh trực tiếp trên văn bản gốc | Cần đọc văn bản gốc |
| Nội dung sửa đổi/bổ sung | Nghị định 359/2025/NĐ-CP | Pending | Pending | Chưa xác minh trực tiếp trên văn bản gốc | Cần kiểm tra có ảnh hưởng Case 3 không |
| Nội dung sửa đổi/bổ sung | Nghị định 144/2026/NĐ-CP | Pending | Pending | Chưa xác minh trực tiếp trên văn bản gốc | Cần kiểm tra có ảnh hưởng Case 3 không |
| Hướng dẫn của Bộ Tài chính | Thông tư 69/2025/TT-BTC | Pending | Pending | Chưa xác minh trực tiếp trên văn bản gốc | Cần kiểm tra hướng dẫn liên quan nếu có |

Bảng này là khung đối chiếu ban đầu. Chỉ chuyển trạng thái sang “Đã xác minh” khi đã mở văn bản gốc và kiểm tra điều/khoản cụ thể.

## 5. Các ngoại lệ/rủi ro nghiệp vụ cần giữ thận trọng

- Hóa đơn nhiều dòng hàng.
- Nhiều mức thuế suất trên cùng hóa đơn.
- Chiết khấu.
- Làm tròn số.
- Hàng hóa/dịch vụ không chịu thuế hoặc có cách xử lý đặc biệt.
- Hóa đơn điều chỉnh.
- Hóa đơn thay thế.
- Dữ liệu Excel chỉ là bản tổng hợp, thiếu dòng chi tiết.
- Dữ liệu nhập thủ công có thể sai format.

Các trường hợp trên có thể làm phép tính tổng hợp khác với phép tính đơn giản ở cấp hóa đơn. Vì vậy, một sai lệch số học chỉ nên kích hoạt bước rà soát chứng từ và dữ liệu chi tiết.

## 6. Wording an toàn đề xuất cho Dashboard/API

Wording được phép dùng:

> Có dấu hiệu số tiền thuế GTGT không khớp với phép tính cơ bản từ dữ liệu được cung cấp. Cần rà soát lại hóa đơn, thuế suất, dòng hàng, cách làm tròn và chứng từ liên quan.

Wording không được dùng:

- vi phạm pháp luật
- gian lận
- hóa đơn vô hiệu
- không được khấu trừ
- bị xử phạt
- bị loại chi phí
- ngưỡng pháp luật
- kết luận sai phạm

## 7. Đánh giá sơ bộ Case 3

- Technical confidence: High, vì logic số học có thể kiểm tra được.
- Legal confidence: Pending, vì chưa rà đủ văn bản gốc.
- Product wording: Safe warning only.
- RAG status: LOCKED.

Technical confidence chỉ áp dụng cho khả năng phát hiện sai lệch theo rule số học đã cấu hình; không đồng nghĩa với độ tin cậy của kết luận pháp lý hoặc mức độ đầy đủ của dữ liệu đầu vào.

## 8. Điều kiện tối thiểu trước khi cân nhắc mở RAG cho Case 3

Chỉ cân nhắc mở RAG nếu đáp ứng đầy đủ:

1. Đã xác minh văn bản gốc.
2. Đã ghi rõ điều/khoản/điểm liên quan.
3. Đã kiểm tra văn bản sửa đổi/bổ sung.
4. Đã có bảng đối chiếu sạch.
5. Đã có kiểm tra chéo tối thiểu, ưu tiên Thế Anh hoặc người khác.
6. Wording vẫn không kết luận pháp lý.

Việc đáp ứng các điều kiện trên chỉ cho phép cân nhắc; không tự động mở RAG và không đồng nghĩa Case 3 đã hoàn tất pháp lý.

## 9. Việc cần làm tiếp

- Mở từng văn bản gốc chính thức.
- Tìm phần giá tính thuế, thuế suất, xác định số thuế GTGT và hóa đơn/chứng từ nếu có liên quan.
- Điền điều/khoản/điểm vào bảng.
- Đánh dấu điểm còn chưa chắc.
- Đưa Thế Anh kiểm tra chéo nếu liên hệ được.
- Đối chiếu lại `taxable_amount`, `net_amount`, phép kiểm tra tổng tiền và ngưỡng sai lệch với backend rule hiện tại.
- Sau khi file hoàn thành, mới cập nhật 3 file điều phối.
