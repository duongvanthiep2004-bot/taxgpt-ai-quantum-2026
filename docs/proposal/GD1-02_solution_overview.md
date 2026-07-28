# GD1-02 — Mô tả giải pháp TaxGPT

## 1. Tổng quan giải pháp

TaxGPT là trợ lý AI hỗ trợ doanh nghiệp nhỏ, hộ kinh doanh và người làm kế toán rà soát sớm các dấu hiệu rủi ro trong hóa đơn, chứng từ và dữ liệu kế toán cơ bản. Giải pháp giúp tập hợp dữ liệu từ nhiều định dạng, thực hiện các bước kiểm tra lặp lại và trình bày cảnh báo theo cách dễ hiểu để người dùng biết nội dung nào cần xem xét thêm.

Trong phạm vi MVP, TaxGPT tập trung vào năm nhóm rủi ro thường gặp: hóa đơn có dấu hiệu trùng lặp; mã số thuế hoặc tên người mua không nhất quán; VAT không khớp logic tính toán; hóa đơn có ngày lập ngoài kỳ dữ liệu đang rà soát; và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt tương ứng.

Kết quả do TaxGPT cung cấp chỉ là cảnh báo rủi ro, lý do phát hiện và gợi ý kiểm tra tiếp theo. Hệ thống không tự kết luận một hóa đơn đúng hay sai về mặt pháp lý, không thay thế quyết định chuyên môn và không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế. Với định hướng đó, TaxGPT phù hợp với nhóm chủ đề **AI cho Quản trị Rủi ro và Tuân thủ**.

## 2. Đối tượng sử dụng

- **Doanh nghiệp nhỏ và vừa:** cần một lớp rà soát bổ sung trước khi kê khai, lưu trữ hoặc chuẩn bị hồ sơ giải trình nhưng chưa có bộ phận thuế chuyên sâu.
- **Hộ kinh doanh:** cần hỗ trợ làm quen với hóa đơn điện tử, dữ liệu số và quy trình đối chiếu chứng từ.
- **Kế toán nội bộ:** cần phát hiện nhanh các điểm bất thường trong khối lượng hóa đơn, bảng kê và chứng từ thanh toán ngày càng lớn.
- **Dịch vụ kế toán hoặc đại lý thuế quy mô nhỏ:** cần chuẩn hóa bước kiểm tra ban đầu trước khi chuyên gia đánh giá từng trường hợp.
- **Sinh viên và người học nghiệp vụ thuế:** cần công cụ mô phỏng quy trình rà soát, giải thích lý do cảnh báo và thực hành với dữ liệu mẫu.

## 3. Luồng xử lý chính

**Upload dữ liệu → Parser → Chuẩn hóa dữ liệu → Rule engine → RAG pháp lý → Cảnh báo rủi ro → Gợi ý kiểm tra → Xuất báo cáo**

1. **Upload dữ liệu:** Người dùng đưa hóa đơn XML, PDF, bảng Excel, sao kê hoặc chứng từ liên quan vào hệ thống. Trước khi xử lý, người dùng cần bảo đảm mình có quyền sử dụng dữ liệu và hạn chế đưa thông tin không cần thiết.
2. **Parser:** Hệ thống đọc tệp và trích xuất các trường phục vụ rà soát như số, ký hiệu và ngày hóa đơn; mã số thuế; tên người mua, người bán; giá trị trước thuế; thuế suất; tiền thuế; tổng tiền và thông tin thanh toán.
3. **Chuẩn hóa dữ liệu:** Dữ liệu từ các nguồn khác nhau được đưa về một cấu trúc thống nhất. Bước này giúp hệ thống so sánh các bản ghi và nhận biết trường còn thiếu hoặc chưa đọc được.
4. **Rule engine:** Các quy tắc rõ ràng kiểm tra năm case MVP. Mỗi cảnh báo có thể truy ngược về dữ liệu đầu vào và điều kiện đã kích hoạt, giúp người dùng kiểm tra lại kết quả.
5. **RAG pháp lý:** Hệ thống tìm kiếm nội dung liên quan trong kho tài liệu đã được chuẩn bị; chỉ nội dung đã qua kiểm chứng mới được dùng làm căn cứ giải thích cho cảnh báo. Nội dung truy xuất không tự tạo thành kết luận pháp lý.
6. **Cảnh báo rủi ro:** Kết quả được nhóm theo loại rủi ro và mức độ ưu tiên rà soát. Mức cảnh báo chỉ hỗ trợ sắp xếp công việc, không phải mức xử phạt hoặc phán quyết pháp lý.
7. **Gợi ý kiểm tra:** TaxGPT đề xuất hồ sơ, trường dữ liệu hoặc tình huống người dùng cần đối chiếu thêm, đồng thời chỉ rõ khi dữ liệu chưa đủ để đánh giá.
8. **Xuất báo cáo:** Hệ thống tạo bản tóm tắt gồm dấu hiệu phát hiện, dữ liệu liên quan, lý do cảnh báo và bước kiểm tra tiếp theo để lưu trữ hoặc phục vụ rà soát nội bộ.

## 4. Các chức năng MVP

