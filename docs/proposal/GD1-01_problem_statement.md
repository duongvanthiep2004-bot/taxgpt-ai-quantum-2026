# GD1-01 — Mô tả vấn đề TaxGPT

## 1. Bối cảnh

Quá trình chuyển đổi số đang làm thay đổi cách doanh nghiệp nhỏ và hộ kinh doanh quản lý hóa đơn, chứng từ và hồ sơ thuế. Hóa đơn điện tử ngày càng phổ biến, trong khi chứng từ thanh toán, bảng kê, tờ khai và dữ liệu đối soát cũng được tạo ra với số lượng lớn hơn. Dữ liệu số giúp việc lưu trữ và trao đổi thuận tiện hơn, nhưng đồng thời làm tăng nhu cầu kiểm tra tính đầy đủ, chính xác và nhất quán giữa nhiều nguồn thông tin.

Đối với một đơn vị quy mô nhỏ, mỗi kỳ kê khai có thể liên quan đến nhiều hóa đơn đầu vào, đầu ra và chứng từ thanh toán đi kèm. Một sai lệch nhỏ về thông tin người mua, số tiền hoặc thời điểm ghi nhận có thể không được phát hiện ngay nếu dữ liệu chỉ được kiểm tra bằng mắt hoặc qua các bảng tính rời rạc.

Trong khi đó, nhiều doanh nghiệp nhỏ và hộ kinh doanh chưa có bộ phận chuyên trách về thuế. Công việc thường do kế toán nội bộ kiêm nhiệm hoặc được giao cho dịch vụ kế toán bên ngoài. Nguồn lực hạn chế khiến việc rà soát chuyên sâu trước khi kê khai, quyết toán hoặc chuẩn bị hồ sơ giải trình chưa phải lúc nào cũng được thực hiện đầy đủ.

## 2. Vấn đề thực tế

Dữ liệu phục vụ kiểm tra thuế thường nằm rải rác trong nhiều định dạng như XML của hóa đơn điện tử, PDF, Excel, ảnh scan và sao kê ngân hàng. Mỗi định dạng có cấu trúc khác nhau, nên người dùng phải mở nhiều file, đọc từng trường dữ liệu và tự liên kết các thông tin có liên quan. Việc tổng hợp này mất thời gian và khó duy trì nhất quán khi số lượng chứng từ tăng.

Kiểm tra thủ công cũng dễ bị ảnh hưởng bởi áp lực thời gian, thao tác lặp lại và sự khác biệt về kinh nghiệm của người thực hiện. Những lỗi như ghi nhận trùng hóa đơn, sai thông tin người mua hoặc chênh lệch phép tính thuế có thể bị bỏ sót. Một lỗi nhỏ chưa chắc đồng nghĩa với vi phạm, nhưng có thể tạo ra rủi ro khi kê khai, quyết toán hoặc giải trình nếu không được phát hiện và làm rõ kịp thời.

Người dùng không chuyên còn gặp khó khăn khi muốn đối chiếu dấu hiệu bất thường với căn cứ pháp lý liên quan. Văn bản có thể dài, được sửa đổi theo thời gian và cần được đặt trong đúng bối cảnh nghiệp vụ. Vì vậy, việc tìm thấy một điều khoản chưa đủ để tự đưa ra kết luận; người dùng vẫn cần biết nội dung nào cần kiểm chứng và cần chuẩn bị thêm chứng từ gì.

Các công cụ kế toán và kê khai hiện có hỗ trợ tốt việc nhập liệu, lập báo cáo hoặc gửi tờ khai. Tuy nhiên, nhu cầu rà soát rủi ro chủ động trước khi nộp hồ sơ hoặc trước khi lưu trữ chứng từ vẫn còn dư địa để cải thiện. Người dùng cần một lớp kiểm tra bổ sung, có khả năng tổng hợp dữ liệu, chỉ ra dấu hiệu bất thường và giải thích cảnh báo theo cách dễ hiểu.

## 3. Nhóm người dùng bị ảnh hưởng

