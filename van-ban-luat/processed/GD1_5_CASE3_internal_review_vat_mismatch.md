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

TaxGPT phát hiện dấu hiệu số tiền thuế GTGT không khớp với phép tính cơ bản từ giá tính thuế và thuế suất trong dữ liệu được cung cấp.

- Đây là cảnh báo rà soát dữ liệu.
- Đây không phải kết luận sai phạm.
- Cảnh báo không thay thế đánh giá của kế toán, luật sư, đại lý thuế hoặc cơ quan thuế.

## 3. Logic kỹ thuật hiện tại

Sau fix tại commit `a60f7bc`, logic kỹ thuật hiện tại là:

- `taxable_amount` là field nội bộ chuẩn cho Case 3.
- Parser giữ `taxable_amount` nếu file cung cấp field này. Nếu chỉ có `net_amount`, parser bổ sung `taxable_amount` từ `net_amount` và vẫn giữ field gốc.
- Nếu file có cả `taxable_amount` và `net_amount` nhưng hai giá trị không tương đương sau parse số, parser/API trả lỗi dữ liệu rõ ràng.
- Rule chạy trên mọi invoice có đủ `taxable_amount`, `vat_rate`, `vat_amount`; không còn phụ thuộc vào `expected_risk_case`.
- Thuế suất lớn hơn `1` được hiểu theo dạng phần trăm và chia cho `100`; thuế suất không lớn hơn `1` được dùng trực tiếp.
- Rule phát cảnh báo khi `abs(vat_amount - taxable_amount × vat_rate)` lớn hơn ngưỡng sai lệch.
- Ngưỡng sai lệch mặc định hiện tại là `1.0` theo đơn vị số tiền trong dữ liệu.
- Nếu thiếu một trong ba field tính toán, rule bỏ qua dòng đó mà không kết luận.
- Rule hiện chưa kiểm tra quan hệ `total_amount = taxable_amount + vat_amount`.

Ngưỡng `1.0` là tham số kỹ thuật hiện tại, không được mô tả là ngưỡng pháp luật. Việc làm tròn theo nghiệp vụ hoặc theo hóa đơn gốc chưa được xác minh pháp lý trong review này.

## 4. Bảng đối chiếu văn bản gốc

