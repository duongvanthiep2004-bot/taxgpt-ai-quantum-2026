# GD1.5-P — AI-assisted legal verification draft for 5 MVP cases

Ngày lập bản nháp: 18/08/2026.

**Nguồn tạo:** VSCode AI theo prompt điều phối của ChatGPT Plus.

**Tình trạng rà soát độc lập:** Chưa có Khánh/Gemini Pro hoặc người có chuyên môn rà soát độc lập.

**Mức tin cậy:** Nhãn High/Medium/Low là đánh giá sơ bộ của AI, không phải xác nhận pháp lý cuối cùng.

## Cảnh báo phạm vi

- Tài liệu này là bản nháp hỗ trợ kiểm chứng pháp lý bằng AI, không phải ý kiến hoặc tư vấn pháp lý chính thức.
- Nội dung chưa thay thế việc rà soát của Khánh hoặc người có chuyên môn về thuế, hóa đơn và chứng từ.
- Tài liệu chưa được dùng để kết luận nghĩa vụ thuế, tình trạng pháp lý của hóa đơn hoặc hậu quả pháp lý đối với người dùng.
- Các rule chỉ nhận diện dữ liệu có dấu hiệu cần rà soát; luôn cần kiểm tra thêm hóa đơn, chứng từ, hồ sơ và bối cảnh giao dịch.
- Tài liệu chỉ phục vụ chuẩn bị RAG và xây dựng câu chữ an toàn. RAG pháp lý vẫn bị khóa cho tới khi nguồn, phiên bản văn bản và cách diễn giải được người có chuyên môn xác nhận.
- Mức tự tin dưới đây phản ánh mức độ liên quan giữa điều khoản dự kiến và rule kỹ thuật, không phản ánh mức chắc chắn của một kết luận pháp lý.
- Tài liệu này là legal draft, chưa phải kiểm chứng pháp lý hoàn tất. Không điều/khoản nào trong bản nháp được coi là đã xác nhận cuối cùng nếu chưa có bằng chứng đối chiếu trực tiếp nguyên văn và rà soát độc lập.

## Tình trạng nguồn được đối chiếu sơ bộ

- Đã xác nhận trên Cổng văn bản Chính phủ sự tồn tại, ngày hiệu lực và tệp văn bản gốc của Luật Thuế GTGT số 48/2024/QH15, Nghị định 181/2025/NĐ-CP, Nghị định 254/2026/NĐ-CP và Thông tư 91/2026/TT-BTC.
- Luật số 48/2024/QH15 đã có văn bản sửa đổi và văn bản hợp nhất. Văn bản hợp nhất số 12/VBHN-VPQH ngày 06/02/2026 được ban hành trước Luật số 09/2026/QH16 ngày 24/04/2026, vì vậy chưa thể mặc nhiên xem văn bản hợp nhất này là nguồn cập nhật cuối cùng. Nghị định 181/2025/NĐ-CP cũng đã có văn bản sửa đổi. Trước khi ingest cần xác định bản đang có hiệu lực tại thời điểm áp dụng, không dùng riêng bản ban đầu như nguồn duy nhất.
- Với Nghị định 254/2026/NĐ-CP, bản nháp mới đối chiếu sơ bộ các nguyên tắc lập hóa đơn, thời điểm lập hóa đơn và nội dung hóa đơn tại Điều 8, Điều 9 và Điều 10.
- Với Thông tư 91/2026/TT-BTC, chưa hoàn tất đối chiếu trực tiếp từng điều khoản liên quan tới hóa đơn sai sót, điều chỉnh hoặc thay thế. Mọi dẫn chiếu cụ thể tới thông tư này hiện chỉ là đầu mục cần kiểm tra thêm.
- Nguồn chính thức cần tiếp tục đối chiếu gồm: Luật Thuế GTGT số 48/2024/QH15; Luật số 09/2026/QH16 sửa đổi một số luật thuế, trong đó có Luật Thuế GTGT; Nghị định 181/2025/NĐ-CP và các văn bản sửa đổi nếu liên quan; Nghị định 254/2026/NĐ-CP về hóa đơn điện tử, chứng từ điện tử; Thông tư 91/2026/TT-BTC.
- Quy tắc áp dụng cho toàn bộ dẫn chiếu chưa có bằng chứng rà nguyên văn trong file này: **Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest.**

## Bảng tổng hợp 5 case