### 4.1. Phát hiện hóa đơn trùng

- **Mục tiêu:** Nhận diện những hóa đơn có khả năng bị nhập, tải lên hoặc ghi nhận nhiều lần trong tập dữ liệu.
- **Dữ liệu cần kiểm tra:** Số và ký hiệu hóa đơn, mã số thuế người bán/người mua, ngày lập, tổng tiền và các trường nhận diện liên quan.
- **Cảnh báo đầu ra:** Hiển thị các bản ghi nghi trùng, trường dữ liệu trùng khớp và lý do tạo cảnh báo. Người dùng phải xác minh đó là dữ liệu lặp, bản sao, hóa đơn điều chỉnh/thay thế hay các giao dịch riêng biệt. TaxGPT không kết luận gian lận.

### 4.2. Kiểm tra sai MST hoặc tên người mua

- **Mục tiêu:** Phát hiện thông tin người mua không khớp với hồ sơ tham chiếu do người dùng cung cấp.
- **Cách phân biệt:** Trường hợp mã số thuế không khớp được tách riêng khỏi trường hợp mã số thuế đúng nhưng tên hoặc địa chỉ có sai lệch nhỏ. Cách phân loại này giúp người dùng ưu tiên rà soát mà không đánh đồng mọi khác biệt.
- **Cảnh báo đầu ra:** Nêu rõ trường không khớp, giá trị trên hóa đơn và giá trị tham chiếu. Hệ thống không tự kết luận hóa đơn vô hiệu, không có giá trị hoặc không được kê khai.

### 4.3. Kiểm tra VAT không khớp phép tính

- **Mục tiêu:** Phát hiện chênh lệch số học giữa tiền hàng, thuế suất, tiền thuế và tổng tiền được thể hiện trong dữ liệu hóa đơn.
- **Cách kiểm tra:** Hệ thống tính lại các giá trị từ trường dữ liệu đã trích xuất và so sánh với số liệu trên chứng từ. Các hóa đơn có nhiều dòng hàng, nhiều mức thuế suất hoặc nghiệp vụ đặc thù cần được xử lý theo cấu trúc dữ liệu phù hợp.
- **Cảnh báo đầu ra:** Hiển thị giá trị gốc, giá trị tính lại và mức chênh lệch. `Tolerance` là tham số kỹ thuật để xử lý làm tròn hoặc khác biệt giữa hệ thống, không phải ngưỡng sai số được pháp luật mặc nhiên chấp nhận.

### 4.4. Kiểm tra hóa đơn ngoài kỳ dữ liệu đang rà soát

- **Mục tiêu:** Phát hiện hóa đơn có ngày lập nằm ngoài khoảng thời gian của kỳ dữ liệu người dùng đang kiểm tra.
- **Cách kiểm tra:** Hệ thống so sánh ngày hóa đơn với kỳ rà soát được chọn và đưa các trường hợp lệch kỳ vào danh sách cần xem xét.
- **Cảnh báo đầu ra:** Gợi ý người dùng kiểm tra lại kỳ kê khai, thời điểm tiếp nhận chứng từ hoặc khả năng kê khai bổ sung theo tình huống thực tế. TaxGPT không kết luận trường hợp đó là vi phạm, không hợp lệ hoặc không được kê khai.

### 4.5. Kiểm tra hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt

- **Mục tiêu:** Hỗ trợ đối chiếu hóa đơn giá trị lớn với sao kê hoặc chứng từ thanh toán không dùng tiền mặt có liên quan trong dữ liệu được cung cấp.
- **Cách kiểm tra:** Hệ thống tìm liên kết dựa trên thông tin như đối tác, nội dung thanh toán, giá trị và thời gian giao dịch. Việc chưa tìm thấy liên kết có thể xuất phát từ dữ liệu thiếu, nội dung chuyển khoản không rõ hoặc một khoản thanh toán liên quan đến nhiều hóa đơn.
- **Cảnh báo đầu ra:** Thông báo rằng hóa đơn giá trị lớn cần được đối chiếu với chứng từ thanh toán không dùng tiền mặt theo quy định hiện hành và dữ liệu hiện có chưa thể hiện chứng từ phù hợp. Hệ thống không kết luận chứng từ không tồn tại, không khẳng định chi phí hoặc thuế GTGT chắc chắn bị loại và không áp dụng một ngưỡng pháp lý chưa được kiểm chứng.

## 5. Thành phần kỹ thuật dự kiến

- **Frontend Streamlit:** Cung cấp giao diện tải dữ liệu, lựa chọn kỳ rà soát, xem cảnh báo và mở phần giải thích.
- **Backend FastAPI:** Tiếp nhận yêu cầu, điều phối các bước xử lý và trả kết quả cho giao diện.
- **Parser hóa đơn và chứng từ:** Đọc các định dạng dữ liệu trong phạm vi MVP, trích xuất trường cần thiết và ghi nhận trường không đọc được.
- **Rule engine:** Thực hiện các kiểm tra có điều kiện rõ ràng cho năm case MVP và lưu lý do kích hoạt từng cảnh báo.
- **Vector database/ChromaDB:** Lưu các đoạn tài liệu đã được chuẩn bị cùng thông tin nguồn để phục vụ tìm kiếm theo ngữ nghĩa.
- **RAG pháp lý:** Truy xuất nội dung liên quan từ kho tài liệu và hỗ trợ tạo phần giải thích có ngữ cảnh cho người dùng đối chiếu.
- **Báo cáo kết quả:** Tổng hợp cảnh báo, dữ liệu liên quan, lý do phát hiện và gợi ý rà soát thành đầu ra dễ lưu trữ.

