# GD1-06 — Phản biện thử hồ sơ Vòng 1 TaxGPT

## 1. Đánh giá tổng quan

**Điểm tổng quan đề xuất: 7,4/10.**

TaxGPT phù hợp rõ với nhóm **AI cho Quản trị Rủi ro và Tuân thủ**, có phạm vi MVP cụ thể và cách phân vai giữa rule engine, RAG, AI và con người tương đối chặt chẽ. Hồ sơ có ưu điểm là không thổi phồng trạng thái sản phẩm và giữ ngôn ngữ pháp lý thận trọng. Tuy nhiên, phần chứng minh vấn đề còn thiên về lập luận hợp lý hơn là bằng chứng từ người dùng; điểm khác biệt so với phần mềm kế toán hiện có chưa đủ sắc; dữ liệu mẫu mới chứng minh được cách minh họa, chưa chứng minh độ chính xác hay khả năng xử lý ngoại lệ. Kiến trúc khả thi nếu thu hẹp demo, nhưng sẽ quá tham vọng nếu nhóm đồng thời cam kết XML, PDF/OCR, Excel, sao kê, năm rule, RAG và AI giải thích trong một prototype ngắn hạn.

Điểm trên là đánh giá thử theo tám khía cạnh được giao trong nhiệm vụ này, không phải điểm theo một bảng chấm chính thức chưa được cung cấp.

## 2. Điểm mạnh

1. **Đúng trọng tâm quản trị rủi ro và tuân thủ:** đầu ra là danh sách dấu hiệu cần rà soát, lý do cảnh báo và bước kiểm tra tiếp theo, không phải chức năng hạch toán hay lập tờ khai thông thường.
2. **Phạm vi MVP nhìn thấy được:** năm case đều có dữ liệu đầu vào, logic kiểm tra và cảnh báo kỳ vọng; ba case đầu đặc biệt phù hợp để triển khai rule minh bạch.
3. **Phân vai kỹ thuật hợp lý:** rule engine chịu trách nhiệm điều kiện xác định; RAG truy xuất nội dung; AI diễn giải; con người quyết định. Cách tách này có lợi cho truy vết và giảm ảo giác.
4. **Ngôn ngữ pháp lý tương đối an toàn:** hồ sơ không coi cảnh báo là kết luận vi phạm, không thay thế chuyên gia và không kết luận chắc chắn hậu quả về chi phí hoặc thuế.
5. **Trạng thái kỹ thuật được mô tả trung thực:** tài liệu phân biệt nền tảng đã có với parser, rule engine, kho RAG và Dashboard nghiệp vụ còn dự kiến.
6. **Có bộ dữ liệu demo nhất quán:** 12 hóa đơn, 6 giao dịch, mỗi case có hai dòng và có hai hóa đơn bình thường để đối chứng; dữ liệu được đánh dấu rõ là giả lập.
7. **Nhận diện rủi ro vận hành khá đầy đủ:** hồ sơ đã đề cập lỗi parser/OCR, cảnh báo nhầm, kho pháp lý chưa hoàn chỉnh, AI diễn giải quá chắc chắn, bảo mật dữ liệu và hiểu nhầm của người dùng.

## 3. Điểm yếu / rủi ro