| Case ID | Tên case | Văn bản pháp lý dự kiến | Điều/khoản cần kiểm tra | Mức tự tin | Có thể dùng cho RAG ngay chưa | Ghi chú |
|---|---|---|---|---|---|---|
| CASE_1_DUPLICATE_INVOICE | Hóa đơn trùng | Nghị định 254/2026/NĐ-CP; Thông tư 91/2026/TT-BTC | Dự kiến đối chiếu Điều 8, 9, 10 Nghị định 254 và quy định xử lý sai sót tại Thông tư 91. Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest. | low | no | Đây là duplicate-data risk, không phải kết luận hóa đơn vi phạm; phải loại trừ nhập lặp, điều chỉnh, thay thế, hủy và giao dịch định kỳ. |
| CASE_2_BUYER_INFO_MISMATCH | Sai MST/tên người mua | Nghị định 254/2026/NĐ-CP; Thông tư 91/2026/TT-BTC | Dự kiến đối chiếu Điều 10, phụ lục liên quan của Nghị định 254 và quy định xử lý sai sót tại Thông tư 91. Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest. | medium/conditional | conditional after independent legal review | Rule demo chưa đối chiếu thật với hồ sơ người mua chuẩn; phải thiết kế và xác minh nguồn dữ liệu chuẩn trước khi thành rule thật. |
| CASE_3_VAT_MISMATCH | VAT không khớp phép tính | Luật 48/2024/QH15, Luật 09/2026/QH16 và văn bản sửa đổi/hợp nhất; Nghị định 254/2026/NĐ-CP | Dự kiến đối chiếu điểm b khoản 1 Điều 11 Luật 48 và Điều 10 Nghị định 254. Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest. | high ở mức kỹ thuật-pháp lý sơ bộ | conditional after independent legal review | Chưa mở RAG và không kết luận sai thuế; phải xác minh công thức, thuế suất, giá tính thuế, chiết khấu, làm tròn, nhiều mức thuế suất, ngoại tệ và điều chỉnh. |
| CASE_4_OUT_OF_REVIEW_PERIOD | Hóa đơn có ngày lập ngoài kỳ dữ liệu đang rà soát | Luật 48/2024/QH15, Luật 09/2026/QH16 và văn bản sửa đổi/hợp nhất; Nghị định 254/2026/NĐ-CP | Dự kiến đối chiếu điểm đ khoản 1 Điều 14 Luật 48 và Điều 9 Nghị định 254. Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest. | medium/conditional | conditional after independent legal review | “Kỳ dữ liệu đang rà soát” không tự động là “kỳ kê khai thuế”; cần đối chiếu ngày lập, ngày nhận hóa đơn, kỳ khai và khai bổ sung. |
| CASE_5_MISSING_BANK_PAYMENT | Chưa tìm thấy chứng từ thanh toán không dùng tiền mặt trong dữ liệu được cung cấp | Luật 48/2024/QH15, Luật 09/2026/QH16 và văn bản sửa đổi/hợp nhất; Nghị định 181/2025/NĐ-CP cùng văn bản sửa đổi nếu liên quan | Dự kiến đối chiếu điểm b khoản 2 Điều 14 Luật 48 và Điều 26 Nghị định 181 cùng các sửa đổi. Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest. | low | no | Chỉ ghi nhận chưa tìm thấy chứng từ trong dữ liệu được cung cấp. Mọi ngưỡng hiện tại chỉ là ngưỡng cấu hình rà soát nội bộ/demo, không phải “ngưỡng pháp luật”. |

## Chi tiết từng case

### Case 1 — Hóa đơn trùng

#### 1. Mô tả rule trong TaxGPT

Rule nhóm các dòng có cùng số hóa đơn, ngày lập và tổng tiền; nếu dữ liệu có mã số thuế người bán hoặc ký hiệu hóa đơn thì các trường này cũng được dùng để so khớp. Nhóm có từ hai dòng trở lên được cảnh báo là có dấu hiệu trùng dữ liệu cần rà soát.

#### 2. Căn cứ pháp lý dự kiến

- Nghị định 254/2026/NĐ-CP, Điều 8, Điều 9 và Điều 10: cần đối chiếu nguyên tắc lập hóa đơn, thời điểm lập và các trường định danh/nội dung của hóa đơn.
- Thông tư 91/2026/TT-BTC: cần kiểm tra thêm điều khoản về xử lý hóa đơn điện tử có sai sót, điều chỉnh hoặc thay thế.
- Chưa tìm thấy căn cứ đủ chắc để suy ra rằng hai dòng dữ liệu giống nhau luôn phản ánh hai hóa đơn có cùng bản chất pháp lý.
- Các dẫn chiếu trên mới là hướng đối chiếu, chưa phải xác nhận điều/khoản cuối cùng. **Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest.**

