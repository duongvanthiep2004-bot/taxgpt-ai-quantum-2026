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
| Nội dung sửa đổi/bổ sung | Luật 149/2025/QH15 — Luật sửa đổi, bổ sung một số điều của Luật Thuế GTGT | Khoản 1, khoản 2 và khoản 3 Điều 1; Điều 2 | Sửa khoản 1 và khoản 25 Điều 5; sửa khoản 5 Điều 9; bãi bỏ khoản 3 Điều 12 và điểm c khoản 9 Điều 15 của Luật 48/2024/QH15. Luật có hiệu lực từ 01/01/2026. | Đã xác minh trực tiếp trên bản ký chính thức | Khoản 5 Điều 9 liên quan cách xác định thuế suất cho phế phẩm, phụ phẩm, phế liệu; việc bãi bỏ khoản 3 Điều 12 thu hẹp một trường hợp phương pháp trực tiếp. Không xác định thấy Luật 149 sửa trực tiếp Điều 6, Điều 7 hoặc Điều 11 trong phạm vi rà hiện tại. |
| Giá tính thuế, thuế suất và phương pháp khấu trừ | Nghị định 181/2025/NĐ-CP | Điều 1; các Điều 5–14; Điều 17–22; đã đối chiếu trực tiếp khoản 1, khoản 2 Điều 5; khoản 1, khoản 2 Điều 6; khoản 1 Điều 7; khoản 2 Điều 9; khoản 1–3 Điều 20; Điều 21 và Điều 22 | Điều 5–14 hướng dẫn chi tiết giá tính thuế; Điều 17–19 quy định chi tiết nhóm thuế suất; khoản 2 Điều 20 quy định thuế GTGT đầu ra trên hóa đơn bằng giá tính thuế nhân thuế suất và có công thức quy đổi khi giá thanh toán đã gồm thuế; Điều 21 xác định đối tượng áp dụng phương pháp khấu trừ; Điều 22 quy định cách tính trực tiếp riêng cho vàng, bạc, đá quý. | Đã xác minh trực tiếp các phần trọng yếu nêu tại Mục 12; chưa phải kiểm tra chéo độc lập | Công thức lõi có cơ sở cho thuế đầu ra theo phương pháp khấu trừ, nhưng không đủ để xác nhận `taxable_amount` hoặc `vat_rate` đầu vào là đúng. Nghị định có nhiều giá tính thuế đặc thù và phương pháp trực tiếp khác; đồng thời Nghị định 359/2025/NĐ-CP và 144/2026/NĐ-CP sửa đổi Nghị định 181 nên tình trạng áp dụng hiện hành vẫn `Pending`. |
| Nội dung sửa đổi/bổ sung | Nghị định 359/2025/NĐ-CP | Khoản 1 và khoản 2 Điều 1 (phạm vi sửa đổi xác định từ nguồn Chính phủ) | Nguồn Chính phủ mô tả việc bổ sung khoản 1b sau khoản 1 Điều 4 và bãi bỏ khoản 3 Điều 39 của Nghị định 181/2025/NĐ-CP; chưa thấy nội dung trực tiếp thay đổi phép tính Case 3 trong phạm vi rà hiện tại. | Pending | Bản ký là PDF scan; cần kiểm tra chéo trực tiếp câu chữ và tình trạng hiệu lực trước khi kết luận không ảnh hưởng. |
| Nội dung sửa đổi/bổ sung | Nghị định 144/2026/NĐ-CP | Pending | Nguồn Chính phủ cho thấy văn bản sửa nhiều quy định GTGT, trong đó có nội dung liên quan Nghị định 181/2025/NĐ-CP. Chưa xác định chắc chắn toàn bộ ảnh hưởng trực tiếp tới giá tính thuế/Case 3. | Pending | Bản ký là PDF scan; phải rà chi tiết các điều sửa đổi, đặc biệt trường hợp giá tính thuế đặc thù, và kiểm tra chéo hiệu lực. |
| Phạm vi hướng dẫn | Thông tư 69/2025/TT-BTC | Điều 1; Điều 5; Điều 9 | Thông tư tập trung vào hồ sơ/thủ tục, nhóm áp dụng tỷ lệ phần trăm, hoàn thuế và thuế đối với tổ chức, cá nhân nước ngoài. Điều 5 và Điều 9 cho thấy có các trường hợp tính trực tiếp theo tỷ lệ trên doanh thu và cách xác định doanh thu riêng. | Đã xác minh trực tiếp trên văn bản gốc | Không xác định được trực tiếp trong phạm vi rà hiện tại một quy định của Thông tư 69 thay thế phép tính tại điểm b khoản 1 Điều 11 Luật 48 cho hóa đơn theo phương pháp khấu trừ. Các trường hợp tại Điều 5, Điều 9 là ngoại lệ phạm vi sản phẩm phải nhận diện. |