1. **Nhu cầu người dùng chưa có bằng chứng trực tiếp.** Hồ sơ chưa nêu phỏng vấn, quan sát quy trình hoặc phản hồi từ doanh nghiệp nhỏ, hộ kinh doanh hay dịch vụ kế toán. Vì vậy, vấn đề có vẻ hợp lý nhưng chưa được xác nhận là đủ đau và đủ ưu tiên.
2. **Một số mô tả còn chung chung.** Các cụm như “dữ liệu ngày càng lớn”, “dễ bỏ sót” và “còn dư địa cải thiện” chưa cho giám khảo thấy quy trình hiện tại mất công ở đâu, ai chịu trách nhiệm và kết quả mong muốn được đo thế nào.
3. **Điểm khác biệt chưa tạo khoảng cách rõ với phần mềm hiện có.** Phát hiện trùng, kiểm tra trường và tính lại VAT có thể đã xuất hiện ở phần mềm hóa đơn hoặc kế toán. “Kết hợp rule engine + RAG + AI” là thiết kế hợp lý nhưng bản thân việc ghép công nghệ chưa đủ chứng minh tính mới.
4. **Vai trò thiết yếu của AI chưa thật thuyết phục.** Năm case MVP chủ yếu dựa trên rule và phép đối chiếu. Hồ sơ cần chỉ rõ AI tạo giá trị ở phần nào mà rule, bộ lọc hoặc giao diện truyền thống không làm tốt bằng, đồng thời không giao quyết định pháp lý cho AI.
5. **Kiến trúc có nguy cơ quá rộng.** Hỗ trợ XML, PDF/ảnh scan, Excel, sao kê, parser/OCR, năm rule, RAG, hỏi đáp, báo cáo và bảo mật là nhiều hạng mục. Nếu không công bố phạm vi demo tối thiểu, giám khảo có thể nghi ngờ khả năng hoàn thành.
6. **Dữ liệu mẫu quá sạch và quá ít để chứng minh chất lượng.** Hai dòng cho mỗi case đủ trình bày luồng nhưng chưa kiểm tra trường hợp biên, dữ liệu thiếu, hóa đơn điều chỉnh/thay thế, làm tròn, thanh toán nhiều lần hoặc liên kết mơ hồ.
7. **Chưa có tiêu chí đánh giá prototype.** Hồ sơ chưa nêu cách đo đúng/sai của rule, tỷ lệ cảnh báo nhầm, trường parser không đọc được, độ chính xác liên kết thanh toán hoặc tiêu chí đánh giá câu giải thích của AI.
8. **Case 2 phụ thuộc hồ sơ tham chiếu nhưng nguồn và quy trình quản lý chưa rõ.** Nếu người dùng cung cấp sai dữ liệu tham chiếu, cảnh báo có thể sai ngay từ đầu.
9. **Case 5 an toàn về câu chữ nhưng khó về dữ liệu và nghiệp vụ.** “Chưa tìm thấy chứng từ” có thể do thanh toán gộp, thanh toán từng phần, nội dung chuyển khoản không rõ hoặc dữ liệu chưa tải đủ. Rule ghép nối và cách trình bày độ tin cậy cần được giải thích.
10. **Kế hoạch demo chưa thành một kịch bản có đầu vào và kết quả đo được.** Hồ sơ có dữ liệu và kiến trúc, nhưng chưa nói rõ trong vài phút giám khảo sẽ nhìn thấy thao tác nào, cảnh báo nào và bằng chứng truy vết nào.

## 4. Câu hỏi giám khảo có thể hỏi

1. Nhóm đã nói chuyện với bao nhiêu doanh nghiệp nhỏ, hộ kinh doanh hoặc kế toán để xác nhận đây là vấn đề ưu tiên?
2. Một phần mềm kế toán hiện có cũng có thể phát hiện trùng và tính lại VAT; TaxGPT khác biệt thực chất ở đâu?
3. Nếu bỏ lớp AI, bao nhiêu phần trăm giá trị của MVP vẫn được rule engine thực hiện đầy đủ?
4. AI tham gia chính xác ở bước nào, và nhóm đo chất lượng phần giải thích của AI bằng cách nào?
5. Trong ngày demo, những module nào thực sự chạy được và những phần nào chỉ được minh họa bằng kiến trúc?
6. Nhóm ưu tiên định dạng đầu vào nào trước nếu không kịp hoàn thiện đồng thời XML, PDF/OCR, Excel và sao kê?
7. Với hóa đơn điều chỉnh, thay thế hoặc giao dịch định kỳ có thông tin gần giống nhau, rule chống trùng tránh cảnh báo nhầm ra sao?
8. Hồ sơ người mua tham chiếu cho case 2 lấy từ đâu, ai xác nhận và xử lý thế nào khi dữ liệu tham chiếu đã cũ hoặc sai?
9. `Tolerance` của kiểm tra VAT được cấu hình, kiểm thử và phê duyệt theo quy trình nào?
10. Với hóa đơn ngoài kỳ dữ liệu, hệ thống phân biệt “cần rà soát” với trường hợp nghiệp vụ hợp lệ như thế nào?
11. Case 5 xử lý thanh toán từng phần, thanh toán gộp nhiều hóa đơn hoặc nội dung chuyển khoản không có số hóa đơn ra sao?
12. Kho RAG gồm những loại tài liệu nào, ai kiểm chứng hiệu lực và làm sao ngăn tài liệu hết hiệu lực được dùng để giải thích?
13. Nếu RAG không tìm thấy nguồn đủ tin cậy hoặc các nguồn mâu thuẫn, TaxGPT sẽ trả lời thế nào?
14. Nhóm sẽ đo tỷ lệ cảnh báo đúng, cảnh báo nhầm và bỏ sót trên bộ kiểm thử nào ngoài 12 hóa đơn mẫu?
15. Dữ liệu hóa đơn và sao kê thật sẽ được mã hóa, lưu trong bao lâu, ai có quyền truy cập và người dùng xóa dữ liệu bằng cách nào?