#### 3. Ý nghĩa pháp lý ở mức an toàn

Dữ liệu có duplicate-data risk và cần đối chiếu để xác định đây là bản ghi được nhập lặp hay các hóa đơn/chứng từ có quan hệ điều chỉnh, thay thế, hủy hoặc phát sinh định kỳ. Đây không phải kết luận hóa đơn vi phạm. Cần kiểm tra hóa đơn điện tử gốc và lịch sử xử lý liên quan. Chưa đủ dữ liệu để kết luận.

#### 4. Điều kiện áp dụng

- Có số hóa đơn, ngày lập, tổng tiền và, nếu có, ký hiệu hóa đơn cùng mã số thuế người bán.
- Dữ liệu đã được chuẩn hóa định dạng ngày, số tiền và mã định danh.
- Có khả năng truy xuất mã cơ quan thuế, trạng thái hóa đơn và quan hệ với hóa đơn điều chỉnh/thay thế để kiểm tra thêm.

#### 5. Điều chưa chắc / cần người kiểm chứng

- Bộ khóa nào đủ để nhận diện một hóa đơn duy nhất theo Nghị định 254 và chuẩn dữ liệu áp dụng?
- Cách phân biệt dòng nhập lặp với hóa đơn điều chỉnh, thay thế, hủy hoặc giao dịch định kỳ?
- Điều khoản cụ thể trong Thông tư 91 điều chỉnh từng tình huống sai sót là gì?
- Rule có cần dùng mã của cơ quan thuế hoặc định danh hóa đơn khác không?

#### 6. Câu chữ an toàn cho Dashboard

- “Phát hiện các bản ghi có thông tin hóa đơn trùng nhau; có thể cần đối chiếu với hóa đơn điện tử gốc.”
- “Cần kiểm tra thêm trạng thái và quan hệ điều chỉnh/thay thế của các hóa đơn liên quan.”
- “Chưa đủ dữ liệu để kết luận nguyên nhân trùng.”

#### 7. Khuyến nghị cho RAG

- Có nên ingest không: chưa.
- Nguồn dự kiến: Điều 8, Điều 9, Điều 10 Nghị định 254/2026/NĐ-CP và điều xử lý sai sót tương ứng trong Thông tư 91/2026/TT-BTC sau khi kiểm chứng.
- Cách chunk: tách riêng theo từng điều; phần xử lý sai sót cần tách tiếp theo trường hợp điều chỉnh, thay thế và hủy nếu văn bản quy định riêng.
- Trạng thái: khóa case này, chưa đưa vào RAG cho tới khi người kiểm chứng xác nhận bộ khóa nhận diện và các ngoại lệ.

### Case 2 — Sai MST/tên người mua

#### 1. Mô tả rule trong TaxGPT

Trong dữ liệu demo hiện tại, rule nhận diện các dòng đã được gắn nhãn Case 2 và đưa thông tin mã số thuế, tên người mua cùng ghi chú vào evidence. Rule chưa thực hiện đối chiếu thật với hồ sơ chuẩn hoặc danh mục người mua đã xác minh.

#### 2. Căn cứ pháp lý dự kiến

- Nghị định 254/2026/NĐ-CP, Điều 10: cần đối chiếu các nội dung bắt buộc của hóa đơn, trong đó có thông tin người mua, và các trường hợp ngoại lệ tại phụ lục liên quan.
- Thông tư 91/2026/TT-BTC: cần kiểm tra thêm quy định xử lý khi thông tin người mua có sai sót.
- Cần kiểm tra chính xác yêu cầu áp dụng theo từng loại người mua, loại hóa đơn và loại giao dịch.
- Các dẫn chiếu trên mới là hướng đối chiếu, chưa phải xác nhận điều/khoản cuối cùng. **Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest.**

#### 3. Ý nghĩa pháp lý ở mức an toàn

Thông tin người mua có dấu hiệu cần đối chiếu với hồ sơ đăng ký, hợp đồng và dữ liệu giao dịch. Cần kiểm tra thêm trường hợp có hoặc không bắt buộc ghi đầy đủ thông tin người mua. Chưa đủ dữ liệu để kết luận.

#### 4. Điều kiện áp dụng