| Nhóm vấn đề | Văn bản cần kiểm tra | Điều/khoản/điểm | Nội dung liên quan rút ra | Trạng thái xác minh | Ghi chú/rủi ro |
|---|---|---|---|---|---|
| Căn cứ và giá tính thuế GTGT | Luật 48/2024/QH15 | Điều 6; điểm a và điểm k khoản 1 Điều 7 | Căn cứ tính thuế gồm giá tính thuế và thuế suất. Trường hợp bán hàng hóa, dịch vụ thông thường, giá tính thuế là giá chưa có thuế GTGT; nếu giá thanh toán đã có thuế thì có công thức quy đổi về giá chưa thuế. | Đã xác minh trực tiếp trên văn bản gốc | Điều 7 có nhiều trường hợp xác định giá tính thuế riêng; không được mặc định mọi `taxable_amount` đều là căn cứ đúng nếu chưa biết nghiệp vụ. |
| Thuế suất GTGT | Luật 48/2024/QH15 | Khoản 1, khoản 2, khoản 3 và khoản 4 Điều 9 | Luật quy định các mức 0%, 5%, 10%; nếu có nhiều loại hàng hóa, dịch vụ với mức khác nhau thì phải khai theo từng mức, trường hợp không xác định được thì áp dụng nguyên tắc tại khoản 4. | Đã xác minh trực tiếp trên văn bản gốc | Case 3 chỉ kiểm tra phép nhân theo `vat_rate` đầu vào, chưa xác định thuế suất đó có đúng đối tượng hay không. |
| Quan hệ giữa giá tính thuế, thuế suất và số thuế | Luật 48/2024/QH15 | Điểm b khoản 1 Điều 11 | Nội dung được ghi nhận là cơ sở tham chiếu cho phương pháp khấu trừ và số thuế GTGT đầu ra. Trong phạm vi TaxGPT, nội dung này chỉ được dùng để hỗ trợ cảnh báo kỹ thuật giữa giá trị tính thuế, thuế suất và tiền thuế. | Đã xác minh trực tiếp trên văn bản gốc | Chưa dùng để kết luận sai phạm pháp lý. |
| Phương pháp tính trực tiếp | Luật 48/2024/QH15 | Điều 12 | Luật còn quy định phương pháp trực tiếp, trong đó số thuế có thể được xác định theo tỷ lệ phần trăm trên doanh thu hoặc theo giá trị gia tăng. | Đã xác minh trực tiếp trên văn bản gốc | Rule hiện không nhận diện phương pháp tính thuế; có nguy cơ áp phép nhân của Case 3 cho dữ liệu thuộc phương pháp khác. |
| Nội dung sửa đổi/bổ sung | Luật 149/2025/QH15 — Luật sửa đổi, bổ sung một số điều của Luật Thuế GTGT | Pending | Pending | Pending | Cần rà xem có sửa đổi nội dung ảnh hưởng đến Case 3 hay không. |
| Giá tính thuế, thuế suất và phương pháp khấu trừ | Nghị định 181/2025/NĐ-CP | Các Điều 5–14; Điều 17–21 (mới xác định được phạm vi điều trên trang toàn văn chính thức) | Nguồn Chính phủ cho thấy các Điều 5–14 hướng dẫn nhiều trường hợp giá tính thuế; Điều 17–19 liên quan thuế suất; Điều 20–21 liên quan phương pháp khấu trừ. | Pending | Đã mở bản ký chính thức nhưng PDF scan chưa trích đọc tin cậy từng khoản. Cần đối chiếu trực tiếp nội dung chi tiết, nhất là giá tính thuế đặc thù, trước khi chốt ảnh hưởng tới Case 3. |
| Nội dung sửa đổi/bổ sung | Nghị định 359/2025/NĐ-CP | Khoản 1 và khoản 2 Điều 1 (phạm vi sửa đổi xác định từ nguồn Chính phủ) | Nguồn Chính phủ mô tả việc bổ sung khoản 1b sau khoản 1 Điều 4 và bãi bỏ khoản 3 Điều 39 của Nghị định 181/2025/NĐ-CP; chưa thấy nội dung trực tiếp thay đổi phép tính Case 3 trong phạm vi rà hiện tại. | Pending | Bản ký là PDF scan; cần kiểm tra chéo trực tiếp câu chữ và tình trạng hiệu lực trước khi kết luận không ảnh hưởng. |
| Nội dung sửa đổi/bổ sung | Nghị định 144/2026/NĐ-CP | Pending | Nguồn Chính phủ cho thấy văn bản sửa nhiều quy định GTGT, trong đó có nội dung liên quan Nghị định 181/2025/NĐ-CP. Chưa xác định chắc chắn toàn bộ ảnh hưởng trực tiếp tới giá tính thuế/Case 3. | Pending | Bản ký là PDF scan; phải rà chi tiết các điều sửa đổi, đặc biệt trường hợp giá tính thuế đặc thù, và kiểm tra chéo hiệu lực. |
| Phạm vi hướng dẫn | Thông tư 69/2025/TT-BTC | Điều 1; Điều 5; Điều 9 | Thông tư tập trung vào hồ sơ/thủ tục, nhóm áp dụng tỷ lệ phần trăm, hoàn thuế và thuế đối với tổ chức, cá nhân nước ngoài. Điều 5 và Điều 9 cho thấy có các trường hợp tính trực tiếp theo tỷ lệ trên doanh thu và cách xác định doanh thu riêng. | Đã xác minh trực tiếp trên văn bản gốc | Không xác định được trực tiếp trong phạm vi rà hiện tại một quy định của Thông tư 69 thay thế phép tính tại điểm b khoản 1 Điều 11 Luật 48 cho hóa đơn theo phương pháp khấu trừ. Các trường hợp tại Điều 5, Điều 9 là ngoại lệ phạm vi sản phẩm phải nhận diện. |

Bảng này chưa phải kết quả legal review độc lập. Các dòng `Pending` chỉ được chuyển trạng thái sau khi câu chữ trong bản gốc, tình trạng hiệu lực và ảnh hưởng tới Case 3 đã được kiểm tra đủ tin cậy và có kiểm tra chéo.

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
- Legal confidence: Pending. Đã ghi nhận điểm b khoản 1 Điều 11 Luật 48/2024/QH15 làm cơ sở tham chiếu cho phương pháp khấu trừ và số thuế GTGT đầu ra, nhưng chưa rà đủ ngoại lệ, văn bản sửa đổi và chưa có kiểm tra chéo.
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

- Đối chiếu trực tiếp từng khoản liên quan trong bản ký Nghị định 181/2025/NĐ-CP, Nghị định 359/2025/NĐ-CP và Nghị định 144/2026/NĐ-CP; giữ `Pending` cho đến khi đọc đủ tin cậy.
- Rà Luật 149/2025/QH15 để xác định có sửa đổi nội dung ảnh hưởng đến Case 3 hay không.
- Kiểm tra tình trạng hiệu lực và các văn bản sửa đổi/hợp nhất áp dụng tại thời điểm sử dụng sản phẩm.
- Xác định rõ cách nhận diện phương pháp khấu trừ so với phương pháp trực tiếp trước khi mở rộng phạm vi kết luận của Case 3.
- Đưa Thế Anh kiểm tra chéo nếu liên hệ được.
- Xác minh ngoại lệ làm tròn, hóa đơn nhiều dòng, chiết khấu, điều chỉnh/thay thế và ý nghĩa pháp lý của dữ liệu `taxable_amount`.
- Chưa bổ sung kiểm tra tổng tiền nếu chưa chốt được phạm vi nghiệp vụ và ngoại lệ.
- Sau khi file hoàn thành, mới cập nhật 3 file điều phối.