## 5. Gợi ý chỉnh sửa bản GD1-05

| Vị trí / mục | Vấn đề | Mức độ ưu tiên | Gợi ý sửa |
|---|---|---|---|
| Mục 3–4: Tóm tắt và vấn đề | Nhu cầu đúng hướng nhưng chưa có bằng chứng từ người dùng. | Cao | Bổ sung một đoạn ngắn về số cuộc trao đổi/quan sát thực tế nếu nhóm có bằng chứng; nếu chưa có, ghi đây là giả thuyết cần kiểm chứng và đưa phỏng vấn người dùng vào kế hoạch gần nhất. |
| Mục 4: Bối cảnh | Mô tả “nhiều dữ liệu, dễ bỏ sót” còn chung. | Trung bình | Thêm một hành trình ngắn: người dùng nhận hóa đơn và sao kê ở hai nguồn, phải đối chiếu trường nào, TaxGPT rút ngắn bước nào. Không thêm số liệu chưa có nguồn. |
| Mục 10–11: Vai trò AI và khác biệt | Chưa trả lời dứt khoát vì sao cần AI thay vì chỉ có rule engine. | Cao | Nhấn mạnh rule tạo cảnh báo có thể kiểm thử; AI chỉ biến kết quả và nguồn đã kiểm chứng thành giải thích theo ngữ cảnh, hỏi đáp và hướng dẫn kiểm tra. Đừng lấy “dùng AI” làm điểm mới tự thân. |
| Mục 11: Tính mới | So sánh với phần mềm kế toán còn mang tính khái quát. | Cao | Chuyển trọng tâm khác biệt sang “lớp rà soát độc lập, cảnh báo có thể truy ngược, giải thích bị giới hạn nguồn và human review”; chỉ nêu so sánh sản phẩm cụ thể khi có khảo sát cạnh tranh. |
| Mục 7 và 12: Phạm vi, khả thi | Chưa chốt phiên bản demo tối thiểu nên kiến trúc dễ bị xem là quá tham vọng. | Cao | Nêu rõ demo ưu tiên dữ liệu Excel cấu trúc sẵn và năm rule; XML là bước kế tiếp, còn PDF/OCR và RAG hoàn chỉnh chỉ triển khai khi phần lõi đã ổn định. Điều chỉnh theo năng lực thật của nhóm. |
| Mục 9: Dữ liệu và demo | Bộ dữ liệu chỉ đủ minh họa, chưa phải bằng chứng chất lượng. | Cao | Thêm kế hoạch mở rộng test: dữ liệu bình thường, trường hợp biên, dữ liệu thiếu và ngoại lệ; công bố số ca test, kết quả đúng kỳ vọng, cảnh báo nhầm và bỏ sót khi đã chạy thật. |
| Mục 9 hoặc 14: Kế hoạch demo | Chưa có kịch bản demo 2–3 phút. | Trung bình | Viết chuỗi thao tác: tải bộ mẫu → chọn kỳ → chạy kiểm tra → mở một cảnh báo → xem trường kích hoạt và nguồn tham khảo → human review → xuất báo cáo. |
| Mục 8–10: RAG và AI | Một số câu có thể khiến người đọc tưởng kho RAG đã sẵn sàng. | Trung bình | Dùng nhất quán “dự kiến”; nói rõ chỉ nội dung pháp lý đã được con người kiểm chứng, có nguồn và trạng thái hiệu lực mới được đưa vào kho dùng cho giải thích. |
| Mục 13: Giới hạn | Đã nêu rủi ro nhưng chưa gắn với tiêu chí dừng an toàn. | Trung bình | Bổ sung: khi dữ liệu thiếu, parser có độ tin cậy thấp hoặc RAG không có nguồn phù hợp, hệ thống phải báo “chưa đủ dữ liệu/căn cứ” thay vì tạo giải thích chắc chắn. |
| Toàn bản | Bản master khoảng 2.343 từ, có lặp lại giới hạn trách nhiệm ở nhiều mục. | Thấp | Giữ bản master làm nguồn; sau khi biết cấu trúc Dashboard, tạo bản rút gọn theo từng trường và giữ một tuyên bố giới hạn rõ ở tóm tắt hoặc kết luận thay vì lặp dài. |