- Có tên người mua và mã số thuế hoặc mã định danh phù hợp với loại người mua.
- Có nguồn dữ liệu chuẩn đã được xác minh để so sánh.
- Biết loại hóa đơn, loại khách hàng và giao dịch có thuộc trường hợp ngoại lệ hay không.
- Dữ liệu được chuẩn hóa chữ hoa/thường, khoảng trắng, ký tự tiếng Việt và mã số thuế.

#### 5. Điều chưa chắc / cần người kiểm chứng

- Những trường hợp nào không bắt buộc ghi tên hoặc mã số thuế người mua theo Nghị định 254 và phụ lục?
- Sai tên nhưng đúng mã số thuế, hoặc ngược lại, cần xử lý theo điều khoản nào?
- Nguồn hồ sơ chuẩn nào được phép dùng để so sánh trong sản phẩm?
- Rule cần được thay thế thế nào để bỏ phụ thuộc vào nhãn demo?

#### 6. Câu chữ an toàn cho Dashboard

- “Thông tin người mua có dấu hiệu chưa khớp với dữ liệu đối chiếu; cần kiểm tra thêm hồ sơ liên quan.”
- “Có thể cần đối chiếu tên và mã số thuế người mua với hợp đồng hoặc nguồn dữ liệu đã xác minh.”
- “Chưa đủ dữ liệu để kết luận tình trạng của hóa đơn.”

#### 7. Khuyến nghị cho RAG

- Có nên ingest không: không ở thời điểm hiện tại; chỉ xem xét sau independent legal review.
- Nguồn dự kiến: Điều 10 và phụ lục liên quan của Nghị định 254/2026/NĐ-CP; điều xử lý sai sót tương ứng trong Thông tư 91/2026/TT-BTC.
- Cách chunk: tách nội dung người bán, người mua, các trường hợp ngoại lệ và từng phương án xử lý sai sót.
- Trạng thái: khóa ở thời điểm hiện tại; chỉ mở sau khi xác nhận ngoại lệ và có rule đối chiếu với dữ liệu chuẩn.

### Case 3 — VAT không khớp phép tính

#### 1. Mô tả rule trong TaxGPT

Trong dữ liệu demo, rule chọn các dòng đã được gắn nhãn Case 3, tính lại thuế GTGT bằng giá trị chưa thuế nhân với thuế suất và so sánh với số thuế trên dòng. Chênh lệch lớn hơn dung sai cấu hình mặc định 1 đồng được cảnh báo để rà soát.

#### 2. Căn cứ pháp lý dự kiến

- Luật Thuế GTGT số 48/2024/QH15, điểm b khoản 1 Điều 11: căn cứ dự kiến cho cách xác định thuế GTGT đầu ra từ giá tính thuế và thuế suất.
- Nghị định 254/2026/NĐ-CP, Điều 10: cần đối chiếu các trường giá tính thuế, thuế suất, tiền thuế và tổng thanh toán trên hóa đơn.
- Cần dùng phiên bản Luật Thuế GTGT hiện hành sau sửa đổi/hợp nhất và kiểm tra thêm quy định về làm tròn, giảm giá, chiết khấu, nhiều mức thuế suất và các trường hợp đặc thù.
- Các dẫn chiếu trên mới là hướng đối chiếu, chưa phải xác nhận điều/khoản cuối cùng. **Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest.**

#### 3. Ý nghĩa pháp lý ở mức an toàn

Số thuế trên dữ liệu có dấu hiệu chưa khớp với phép tính cấu hình và cần rà soát lại công thức, thuế suất, giá tính thuế, chiết khấu, cách làm tròn, nhiều mức thuế suất, ngoại tệ, điều chỉnh cùng nội dung hóa đơn. Chênh lệch kỹ thuật không phải kết luận đã tính sai thuế, không tự xác định nguyên nhân hoặc hệ quả pháp lý. Chưa đủ dữ liệu để kết luận.

#### 4. Điều kiện áp dụng

- Có giá tính thuế, thuế suất và số thuế ở cùng cấp chi tiết hoặc tổng hợp có thể so sánh.
- Thuế suất đã được xác định đúng cho hàng hóa, dịch vụ và thời điểm giao dịch.
- Dữ liệu phản ánh đúng chiết khấu, giảm giá, điều chỉnh, tiền tệ và quy tắc làm tròn.
- Dung sai là cấu hình kỹ thuật đã được phê duyệt, không được mô tả như một chuẩn pháp lý nếu chưa có căn cứ.