## 10. Ghi chú rà nguồn pháp lý ngày 01/09/2026

### 10.1. Nguồn đã mở

- [Luật Thuế GTGT 48/2024/QH15](https://vanban.chinhphu.vn/?classid=1&docid=212476&orggroupid=1&pageid=27160): đã mở trang hồ sơ và PDF gốc trên Cổng Thông tin điện tử Chính phủ; đã đối chiếu trực tiếp Điều 6, khoản 1 Điều 7, Điều 9, điểm b khoản 1 Điều 11 và Điều 12.
- Luật 149/2025/QH15 — Luật sửa đổi, bổ sung một số điều của Luật Thuế GTGT: chưa rà trực tiếp trong bước này; trạng thái `Pending`, cần xác định nội dung có ảnh hưởng đến Case 3 hay không.
- [Nghị định 181/2025/NĐ-CP](https://vanban.chinhphu.vn/?classid=1&docid=214336&pageid=27160): đã mở trang hồ sơ, bản ký chính thức và trang toàn văn của Chính phủ. Đã xác định sơ bộ nhóm điều liên quan nhưng bản ký là PDF scan, chưa đọc tin cậy từng khoản nên phần chi tiết vẫn `Pending`.
- [Nghị định 359/2025/NĐ-CP](https://vanban.chinhphu.vn/?classid=1&docid=216388&pageid=27160&typegroupid=4): đã mở trang hồ sơ, bản ký chính thức và bài giới thiệu nội dung mới trên nguồn Chính phủ. Bản ký là PDF scan; ảnh hưởng cuối cùng tới Case 3 vẫn `Pending`.
- [Nghị định 144/2026/NĐ-CP](https://vanban.chinhphu.vn/?classid=1&docid=218020&orggroupid=2&pageid=27160): đã mở trang hồ sơ, bản ký chính thức và trang toàn văn/tóm tắt trên nguồn Chính phủ. Bản ký là PDF scan; chưa đối chiếu đủ từng điều sửa đổi nên vẫn `Pending`.
- [Thông tư 69/2025/TT-BTC](https://vanban.chinhphu.vn/?classid=1&docid=214417&pageid=27160&typegroupid=6): đã mở trang hồ sơ Chính phủ và PDF gốc có chữ ký số trên hệ thống văn bản Bộ Tài chính; đã đối chiếu trực tiếp Điều 1, Điều 5 và Điều 9.

### 10.2. Kết quả ảnh hưởng tới Case 3

- Điểm b khoản 1 Điều 11 Luật 48/2024/QH15 được ghi nhận là cơ sở tham chiếu cho phương pháp khấu trừ và số thuế GTGT đầu ra; trong phạm vi TaxGPT, nội dung này chỉ được dùng để hỗ trợ cảnh báo kỹ thuật giữa giá trị tính thuế, thuế suất và tiền thuế. Chưa dùng để kết luận sai phạm pháp lý.
- Không xác định được trực tiếp trong phạm vi rà hiện tại một quy định pháp luật đặt ngưỡng sai lệch `1.0`; ngưỡng này tiếp tục chỉ là tham số kỹ thuật.
- Rule chưa kiểm tra `total_amount`; đã sửa mô tả mục tiêu trong file này để không hàm ý sản phẩm đang thực hiện phép kiểm tra đó.
- Wording cảnh báo hiện tại vẫn phù hợp ở mức cảnh báo dữ liệu, với điều kiện không dùng để kết luận thuế suất đúng, giá tính thuế đúng, gian lận hoặc vi phạm.
- Chưa cần sửa công thức lõi ở bước rà nguồn này. Bước kỹ thuật sau cần cân nhắc nhận diện phương pháp tính thuế và phạm vi dữ liệu trước khi áp dụng Case 3 rộng hơn; các ngoại lệ về giá tính thuế, nhiều dòng, chiết khấu, điều chỉnh và làm tròn còn `Pending`.
- Luật 48/2024/QH15 và Thông tư 69/2025/TT-BTC có dấu hiệu đã được sửa đổi hoặc hết hiệu lực một phần trên cơ sở dữ liệu pháp luật; cần kiểm tra văn bản sửa đổi/hợp nhất hiện hành trước khi chốt pháp lý.

### 10.3. Trạng thái còn lại

- Chưa có independent legal review.
- Chưa có kiểm tra chéo bởi Thế Anh/Khánh/người khác.
- Legal confidence vẫn `Pending`; không gọi review này là hoàn tất.
- Không đủ điều kiện mở RAG. RAG và AI explanation tiếp tục `LOCKED`.