- **Doanh nghiệp nhỏ và vừa:** thường có khối lượng chứng từ đủ lớn để việc kiểm tra thủ công trở nên tốn thời gian, nhưng chưa chắc có nguồn lực xây dựng bộ phận thuế chuyên sâu.
- **Hộ kinh doanh chuyển đổi sang sử dụng hóa đơn điện tử:** cần làm quen với quy trình số hóa, lưu trữ và đối chiếu dữ liệu trong khi kinh nghiệm về công cụ hoặc nghiệp vụ có thể còn hạn chế.
- **Kế toán nội bộ:** cần rà soát nhiều loại chứng từ trong thời gian ngắn và cần một công cụ hỗ trợ phát hiện sớm các điểm đáng chú ý.
- **Dịch vụ kế toán, đại lý thuế quy mô nhỏ:** xử lý dữ liệu của nhiều khách hàng và cần chuẩn hóa bước kiểm tra ban đầu trước khi chuyên gia xem xét.
- **Sinh viên và người học nghiệp vụ thuế:** cần môi trường mô phỏng để hiểu cách phát hiện rủi ro, đọc lý do cảnh báo và thực hành quy trình kiểm tra chứng từ.

## 4. Các rủi ro MVP cần giải quyết

### 4.1. Hóa đơn trùng

- **Rủi ro xảy ra như thế nào:** Cùng một hóa đơn có thể được nhập hoặc tải lên nhiều lần từ các nguồn khác nhau, dẫn đến nguy cơ ghi nhận trùng trong tập dữ liệu.
- **Vì sao dễ bỏ sót:** Tên file có thể khác nhau, dữ liệu được tổng hợp qua nhiều đợt hoặc nhiều người cùng thao tác nên bản ghi trùng không luôn nằm cạnh nhau.
- **Mức hỗ trợ của TaxGPT:** So sánh các trường nhận diện như mẫu số, ký hiệu, số hóa đơn, mã số thuế, ngày lập và giá trị để cảnh báo bản ghi có khả năng trùng. Người dùng vẫn cần xác nhận đó là dữ liệu lặp hay các chứng từ riêng biệt.

### 4.2. Sai mã số thuế hoặc tên người mua

- **Rủi ro xảy ra như thế nào:** Thông tin người mua trên hóa đơn có thể khác với hồ sơ doanh nghiệp do nhập sai, thiếu ký tự, dùng tên viết tắt không phù hợp hoặc chọn nhầm đơn vị.
- **Vì sao dễ bỏ sót:** Mã số thuế là chuỗi số dài, tên doanh nghiệp có thể gần giống nhau và người kiểm tra thường phải đối chiếu giữa nhiều nguồn dữ liệu.
- **Mức hỗ trợ của TaxGPT:** Đối chiếu thông tin trên hóa đơn với hồ sơ tham chiếu do người dùng cung cấp, sau đó đánh dấu trường không khớp hoặc có dấu hiệu bất thường. Cảnh báo chỉ hỗ trợ rà soát và không tự xác nhận giá trị pháp lý của hóa đơn.

### 4.3. VAT không khớp phép tính

- **Rủi ro xảy ra như thế nào:** Tiền thuế VAT trên hóa đơn có thể không khớp với giá trị tính thuế và thuế suất được ghi nhận, hoặc tổng tiền không nhất quán với các thành phần chi tiết.
- **Vì sao dễ bỏ sót:** Hóa đơn có nhiều dòng hàng, nhiều mức thuế suất, quy tắc làm tròn hoặc điều chỉnh khiến việc tính lại thủ công tốn thời gian.
- **Mức hỗ trợ của TaxGPT:** Thực hiện lại các phép tính theo dữ liệu trên chứng từ, áp dụng sai số làm tròn được cấu hình và cảnh báo chênh lệch. Hệ thống chỉ phát hiện bất nhất số học; trường hợp nghiệp vụ đặc thù vẫn cần người có chuyên môn xem xét.

### 4.4. Hóa đơn đầu vào ngoài kỳ kê khai

- **Rủi ro xảy ra như thế nào:** Ngày lập hóa đơn, thời điểm tiếp nhận hoặc kỳ ghi nhận có thể không nhất quán với kỳ kê khai đang được rà soát.
- **Vì sao dễ bỏ sót:** Dữ liệu có thể được nhận muộn, bổ sung qua nhiều đợt hoặc nằm trong các bảng kê khác nhau; người dùng phải đối chiếu đồng thời nhiều mốc thời gian.
- **Mức hỗ trợ của TaxGPT:** So sánh các mốc ngày và kỳ dữ liệu để phát hiện hóa đơn cần được kiểm tra thêm về thời điểm kê khai. Hệ thống không tự kết luận hóa đơn được hay không được kê khai; người dùng phải đối chiếu căn cứ pháp lý liên quan và tình huống thực tế.

### 4.5. Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt

- **Rủi ro xảy ra như thế nào:** Một hóa đơn đạt ngưỡng giá trị cần theo dõi nhưng chưa tìm thấy chứng từ thanh toán không dùng tiền mặt tương ứng trong dữ liệu đã tải lên.
- **Vì sao dễ bỏ sót:** Hóa đơn và chứng từ thanh toán thường được lưu ở hai hệ thống khác nhau; nội dung chuyển khoản có thể không ghi rõ số hóa đơn hoặc một khoản thanh toán có thể liên quan đến nhiều chứng từ.
- **Mức hỗ trợ của TaxGPT:** Dùng ngưỡng do hệ thống hoặc người dùng cấu hình để lọc hóa đơn cần đối chiếu, sau đó tìm liên kết với sao kê hoặc chứng từ thanh toán và cảnh báo khi chưa tìm thấy bằng chứng phù hợp. “Chưa tìm thấy” không đồng nghĩa với “không tồn tại” hoặc kết luận sai phạm; người dùng cần kiểm tra hồ sơ gốc và văn bản pháp luật cần được kiểm chứng.

## 5. Vì sao cần giải pháp AI

AI có khả năng hỗ trợ đọc và trích xuất thông tin từ nhiều định dạng dữ liệu khác nhau, qua đó giảm bớt thao tác nhập lại và giúp đưa các nguồn chứng từ về cấu trúc có thể đối chiếu. Với những điều kiện rõ ràng như nhận diện bản ghi trùng, so sánh trường dữ liệu hoặc kiểm tra phép tính, rule engine giúp kết quả có logic minh bạch và dễ kiểm tra lại.

Đối với phần thông tin pháp lý, kỹ thuật RAG có thể truy xuất các đoạn văn bản liên quan từ kho tài liệu đã được chuẩn bị, kèm nguồn để người dùng tự đối chiếu. Cách tiếp cận này giúp cảnh báo có thêm ngữ cảnh nhưng vẫn đòi hỏi nguồn tài liệu và nội dung trích xuất phải được kiểm chứng.

Giao diện hỏi đáp có thể chuyển một kết quả kỹ thuật thành phần giải thích gần với ngôn ngữ nghiệp vụ: hệ thống phát hiện điều gì, dữ liệu nào tạo ra cảnh báo và người dùng nên kiểm tra tiếp ở đâu. Sự kết hợp giữa AI, rule engine và RAG phù hợp với bài toán hỗ trợ rà soát, nhưng không thay thế đánh giá của kế toán, kiểm toán, luật sư, đại lý thuế hoặc cơ quan có thẩm quyền. Quyết định pháp lý cuối cùng luôn thuộc về con người và các chủ thể có thẩm quyền.

## 6. Phạm vi vấn đề trong MVP

MVP của TaxGPT chỉ tập trung vào năm nhóm rủi ro đã chọn: hóa đơn trùng; sai mã số thuế hoặc tên người mua; VAT không khớp phép tính; hóa đơn đầu vào ngoài kỳ kê khai; và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt.

Phiên bản này chưa xử lý toàn bộ nghiệp vụ thuế Việt Nam, chưa bao quát mọi loại chứng từ và không hướng tới kết luận đúng hoặc sai về mặt pháp lý một cách tuyệt đối. Với mỗi trường hợp, TaxGPT chỉ cung cấp cảnh báo, mức độ rủi ro tham khảo, lý do phát hiện và gợi ý bước kiểm tra tiếp theo. Các tình huống ngoại lệ, dữ liệu thiếu hoặc căn cứ pháp lý chưa được kiểm chứng phải được chuyển cho người có chuyên môn đánh giá.

Việc giới hạn phạm vi giúp nhóm tập trung xây dựng một prototype có thể kiểm thử và trình diễn rõ ràng, đồng thời tạo nền tảng để mở rộng sau khi độ chính xác, dữ liệu và quy trình kiểm chứng được đánh giá đầy đủ.

## 7. Kết luận

TaxGPT hướng tới nhu cầu thực tế về phát hiện sớm rủi ro thuế trong quá trình xử lý hóa đơn và chứng từ. Bằng cách hỗ trợ tổng hợp dữ liệu, tự động hóa các bước kiểm tra lặp lại và giải thích dấu hiệu bất thường, giải pháp có thể giúp người dùng giảm thao tác thủ công, hạn chế bỏ sót và chuẩn bị hồ sơ giải trình có hệ thống hơn. Hướng tiếp cận này gắn trực tiếp với nhóm chủ đề **AI cho Quản trị Rủi ro và Tuân thủ**. Phạm vi năm case cụ thể, kết quả có thể kiểm tra lại và giới hạn trách nhiệm rõ ràng giúp TaxGPT phù hợp để phát triển thành prototype trong khuôn khổ AI-Quantum Challenge 2026.