#### 5. Điều chưa chắc / cần người kiểm chứng

- Điểm b khoản 1 Điều 11 còn nguyên nội dung trong phiên bản luật có hiệu lực tại thời điểm giao dịch hay không?
- Quy tắc làm tròn áp dụng ở cấp dòng hay cấp hóa đơn và theo văn bản nào?
- Xử lý hóa đơn có nhiều thuế suất, ngoại tệ, giảm giá hoặc điều chỉnh ra sao?
- Dung sai 1 đồng có phù hợp cho từng nguồn dữ liệu hay chỉ là cấu hình demo?

#### 6. Câu chữ an toàn cho Dashboard

- “Số thuế có dấu hiệu chưa khớp với phép tính từ giá tính thuế và thuế suất; cần kiểm tra thêm.”
- “Có thể cần đối chiếu thuế suất, cách làm tròn và các khoản điều chỉnh trên hóa đơn.”
- “Chưa đủ dữ liệu để kết luận nguyên nhân chênh lệch.”

#### 7. Khuyến nghị cho RAG

- Có nên ingest không: không ở thời điểm hiện tại; chỉ xem xét sau independent legal review. Confidence `high` chỉ ở mức kỹ thuật-pháp lý sơ bộ và không mở khóa RAG.
- Nguồn dự kiến: điểm b khoản 1 Điều 11 của Luật Thuế GTGT hiện hành; Điều 10 Nghị định 254/2026/NĐ-CP; văn bản chính thức về thuế suất và làm tròn nếu có liên quan.
- Cách chunk: tách riêng giá tính thuế, thuế suất, công thức thuế đầu ra, nội dung hóa đơn và các trường hợp đặc thù.
- Trạng thái: vẫn khóa trong giai đoạn nháp. Dù có nhãn `high`, Case 3 chưa được ingest và không được mở RAG trước khi rà soát độc lập hoàn tất.

### Case 4 — Hóa đơn có ngày lập ngoài kỳ dữ liệu đang rà soát

#### 1. Mô tả rule trong TaxGPT

Trong dữ liệu demo, rule chọn các dòng đã được gắn nhãn Case 4 và so sánh tháng, năm của ngày lập hóa đơn với kỳ rà soát được truyền vào hoặc kỳ khai báo trong dữ liệu. Nếu khác kỳ, rule đưa ra cảnh báo kỹ thuật.

#### 2. Căn cứ pháp lý dự kiến

- Luật Thuế GTGT số 48/2024/QH15, điểm đ khoản 1 Điều 14: cần đối chiếu quy định về thời điểm kê khai, khấu trừ thuế GTGT đầu vào và cách xử lý sai sót, thiếu sót.
- Nghị định 254/2026/NĐ-CP, Điều 9: cần đối chiếu thời điểm lập hóa đơn theo từng loại hoạt động.
- Cần kiểm tra phiên bản Luật Thuế GTGT hiện hành và các quy định quản lý thuế về kỳ khai, khai bổ sung hoặc thời điểm nhận hóa đơn.
- Các dẫn chiếu trên mới là hướng đối chiếu, chưa phải xác nhận điều/khoản cuối cùng. **Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest.**

#### 3. Ý nghĩa pháp lý ở mức an toàn

Ngày lập hóa đơn nằm ngoài kỳ dữ liệu đang rà soát nên có dấu hiệu cần đối chiếu với kỳ khai, thời điểm nhận hóa đơn và hồ sơ liên quan. Kỳ lọc dữ liệu nội bộ không tự động đồng nhất với kỳ thuế áp dụng. Chưa đủ dữ liệu để kết luận.

#### 4. Điều kiện áp dụng

- Có ngày lập hóa đơn hợp lệ và kỳ rà soát được xác định rõ.
- Biết kỳ rà soát là kỳ dữ liệu nội bộ hay kỳ khai thuế.
- Có thông tin về thời điểm nhận hóa đơn, thời điểm giao dịch và lịch sử khai hoặc khai bổ sung.
- Xác định đúng loại hàng hóa, dịch vụ để áp dụng quy định về thời điểm lập hóa đơn.

#### 5. Điều chưa chắc / cần người kiểm chứng

- Trường hợp nào ngày lập ngoài kỳ rà soát vẫn phù hợp với hồ sơ và kỳ khai?
- Quan hệ giữa ngày lập, ngày nhận hóa đơn, thời điểm phát sinh và thời điểm kê khai được xác định thế nào?
- Rule có cần so sánh ngày đầy đủ thay vì chỉ tháng, năm không?
- Cần tích hợp quy định quản lý thuế nào ngoài các văn bản GTGT và hóa đơn nêu trên?