## 6. Những câu không nên nói khi thuyết trình

- “Hệ thống đảm bảo doanh nghiệp tuân thủ đúng pháp luật.”
- “AI có thể thay kế toán, luật sư, đại lý thuế hoặc cơ quan thuế.”
- “TaxGPT xác định hóa đơn này đúng hoặc sai.”
- “Cảnh báo này chứng minh có gian lận.”
- “Không tìm thấy chứng từ nghĩa là chứng từ không tồn tại.”
- “Hóa đơn bị cảnh báo chắc chắn làm chi phí hoặc thuế bị loại.”
- “RAG loại bỏ hoàn toàn ảo giác của AI.”
- “Kho pháp lý của chúng tôi đầy đủ và luôn cập nhật.”
- “TaxGPT đã xử lý tốt mọi loại XML, PDF, ảnh scan, Excel và sao kê.”
- “MVP đã hoàn thiện” khi parser, rule engine, RAG và Dashboard nghiệp vụ chưa được triển khai, kiểm thử đầy đủ.
- “Năm case này bao phủ rủi ro thuế của doanh nghiệp.”
- “Dữ liệu mẫu chứng minh hệ thống chính xác” khi mới chỉ có các tình huống được thiết kế để minh họa.

## 7. Bản pitch 60 giây đề xuất

Doanh nghiệp nhỏ và người làm kế toán thường phải đối chiếu hóa đơn, bảng tính và chứng từ thanh toán nằm ở nhiều nguồn. Kiểm tra thủ công tốn thời gian và dễ bỏ sót những điểm cần xem lại. TaxGPT được đề xuất như một lớp rà soát rủi ro trước khi kê khai hoặc lưu hồ sơ. MVP tập trung vào năm tình huống: hóa đơn nghi trùng, thông tin người mua không khớp, VAT lệch phép tính, hóa đơn ngoài kỳ dữ liệu và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt. Rule engine thực hiện các kiểm tra minh bạch; RAG dự kiến chỉ truy xuất nội dung pháp lý đã được kiểm chứng; AI giải thích cảnh báo bằng ngôn ngữ dễ hiểu. Người dùng luôn đối chiếu chứng từ gốc và quyết định bước tiếp theo. Nhóm đã có khung kỹ thuật và bộ dữ liệu giả lập 12 hóa đơn, 6 giao dịch để phát triển, kiểm thử prototype.

## 8. Kết luận

Hồ sơ **đủ điều kiện để nộp thử nội bộ**, nhưng chưa nên coi là bản tối ưu để dán lên Dashboard. Trước khi tạo bản rút gọn, nhóm nên ưu tiên bốn việc: xác minh ít nhất một số nhu cầu người dùng có bằng chứng; làm sắc điểm khác biệt so với phần mềm kế toán; chốt phạm vi demo thực sự có thể chạy; và bổ sung kế hoạch kiểm thử với tiêu chí đo kết quả. Nội dung pháp lý hiện an toàn ở cấp hồ sơ, trong đó case 5 không đưa kết luận tuyệt đối; việc cấu hình rule và giải thích chi tiết vẫn phải chờ đối chiếu nguồn gốc.

**GD1-06 có thể chốt `[x]` sau báo cáo này** vì đầu ra yêu cầu của nhiệm vụ phản biện đã được tạo: có điểm tổng quan, điểm mạnh, điểm yếu, 15 câu hỏi khó, bảng chỉnh sửa ưu tiên, danh sách câu cần tránh và pitch 60 giây. Việc sửa GD1-05 nên được thực hiện ở nhiệm vụ kế tiếp, không phải điều kiện để hoàn tất báo cáo phản biện.