Các thành phần được tách theo chức năng để nhóm có thể kiểm thử từng bước và mở rộng dần mà không làm thay đổi bản chất của cảnh báo.

## 6. Vai trò của AI trong TaxGPT

AI hỗ trợ đọc và trích xuất thông tin từ các định dạng dữ liệu khác nhau, hiểu câu hỏi của người dùng và diễn giải cảnh báo bằng ngôn ngữ gần với nghiệp vụ. Khi dữ liệu đủ rõ, AI giúp giảm thao tác nhập lại và hỗ trợ liên kết thông tin giữa hóa đơn, chứng từ thanh toán và nguồn tham chiếu.

RAG được sử dụng để truy xuất nội dung liên quan từ kho tài liệu pháp lý đã được chuẩn bị. Cách làm này giúp phần giải thích bám vào nguồn có sẵn và cho người dùng biết nội dung nào cần đối chiếu, nhưng chất lượng vẫn phụ thuộc vào phạm vi, tính cập nhật và mức độ kiểm chứng của kho tài liệu.

Rule engine giữ vai trò thực hiện những kiểm tra có điều kiện rõ ràng như so sánh trường dữ liệu, kiểm tra trùng lặp và tính lại số liệu. Việc tách rule engine khỏi phần diễn giải bằng AI giúp giảm nguy cơ mô hình tự suy diễn điều kiện kiểm tra. Con người vẫn là bên đánh giá tình huống thực tế và đưa ra quyết định cuối cùng.

## 7. Điểm khác biệt của giải pháp

- **Rà soát trước khi nộp hoặc lưu hồ sơ:** TaxGPT tập trung phát hiện sớm các dấu hiệu cần chú ý, thay vì chỉ hỗ trợ nhập liệu hoặc lập tờ khai.
- **Kết hợp rule engine và RAG:** Quy tắc minh bạch xử lý điều kiện kiểm tra; RAG bổ sung ngữ cảnh để người dùng hiểu và tự đối chiếu cảnh báo.
- **Giải thích bằng ngôn ngữ dễ hiểu:** Kết quả cho biết hệ thống phát hiện điều gì, dựa trên dữ liệu nào và người dùng nên kiểm tra tiếp ở đâu.
- **Phù hợp với đơn vị quy mô nhỏ:** MVP hướng tới quy trình gọn, có thể sử dụng với dữ liệu phổ biến mà không đòi hỏi một hệ thống ERP lớn.
- **Có khả năng mở rộng:** Kiến trúc theo module cho phép bổ sung định dạng dữ liệu, case rủi ro và nguồn tài liệu sau khi được kiểm thử và xác nhận.

## 8. Giới hạn của MVP

- MVP chỉ xử lý năm case đã chọn và chưa bao phủ toàn bộ nghiệp vụ thuế Việt Nam.
- Hệ thống không thay thế kế toán, kiểm toán, luật sư, đại lý thuế hoặc cơ quan thuế.
- Cảnh báo không phải kết luận đúng hoặc sai pháp lý tuyệt đối.
- Chất lượng kết quả phụ thuộc vào độ đầy đủ, chính xác và khả năng đọc được của dữ liệu đầu vào.
- Việc ghép hóa đơn với chứng từ thanh toán có thể chưa chính xác khi dữ liệu thiếu hoặc nội dung giao dịch không rõ.
- Kho RAG có thể thiếu tài liệu, chưa cập nhật hoặc truy xuất chưa đúng ngữ cảnh; người dùng phải kiểm tra nguồn gốc trước khi sử dụng.
- Các căn cứ, điều kiện áp dụng, ngoại lệ, quy định chuyển tiếp và nội dung pháp lý chi tiết cần tiếp tục được con người hoặc chuyên gia đối chiếu với văn bản gốc trước khi demo chính thức.

## 9. Kết luận

TaxGPT là một hướng tiếp cận khả thi để hỗ trợ doanh nghiệp nhỏ và người làm kế toán rà soát sớm rủi ro trong hóa đơn, chứng từ và dữ liệu kế toán cơ bản. MVP có phạm vi rõ ràng, kết quả có thể giải thích và có thể trình diễn bằng dữ liệu mẫu cho năm case đã chọn. Sự kết hợp giữa rule engine, AI và RAG tạo nền tảng để phát triển prototype theo từng bước, đồng thời vẫn giữ vai trò quyết định cuối cùng thuộc về con người. Với định hướng cảnh báo sớm và hỗ trợ tuân thủ, giải pháp phù hợp để trình bày trong hồ sơ Vòng 1 và tiếp tục hoàn thiện ở các giai đoạn sau.