#### 6. Câu chữ an toàn cho Dashboard

- “Ngày lập hóa đơn nằm ngoài kỳ dữ liệu đang rà soát; cần kiểm tra thêm kỳ khai và hồ sơ liên quan.”
- “Có thể cần đối chiếu thời điểm lập, thời điểm nhận hóa đơn và lịch sử kê khai.”
- “Chưa đủ dữ liệu để kết luận về cách xử lý thuế.”

#### 7. Khuyến nghị cho RAG

- Có nên ingest không: không ở thời điểm hiện tại; chỉ xem xét sau independent legal review.
- Nguồn dự kiến: điểm đ khoản 1 Điều 14 của Luật Thuế GTGT hiện hành; Điều 9 Nghị định 254/2026/NĐ-CP; quy định quản lý thuế liên quan sau khi xác định chính xác.
- Cách chunk: tách quy định về thời điểm lập theo loại giao dịch, thời điểm kê khai và xử lý sai sót/thiếu sót.
- Trạng thái: khóa cho tới khi người có chuyên môn xác nhận sự khác nhau giữa kỳ rà soát kỹ thuật và kỳ thuế.

### Case 5 — Hóa đơn giá trị lớn nhưng chưa tìm thấy chứng từ thanh toán không dùng tiền mặt trong dữ liệu được cung cấp

#### 1. Mô tả rule trong TaxGPT

Rule demo kiểm tra tham chiếu thanh toán trên các hóa đơn thuộc Case 5 với danh sách tham chiếu trong file giao dịch thanh toán. Nếu không tìm thấy tham chiếu khớp, rule cảnh báo rằng chưa tìm thấy chứng từ thanh toán không dùng tiền mặt trong dữ liệu được cung cấp. Nếu sử dụng mức giá trị để chọn hóa đơn, mức đó phải được gọi là ngưỡng cấu hình rà soát nội bộ/demo.

#### 2. Căn cứ pháp lý dự kiến

- Luật Thuế GTGT số 48/2024/QH15, điểm b khoản 2 Điều 14: căn cứ dự kiến về điều kiện có chứng từ thanh toán không dùng tiền mặt đối với hàng hóa, dịch vụ mua vào, kèm các trường hợp do Chính phủ quy định.
- Nghị định 181/2025/NĐ-CP, Điều 26 và các văn bản sửa đổi, gồm Nghị định 359/2025/NĐ-CP và Nghị định 144/2026/NĐ-CP: cần kiểm tra bản đang có hiệu lực, định nghĩa chứng từ, điều kiện áp dụng, ngưỡng giá trị, thời điểm thanh toán và ngoại lệ.
- Chưa xác minh đủ chắc nội dung hợp nhất để dùng một con số làm “ngưỡng pháp luật” trong rule hoặc Dashboard.
- Các dẫn chiếu trên mới là hướng đối chiếu, chưa phải xác nhận điều/khoản cuối cùng. **Cần kiểm tra trực tiếp nguyên văn điều/khoản trước khi ingest.**

#### 3. Ý nghĩa pháp lý ở mức an toàn

Hệ thống chưa tìm thấy chứng từ thanh toán không dùng tiền mặt trong dữ liệu được cung cấp nên có dấu hiệu cần rà soát thêm. Cần kiểm tra sao kê, ủy nhiệm chi, đối chiếu công nợ, hợp đồng và phương thức thanh toán thực tế. Việc không tìm thấy trong một tập dữ liệu không đồng nghĩa chứng từ không tồn tại; chưa đủ dữ liệu để kết luận.

#### 4. Điều kiện áp dụng

- Có tham chiếu đáng tin cậy để nối hóa đơn với giao dịch thanh toán; không chỉ dựa vào một trường tùy chọn nếu thực tế có nhiều phương thức đối chiếu.
- Có đủ dữ liệu thanh toán trong khoảng thời gian phù hợp, bao gồm giao dịch phát sinh sau ngày hóa đơn nếu điều kiện áp dụng cho phép.
- Xác định giá trị giao dịch, phương thức thanh toán và trường hợp trả chậm, trả góp, thanh toán từng phần hoặc thanh toán gộp.
- Kiểm tra các trường hợp bù trừ công nợ, thanh toán qua bên thứ ba, ủy quyền và ngoại lệ khác theo văn bản hiện hành.
- Mọi mức giá trị dùng trước khi pháp lý được xác nhận chỉ là ngưỡng cấu hình rà soát nội bộ/demo.