Bảng này chưa phải kết quả legal review độc lập. Các dòng `Pending` chỉ được chuyển trạng thái sau khi câu chữ trong bản gốc, tình trạng hiệu lực và ảnh hưởng tới Case 3 đã được kiểm tra đủ tin cậy và có kiểm tra chéo.

## 5. Các ngoại lệ/rủi ro nghiệp vụ cần giữ thận trọng

- Hóa đơn nhiều dòng hàng.
- Nhiều mức thuế suất trên cùng hóa đơn.
- Giá thanh toán đã bao gồm thuế GTGT và phải quy đổi về giá chưa thuế.
- Chiết khấu thương mại, khuyến mại, hàng biếu/tặng/trao đổi và tiêu dùng nội bộ.
- Giá tính thuế đặc thù đối với nhập khẩu, cho thuê/trả tiền trước, gia công, xây dựng, bất động sản, đại lý/môi giới, casino/trò chơi có thưởng/cá cược, du lịch trọn gói, cầm đồ, sách, viễn thông quốc tế và dịch vụ của nhà thầu nước ngoài.
- Phương pháp trực tiếp đối với vàng, bạc, đá quý hoặc trường hợp tính theo tỷ lệ trên doanh thu.
- Làm tròn số.
- Hàng hóa/dịch vụ không chịu thuế hoặc có cách xử lý đặc biệt.
- Hóa đơn điều chỉnh.
- Hóa đơn thay thế.
- Dữ liệu Excel chỉ là bản tổng hợp, thiếu dòng chi tiết.
- Dữ liệu nhập thủ công có thể sai format.

Các trường hợp trên có thể làm phép tính tổng hợp khác với phép tính đơn giản ở cấp hóa đơn. Vì vậy, một sai lệch số học chỉ nên kích hoạt bước rà soát chứng từ và dữ liệu chi tiết.

## 6. Wording an toàn đề xuất cho Dashboard/API

Wording được phép dùng:

> Có dấu hiệu số tiền thuế GTGT không khớp với phép tính cơ bản từ các trường dữ liệu được cung cấp. Cần xác minh phương pháp tính thuế, giá tính thuế, thuế suất, từng dòng hàng, trường hợp giá đã bao gồm thuế, chiết khấu/khuyến mại, cách làm tròn và chứng từ liên quan trước khi kết luận.

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
- Legal confidence: Pending. Đã ghi nhận điểm b khoản 1 Điều 11 Luật 48/2024/QH15 làm cơ sở tham chiếu, đã rà riêng Luật 149/2025/QH15 và đã đọc sâu các phần trọng yếu của Nghị định 181/2025/NĐ-CP tại Mục 12; tuy nhiên, Nghị định 359/2025/NĐ-CP, Nghị định 144/2026/NĐ-CP, các ngoại lệ còn lại và tình trạng áp dụng theo thời điểm chưa được rà sạch, đồng thời chưa có kiểm tra chéo.
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

- Nghị định 181/2025/NĐ-CP đã được rà sâu các phần trọng yếu tại Mục 12; tiếp tục rà Nghị định 359/2025/NĐ-CP và Nghị định 144/2026/NĐ-CP để xác định chính xác phần sửa đổi và tình trạng áp dụng hiện hành.
- Luật 149/2025/QH15 đã được rà riêng tại Mục 11; tiếp tục giữ thận trọng với tác động của thay đổi thuế suất và phạm vi phương pháp trực tiếp cho đến khi có kiểm tra chéo.
- Kiểm tra tình trạng hiệu lực và các văn bản sửa đổi/hợp nhất áp dụng tại thời điểm sử dụng sản phẩm.
- Xác định rõ cách nhận diện phương pháp khấu trừ so với phương pháp trực tiếp trước khi mở rộng phạm vi kết luận của Case 3.
- Đưa Thế Anh kiểm tra chéo nếu liên hệ được.
- Xác minh ngoại lệ làm tròn, hóa đơn nhiều dòng, chiết khấu, điều chỉnh/thay thế và ý nghĩa pháp lý của dữ liệu `taxable_amount`.
- Chưa bổ sung kiểm tra tổng tiền nếu chưa chốt được phạm vi nghiệp vụ và ngoại lệ.
- Sau khi file hoàn thành, mới cập nhật 3 file điều phối.