#### 5. Điều chưa chắc / cần người kiểm chứng

- Nội dung hiện hành của Điều 26 Nghị định 181 sau các lần sửa đổi là gì?
- Ngưỡng giá trị, cách cộng gộp theo ngày hoặc nhà cung cấp và thời điểm phải có chứng từ được áp dụng ra sao?
- Các loại chứng từ và phương thức thanh toán nào được chấp nhận trong từng trường hợp?
- Cách xử lý trả chậm, trả góp, thanh toán từng phần, thanh toán gộp, bù trừ công nợ và thanh toán qua bên thứ ba?
- Rule nối bằng `payment_ref` có đủ độ tin cậy hay cần kết hợp số tiền, ngày giao dịch, đối tác và nội dung chuyển khoản?

#### 6. Câu chữ an toàn cho Dashboard

- “Chưa tìm thấy chứng từ thanh toán không dùng tiền mặt trong dữ liệu được cung cấp; cần kiểm tra thêm hồ sơ thanh toán.”
- “Có thể cần đối chiếu hóa đơn với sao kê, ủy nhiệm chi, hợp đồng và công nợ liên quan.”
- “Chưa đủ dữ liệu để kết luận về điều kiện áp dụng hoặc tình trạng chứng từ.”

#### 7. Khuyến nghị cho RAG

- Có nên ingest không: chưa.
- Nguồn dự kiến: điểm b khoản 2 Điều 14 của Luật Thuế GTGT hiện hành; Điều 26 Nghị định 181/2025/NĐ-CP sau khi hợp nhất đầy đủ các sửa đổi; tài liệu chính thức giải thích ngoại lệ nếu được phê duyệt.
- Cách chunk: tách điều kiện chung, định nghĩa chứng từ, ngưỡng và cách xác định giá trị, trả chậm/trả góp, bù trừ, bên thứ ba và từng ngoại lệ.
- Trạng thái: khóa nghiêm ngặt; không đưa ngưỡng hoặc kết luận điều kiện thuế vào RAG trước khi người có chuyên môn xác nhận văn bản hợp nhất và logic nghiệp vụ.

## Independent review checklist

- [ ] Đã mở văn bản gốc từ Cổng văn bản Chính phủ.
- [ ] Đã xác nhận văn bản còn hiệu lực tại ngày áp dụng.
- [ ] Đã kiểm tra văn bản sửa đổi/hợp nhất.
- [ ] Đã xác định điều/khoản/điểm chính xác.
- [ ] Đã kiểm tra ngoại lệ.
- [ ] Đã có người chịu trách nhiệm rà soát cuối.
- [ ] Đã lưu bằng chứng rà soát.

## Open questions for human review

1. Tại ngày áp dụng cụ thể, chuỗi văn bản gồm Luật số 48/2024/QH15, Luật số 149/2025/QH15, Văn bản hợp nhất số 12/VBHN-VPQH và Luật số 09/2026/QH16 cần được đọc kết hợp như thế nào?
2. Nội dung Nghị định 181/2025/NĐ-CP sau Nghị định 359/2025/NĐ-CP và Nghị định 144/2026/NĐ-CP cần được hợp nhất như thế nào trước khi ingest?
3. Điều khoản nào của Thông tư 91/2026/TT-BTC áp dụng cho sai thông tin người mua, hóa đơn điều chỉnh và hóa đơn thay thế?
4. Bộ định danh nào đủ để phân biệt hóa đơn trùng với bản ghi nhập lặp, hóa đơn điều chỉnh hoặc hóa đơn thay thế?
5. Các ngoại lệ đối với thông tin người mua tại Điều 10 và phụ lục của Nghị định 254 áp dụng cho những loại giao dịch nào?
6. Quy tắc làm tròn, chiết khấu, nhiều thuế suất và ngoại tệ cần được mô hình hóa thế nào cho Case 3?
7. Kỳ rà soát nội bộ trong Case 4 phải được nối với kỳ khai thuế, ngày nhận hóa đơn và khai bổ sung như thế nào?
8. Điều kiện, ngưỡng giá trị và ngoại lệ thanh toán không dùng tiền mặt hiện hành cho Case 5 là gì? Có cần phân loại theo thời điểm giao dịch không?
9. Mỗi chunk RAG cần lưu metadata nào: số văn bản, điều, khoản, điểm, ngày hiệu lực, ngày hết hiệu lực, văn bản sửa đổi và loại giao dịch?
10. Ai là người phê duyệt cuối cùng cho từng case và bằng chứng phê duyệt được lưu ở đâu?

## Decision: RAG remains LOCKED for all 5 cases

- `CASE_1: LOCKED`
- `CASE_2: LOCKED`
- `CASE_3: LOCKED`
- `CASE_4: LOCKED`
- `CASE_5: LOCKED`

Case 3 vẫn `LOCKED`: nhãn High confidence chỉ là đánh giá kỹ thuật-pháp lý sơ bộ của AI; case này chưa được ingest.

| Case ID | Quyết định hiện tại | Điều kiện tối thiểu để mở khóa |
|---|---|---|
| CASE_1_DUPLICATE_INVOICE | LOCKED | Xác nhận bộ khóa nhận diện, quy định về sai sót/điều chỉnh/thay thế và các ngoại lệ nghiệp vụ. |
| CASE_2_BUYER_INFO_MISMATCH | LOCKED | Xác nhận Điều 10, phụ lục ngoại lệ, quy trình xử lý sai sót và nguồn dữ liệu người mua chuẩn. |
| CASE_3_VAT_MISMATCH | LOCKED | Xác nhận phiên bản luật hiện hành, công thức, thuế suất, làm tròn và phạm vi áp dụng; có thể ưu tiên kiểm chứng đầu tiên. |
| CASE_4_OUT_OF_REVIEW_PERIOD | LOCKED | Xác nhận quan hệ giữa kỳ rà soát kỹ thuật, kỳ khai thuế, ngày nhận hóa đơn và quy định khai bổ sung. |
| CASE_5_MISSING_BANK_PAYMENT | LOCKED | Xác nhận bản hợp nhất Điều 26, điều kiện, ngưỡng, thời điểm và toàn bộ ngoại lệ thanh toán liên quan. |

Quyết định chung: RAG pháp lý chưa được mở cho bất kỳ case nào. Các nhãn `conditional` trong bảng tổng hợp chỉ thể hiện khả năng chuẩn bị nguồn sau khi được kiểm chứng, không phải quyền ingest ngay.

## Nguồn chính thức đã đối chiếu sơ bộ

- Cổng văn bản Chính phủ: [Luật Thuế GTGT số 48/2024/QH15](https://vanban.chinhphu.vn/?docid=212476&pageid=27160) và tệp văn bản gốc.
- Cổng văn bản Chính phủ: [Luật số 149/2025/QH15](https://vanban.chinhphu.vn/?docid=216588&pageid=27160&typegroupid=3), [Văn bản hợp nhất số 12/VBHN-VPQH](https://vanban.chinhphu.vn/?docid=216941&pageid=27160) và [Luật số 09/2026/QH16](https://vanban.chinhphu.vn/?docid=218095&pageid=27160). Văn bản hợp nhất số 12 có trước Luật số 09 nên cần kiểm tra chuỗi sửa đổi thay vì dùng độc lập.
- Cổng văn bản Chính phủ: [Nghị định 181/2025/NĐ-CP](https://vanban.chinhphu.vn/?docid=214336&lang=vi&pageid=27160), [Nghị định 359/2025/NĐ-CP](https://vanban.chinhphu.vn/?classid=1&docid=216388&pageid=27160&typegroupid=4) và [Nghị định 144/2026/NĐ-CP](https://vanban.chinhphu.vn/?classid=1&docid=218020&pageid=27160).
- Cổng văn bản Chính phủ: [Nghị định 254/2026/NĐ-CP](https://vanban.chinhphu.vn/?docid=218689&pageid=27160&typegroupid=4) và [Thông tư 91/2026/TT-BTC](https://vanban.chinhphu.vn/?classid=1&docid=219006&orggroupid=4&pageid=27160).
- [Bài toàn văn Nghị định 254/2026/NĐ-CP trên Cổng Thông tin điện tử Chính phủ](https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-so-254-2026-nd-cp-ve-hoa-don-dien-tu-chung-tu-dien-tu-119260713164251972.htm) được dùng để đối chiếu sơ bộ Điều 8, Điều 9 và Điều 10.

Trước khi ingest, cần tải và lưu bản chính thức đã được phê duyệt, kiểm tra hiệu lực theo ngày giao dịch, lập manifest nguồn và gắn metadata đến cấp điều/khoản/điểm.