## 10. Ghi chú rà nguồn pháp lý ngày 01/09/2026

### 10.1. Nguồn đã mở

- [Luật Thuế GTGT 48/2024/QH15](https://vanban.chinhphu.vn/?classid=1&docid=212476&orggroupid=1&pageid=27160): đã mở trang hồ sơ và PDF gốc trên Cổng Thông tin điện tử Chính phủ; đã đối chiếu trực tiếp Điều 6, khoản 1 Điều 7, Điều 9, điểm b khoản 1 Điều 11 và Điều 12.
- Luật 149/2025/QH15 — Luật sửa đổi, bổ sung một số điều của Luật Thuế GTGT: tại thời điểm ghi chú 01/09 chưa rà trực tiếp; đã được rà riêng trên bản ký chính thức ngày 03/09/2026 tại Mục 11.
- [Nghị định 181/2025/NĐ-CP](https://vanban.chinhphu.vn/?classid=1&docid=214336&pageid=27160): tại thời điểm ghi chú 01/09 mới xác định sơ bộ nhóm điều liên quan; ngày 03/09/2026 đã rà sâu bản ký và trang toàn văn chính thức đối với các phần trọng yếu tại Mục 12. Việc áp dụng văn bản sau sửa đổi vẫn `Pending`.
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

## 11. Rà Luật 149/2025/QH15 ngày 03/09/2026

### 11.1. Nguồn và mức độ đọc

- Nguồn chốt: [hồ sơ Luật 149/2025/QH15 trên Cổng Thông tin điện tử Chính phủ](https://vanban.chinhphu.vn/?docid=216588&pageid=27160) và [PDF bản ký chính thức](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat149.signed.pdf).
- Đã mở và đối chiếu đủ 2 trang của bản ký. Hồ sơ chính thức ghi Luật được ban hành ngày 11/12/2025 và có hiệu lực từ 01/01/2026.
- Nguồn phụ trợ tra nhanh: [bài giới thiệu điểm mới trên chuyên trang Xây dựng chính sách, pháp luật của Báo điện tử Chính phủ](https://xaydungchinhsach.chinhphu.vn/nhung-diem-moi-cua-luat-thue-gia-tri-gia-tang-sua-doi-2025-119260110094146844.htm). Nguồn này chỉ dùng hỗ trợ định vị nội dung; không thay thế bản ký và không phải nguồn chốt.

### 11.2. Các nội dung Luật 149 sửa đổi, bổ sung hoặc bãi bỏ

| Căn cứ Luật 149 | Quy định của Luật 48 bị tác động | Tóm tắt ngắn | Ảnh hưởng tới Case 3 | Mức chắc chắn |
|---|---|---|---|---|
| Điểm a khoản 1 Điều 1 | Khoản 1 Điều 5 | Sửa nhóm sản phẩm nông, lâm, chăn nuôi, thủy sản không chịu thuế và bổ sung trường hợp giao dịch giữa doanh nghiệp/hợp tác xã/liên hiệp hợp tác xã không phải kê khai, tính nộp thuế nhưng được khấu trừ đầu vào. | Có thể ảnh hưởng phạm vi áp dụng: không nên chạy cảnh báo phép nhân một cách máy móc cho dữ liệu thuộc nhóm không chịu thuế/không phải kê khai, tính nộp. Không sửa công thức lõi của rule. | Cao về nội dung sửa; Trung bình về đánh giá tác động sản phẩm |
| Điểm b khoản 1 Điều 1 | Khoản 25 Điều 5 | Nâng ngưỡng doanh thu năm của hàng hóa, dịch vụ do hộ/cá nhân sản xuất, kinh doanh thuộc diện không chịu thuế lên 500 triệu đồng; đồng thời quy định lại các nhóm khác trong khoản này. | Có thể làm thay đổi phạm vi chứng từ/dữ liệu mà Case 3 nên áp dụng; không sửa phép tính `taxable_amount × vat_rate`. | Cao về nội dung sửa; Trung bình về đánh giá tác động sản phẩm |
| Khoản 2 Điều 1 | Khoản 5 Điều 9 | Quy định lại thuế suất đối với phế phẩm, phụ phẩm, phế liệu thu hồi trong quá trình sản xuất theo mặt hàng tương ứng. | Có liên quan trực tiếp đến cơ sở pháp lý của giá trị `vat_rate` nếu dữ liệu thuộc nhóm này. Rule hiện chỉ dùng thuế suất đầu vào, không xác định thuế suất đó có đúng pháp luật; chưa xác định thấy thay đổi trực tiếp đối với phép nhân lõi. | Cao về nội dung sửa; Trung bình về đánh giá tác động sản phẩm |
| Khoản 3 Điều 1 | Khoản 3 Điều 12 | Bãi bỏ quy định về phương pháp khoán thuế đối với hộ, cá nhân sản xuất, kinh doanh không thực hiện hoặc thực hiện không đầy đủ chế độ kế toán, hóa đơn, chứng từ. | Tác động trực tiếp đến một phần phạm vi phương pháp trực tiếp từ 01/01/2026, nhưng không bãi bỏ toàn bộ Điều 12. Case 3 vẫn phải nhận diện phương pháp tính thuế trước khi mở rộng phạm vi. | Cao về nội dung bãi bỏ; Trung bình về đánh giá tác động sản phẩm |
| Khoản 3 Điều 1 | Điểm c khoản 9 Điều 15 | Bãi bỏ một điều kiện liên quan đến hoàn thuế. | Chưa xác định thấy ảnh hưởng trực tiếp trong phạm vi rà hiện tại đối với phép so sánh của Case 3. | Cao |
| Điều 2 | Hiệu lực thi hành | Luật có hiệu lực từ 01/01/2026; không xác định thấy điều khoản chuyển tiếp riêng trong 2 trang Luật 149. | Việc đánh giá chứng từ trước/sau mốc hiệu lực phải dùng quy định phù hợp theo thời điểm. | Cao |

### 11.3. Kiểm tra riêng các nhóm điều của Case 3

- **Điều 6 — căn cứ tính thuế:** Không xác định thấy sửa đổi trực tiếp trong phạm vi rà hiện tại.
- **Điều 7 — giá tính thuế:** Không xác định thấy sửa đổi trực tiếp trong phạm vi rà hiện tại.
- **Điều 9 — thuế suất:** Có. Khoản 2 Điều 1 Luật 149 sửa khoản 5 Điều 9 như nêu tại Mục 11.2.
- **Điều 11 — phương pháp khấu trừ:** Không xác định thấy sửa đổi trực tiếp trong phạm vi rà hiện tại. Việc khoản 1 Điều 5 mới nhắc đến khấu trừ thuế đầu vào không đồng nghĩa Luật 149 sửa trực tiếp Điều 11.
- **Điều 12 — phương pháp trực tiếp:** Có. Khoản 3 Điều 1 Luật 149 bãi bỏ khoản 3 Điều 12; các phần còn lại của Điều 12 không bị bãi bỏ bởi quy định này.
- **Hiệu lực/chuyển tiếp:** Điều 2 quy định hiệu lực từ 01/01/2026. Không xác định thấy điều khoản chuyển tiếp riêng trong phạm vi bản ký đã rà.

### 11.4. Kết luận tác động tới Case 3

- Luật 149 có **liên quan trực tiếp đến phạm vi pháp lý của hai input/ngữ cảnh** mà Case 3 đang dùng: khoản 5 Điều 9 ảnh hưởng cách xác định `vat_rate` cho một nhóm hàng hóa cụ thể; việc bãi bỏ khoản 3 Điều 12 thay đổi một phần phạm vi phương pháp trực tiếp.
- Chưa xác định thấy Luật 149 sửa trực tiếp phép tính lõi `taxable_amount × vat_rate` so với `vat_amount`, sửa Điều 6, Điều 7 hoặc Điều 11, hay quy định ngưỡng sai lệch `1.0` trong phạm vi rà hiện tại. Vì vậy, review này chưa cho thấy cần đổi công thức kỹ thuật hiện tại chỉ do Luật 149.
- Kết luận thận trọng: **chưa xác định thấy ảnh hưởng trực tiếp đến phép so sánh số học lõi trong phạm vi rà hiện tại**; tuy nhiên, có ảnh hưởng liên quan đến việc xác định thuế suất đầu vào và phạm vi áp dụng. Không ghi nhận kết luận tuyệt đối là “không ảnh hưởng” khi chưa có kiểm tra chéo.

### 11.5. Điểm còn Pending và trạng thái kiểm soát

- Cần đối chiếu sâu các văn bản sửa đổi/hợp nhất có liên quan để xác định cách áp dụng theo thời điểm. Nghị định 181/2025/NĐ-CP đã được rà sâu các phần trọng yếu tại Mục 12; Nghị định 359/2025/NĐ-CP và 144/2026/NĐ-CP vẫn `Pending`.
- Cần xác định cách sản phẩm nhận diện đối tượng không chịu thuế/không phải kê khai, tính nộp; thuế suất đúng; và phương pháp khấu trừ so với phương pháp trực tiếp trước khi mở rộng Case 3.
- Review này chỉ rà tác động của Luật 149; chưa thay thế việc kiểm tra đầy đủ Luật 48 sau các lần sửa đổi khác hoặc văn bản hợp nhất áp dụng tại thời điểm sử dụng sản phẩm.
- Chưa có independent legal review và chưa có cross review bởi Thế Anh/Khánh/người khác.
- **Legal confidence vẫn `Pending`.** Review này không làm Case 3 hoàn tất pháp lý.
- **RAG/AI explanation vẫn `LOCKED`.**

## 12. Rà Nghị định 181/2025/NĐ-CP ngày 03/09/2026

### 12.1. Nguồn và mức độ đọc

- Nguồn chốt: [hồ sơ Nghị định 181/2025/NĐ-CP trên Cổng Thông tin điện tử Chính phủ](https://vanban.chinhphu.vn/?docid=214336&lang=vi&pageid=27160), [PDF bản ký chính thức](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/181nd.signed.pdf) và [trang toàn văn chính thức của Chính phủ](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-181-2025-nd-cp-quy-dinh-chi-tiet-thi-hanh-mot-so-dieu-cua-luat-thue-gia-tri-gia-tang-119250707172930626.htm).
- Bản ký chính thức dài 75 trang và là PDF scan. Đã đọc/đối chiếu trực tiếp hình ảnh bản ký đối với khoản 1, khoản 2 Điều 5; khoản 1, khoản 2 Điều 6; khoản 1 Điều 7; khoản 1–3 Điều 20; Điều 21; Điều 22 và phần đầu Điều 23.
- Đã dùng trang toàn văn chính thức để xác định cấu trúc, phạm vi Điều 1 và nội dung các Điều 5–14, 17–22. Nguồn phụ trợ chỉ dùng để định vị nhanh câu chữ; không được dùng làm nguồn chốt.
- Nghị định có hiệu lực từ 01/07/2025. Do đã có Nghị định 359/2025/NĐ-CP và Nghị định 144/2026/NĐ-CP sửa đổi, review này không coi bản Nghị định 181 ban đầu là bản hợp nhất hiện hành.

### 12.2. Giá tính thuế — Điều 7 Luật 48

- Điều 1 xác nhận Nghị định quy định chi tiết Điều 7 Luật Thuế GTGT; các Điều 5–14 là nhóm hướng dẫn về giá tính thuế.
- **Điều 5:** giá bán hàng hóa/dịch vụ thông thường là giá chưa có thuế GTGT; giá tính thuế hàng nhập khẩu gồm trị giá tính thuế nhập khẩu và các khoản thuế được liệt kê theo từng trường hợp.
- **Điều 6:** hàng hóa/dịch vụ dùng để trao đổi, tiêu dùng nội bộ, biếu, tặng và các trường hợp tương tự có căn cứ theo hàng hóa/dịch vụ cùng loại hoặc tương đương; có ngoại lệ đối với luân chuyển nội bộ phục vụ tiếp tục quá trình sản xuất, kinh doanh. Hàng khuyến mại đúng pháp luật có thể có giá tính thuế bằng 0; hình thức giảm giá dùng giá đã giảm.
- **Điều 7:** quy định giá tính thuế đối với cho thuê tài sản, gia công và xây dựng; riêng cho thuê có cách xử lý theo kỳ hoặc thu tiền trước.
- **Điều 8:** bất động sản dùng giá chuyển nhượng chưa có thuế GTGT trừ giá đất được trừ; có nhiều trường hợp riêng về giao đất, thuê đất, nhận chuyển nhượng/quyền sử dụng đất, dự án và thu tiền theo tiến độ.
- **Khoản 1 Điều 9:** quy định giá tính thuế là tiền hoa hồng chưa có thuế trong các hoạt động đại lý/môi giới thuộc phạm vi điều này. **Khoản 2 Điều 9:** khi hóa đơn ghi giá thanh toán đã có thuế GTGT thì giá chưa thuế được quy đổi bằng giá thanh toán chia cho `1 + thuế suất`.
- **Điều 10–13:** có cách xác định riêng đối với casino, trò chơi điện tử có thưởng, kinh doanh giải trí có đặt cược; điện, vận tải/bốc xếp, du lịch trọn gói, cầm đồ, sách, in; viễn thông quốc tế; và dịch vụ do nhà thầu nước ngoài cung cấp.
- **Điều 14:** giá tính thuế bao gồm phụ thu và phí thu thêm mà cơ sở kinh doanh được hưởng; khoản thu không liên quan đến bán hàng hóa/dịch vụ không tính vào giá; chiết khấu thương mại dùng giá bán đã chiết khấu.
- Trong phạm vi Điều 5–14, chưa xác định một điều riêng hướng dẫn giá tính thuế cho bán trả chậm/trả góp. Nội dung này và quan hệ với quy định của Luật 48 vẫn cần kiểm tra khi gặp đúng nghiệp vụ. Nội dung về ủy thác và chứng khoán được nhận diện ở các nhóm quy định khác, chưa xác định là một công thức giá tính thuế riêng có thể áp dụng chung cho Case 3.

Hệ quả đối với Case 3: `taxable_amount` chỉ có thể được coi là căn cứ của phép nhân sau khi biết field này đã phản ánh đúng giá chưa thuế hoặc đúng cách xác định giá tính thuế đặc thù. Việc parser đổi tên `net_amount` sang `taxable_amount` không tự xác minh được điều kiện pháp lý đó.

### 12.3. Thuế suất — Điều 9 Luật 48

- **Điều 17** quy định chi tiết phạm vi mức thuế suất 0% và các trường hợp không áp dụng 0%; **Điều 18** quy định điều kiện áp dụng 0%, gồm yêu cầu khác nhau theo loại giao dịch; **Điều 19** quy định chi tiết các nhóm áp dụng mức 5%.
- Các điều này ảnh hưởng trực tiếp tới ý nghĩa của `vat_rate`: mức thuế suất không thể được xác nhận chỉ bằng việc giá trị đầu vào có dạng số hợp lệ; còn phải phân loại đúng hàng hóa/dịch vụ và đáp ứng điều kiện tương ứng.
- Với dữ liệu có nhiều dòng hoặc nhiều mức thuế suất, Case 3 cần ưu tiên kiểm tra ở cấp dòng. Review này chưa xác định trong Điều 17–19 một quy tắc tổng quát cho phép dùng một `vat_rate` duy nhất để kiểm tra mọi hóa đơn có nhiều mức thuế suất.

### 12.4. Phương pháp khấu trừ và giới hạn của công thức

- **Khoản 1 Điều 20:** số thuế GTGT phải nộp theo phương pháp khấu trừ bằng thuế GTGT đầu ra trừ thuế GTGT đầu vào được khấu trừ.
- **Khoản 2 Điều 20:** thuế GTGT đầu ra là tổng số thuế trên hóa đơn GTGT bán ra; số thuế trên hóa đơn được xác định bằng giá tính thuế nhân thuế suất. Nếu hóa đơn chỉ ghi giá thanh toán đã có thuế thì số thuế đầu ra bằng giá thanh toán trừ giá tính thuế được quy đổi theo khoản 2 Điều 9.
- **Khoản 3 Điều 20:** thuế GTGT đầu vào được khấu trừ phụ thuộc hóa đơn/chứng từ và điều kiện khấu trừ theo Chương III. Một mismatch số học không tự chứng minh thuế đầu vào không được khấu trừ.
- **Điều 21:** phương pháp khấu trừ chỉ áp dụng cho các cơ sở kinh doanh thuộc phạm vi và đáp ứng điều kiện về kế toán, hóa đơn, chứng từ được quy định tại điều này.
- **Điều 22:** phương pháp trực tiếp đối với vàng, bạc, đá quý dùng giá trị gia tăng nhân thuế suất; giá trị gia tăng là chênh lệch giữa giá thanh toán bán ra và giá thanh toán mua vào, đều là giá đã có thuế. Đây là ví dụ trực tiếp cho thấy phép nhân `taxable_amount × vat_rate` không phù hợp nếu dữ liệu thuộc phương pháp khác hoặc field không mang đúng ý nghĩa pháp lý.

Vì vậy, Case 3 phù hợp hơn với dữ liệu hóa đơn GTGT đầu ra theo phương pháp khấu trừ, ở cấp dòng hoặc tập dữ liệu đã xác định đúng giá tính thuế và thuế suất. Chưa nên áp dụng rộng cho dữ liệu theo phương pháp trực tiếp hoặc dữ liệu chưa nhận diện được phương pháp tính thuế.

### 12.5. Ảnh hưởng tới wording và rule

- **Công thức lõi:** chưa xác định thấy cần đổi phép so sánh `taxable_amount × vat_rate ≈ vat_amount` chỉ do Nghị định 181; khoản 2 Điều 20 trực tiếp hỗ trợ phép tính này trong phạm vi nêu trên. Tolerance `1.0` vẫn chỉ là tham số kỹ thuật, không phải ngưỡng pháp luật.
- **Phạm vi rule:** cần cân nhắc bổ sung điều kiện nhận diện phương pháp khấu trừ/hóa đơn GTGT đầu ra và các trường hợp cần quy đổi hoặc xác định giá tính thuế riêng trước khi mở rộng Case 3. Đây là khuyến nghị sau review, không phải thay đổi code trong phiên này.
- **Wording:** cần giữ ở mức cảnh báo dữ liệu và bổ sung yêu cầu xác minh phương pháp tính thuế, giá tính thuế, giá đã bao gồm thuế, chiết khấu/khuyến mại và dòng hàng. Wording tại Mục 6 đã được chỉnh thận trọng hơn. Không được suy diễn mismatch thành sai phạm, gian lận hoặc mất quyền khấu trừ.
- **Dashboard/API:** chưa sửa code hoặc nội dung triển khai trong phiên này. Trước khi sửa sản phẩm, cần xác nhận các ngoại lệ, thiết kế dữ liệu và văn bản sửa đổi hiện hành.

### 12.6. Điểm còn Pending và kết luận thận trọng

- Chưa rà sâu toàn bộ từng khoản của Điều 5–14 và Điều 17–19 trên hình ảnh bản ký; đã đọc các phần trọng yếu và đối chiếu cấu trúc/nội dung bằng trang toàn văn chính thức.
- Chưa xác minh đầy đủ cách xử lý trả chậm/trả góp, ủy thác, chứng khoán, hóa đơn điều chỉnh/thay thế, làm tròn và trường hợp nhiều mức thuế suất trong cấu trúc dữ liệu thực tế của TaxGPT.
- Chưa rà sạch Nghị định 359/2025/NĐ-CP và Nghị định 144/2026/NĐ-CP, nên chưa chốt tình trạng áp dụng hiện hành của toàn bộ nội dung Nghị định 181 tại ngày review.
- Chưa có independent legal review và chưa có cross review bởi Thế Anh/Khánh/người khác.
- Review này chưa làm Case 3 hoàn tất pháp lý và không phải căn cứ để kết luận sai phạm. **Legal confidence vẫn `Pending`.**
- Chưa đủ điều kiện mở dữ liệu pháp lý cho hệ thống sinh giải thích. **RAG/AI explanation vẫn `LOCKED`.**
