# GD1-05 — Bản mô tả ý tưởng Vòng 1: TaxGPT

## 1. Tên ý tưởng

**TaxGPT — Trợ lý AI hỗ trợ rà soát rủi ro thuế và tuân thủ chứng từ cho doanh nghiệp nhỏ**

## 2. Nhóm chủ đề

**AI cho Quản trị Rủi ro và Tuân thủ**

## 3. Tóm tắt ý tưởng

TaxGPT là trợ lý AI hỗ trợ doanh nghiệp nhỏ, hộ kinh doanh và người làm kế toán rà soát sớm dấu hiệu rủi ro trong hóa đơn, chứng từ và dữ liệu kế toán cơ bản. Giải pháp hướng tới vấn đề dữ liệu nằm ở nhiều định dạng, khối lượng chứng từ tăng và việc kiểm tra thủ công dễ bỏ sót các điểm không nhất quán trước khi kê khai hoặc lưu hồ sơ. Ở mức tổng quan, người dùng tải dữ liệu lên hệ thống; parser dự kiến trích xuất thông tin, lớp chuẩn hóa đưa dữ liệu về cấu trúc chung, rule engine kiểm tra các điều kiện rõ ràng, còn RAG và AI hỗ trợ giải thích cảnh báo bằng ngôn ngữ dễ hiểu. MVP tập trung vào năm case: hóa đơn trùng; sai MST hoặc tên người mua; VAT không khớp phép tính; hóa đơn có ngày lập ngoài kỳ dữ liệu đang rà soát; và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt. TaxGPT giúp người dùng ưu tiên nội dung cần xem lại, hiểu lý do cảnh báo và chuẩn bị bước đối chiếu tiếp theo. Hệ thống chỉ cung cấp cảnh báo rủi ro và gợi ý kiểm tra, không thay thế kế toán, luật sư, đại lý thuế, cơ quan thuế hoặc quyết định chuyên môn cuối cùng.

## 4. Bối cảnh và vấn đề thực tế

Doanh nghiệp nhỏ và hộ kinh doanh ngày càng xử lý nhiều hóa đơn điện tử, chứng từ thanh toán, bảng kê và hồ sơ liên quan. Dữ liệu có thể nằm trong XML, PDF, Excel, ảnh scan hoặc sao kê ngân hàng; mỗi định dạng có cấu trúc khác nhau và thường được lưu ở nhiều nơi.

Khi kiểm tra bằng mắt hoặc qua các bảng tính rời rạc, người dùng phải lặp lại nhiều thao tác: đọc từng trường, so sánh MST, tính lại VAT, đối chiếu kỳ dữ liệu và tìm chứng từ thanh toán. Áp lực thời gian và sự khác biệt về kinh nghiệm có thể khiến những sai lệch nhỏ không được phát hiện sớm. Một dấu hiệu bất thường chưa đồng nghĩa với vi phạm, nhưng vẫn cần được làm rõ trước khi nộp, lưu hoặc giải trình hồ sơ.

Các công cụ kế toán hiện có hỗ trợ nhập liệu, lập báo cáo và kê khai, trong khi nhu cầu về một lớp cảnh báo rủi ro chủ động vẫn còn dư địa cải thiện. TaxGPT tập trung vào bước rà soát trước, giúp chỉ ra dữ liệu đáng chú ý và lý do cần kiểm tra. Hướng tiếp cận này phù hợp với quản trị rủi ro và tuân thủ vì hỗ trợ con người nhận biết, ưu tiên và xử lý các dấu hiệu bất thường có hệ thống.

## 5. Đối tượng sử dụng

- **Doanh nghiệp nhỏ và vừa:** cần lớp kiểm tra bổ sung nhưng chưa có bộ phận thuế chuyên sâu.
- **Hộ kinh doanh:** cần hỗ trợ làm quen với hóa đơn điện tử và quy trình đối chiếu dữ liệu.
- **Kế toán nội bộ:** cần rà soát nhiều chứng từ trong thời gian ngắn.
- **Dịch vụ kế toán hoặc đại lý thuế quy mô nhỏ:** cần chuẩn hóa bước kiểm tra ban đầu trước khi chuyên gia đánh giá.
- **Sinh viên và người học nghiệp vụ thuế:** cần công cụ mô phỏng quy trình phát hiện và giải thích cảnh báo.

## 6. Mô tả giải pháp

TaxGPT dự kiến cung cấp một luồng làm việc thống nhất:

**Upload dữ liệu → Parser → Chuẩn hóa → Rule Engine → RAG pháp lý → Giải thích cảnh báo → Dashboard → Human review**

Người dùng tải hóa đơn, chứng từ hoặc sao kê trong định dạng được MVP hỗ trợ. Parser đọc và trích xuất các trường cần thiết; Data Normalizer chuẩn hóa ngày, chuỗi, MST và giá trị tiền. Rule engine kiểm tra năm case bằng điều kiện có thể nhìn thấy và kiểm thử. Với cảnh báo cần ngữ cảnh, RAG dự kiến truy xuất nội dung từ kho pháp lý đã được kiểm chứng. AI Explanation Layer chuyển kết quả kỹ thuật và nội dung tham khảo thành phần giải thích dễ hiểu, kèm giới hạn. Người dùng xem Dashboard, đối chiếu dữ liệu gốc và quyết định bước kiểm tra tiếp theo.

Các module xử lý trên là kiến trúc dự kiến cho MVP, chưa phải toàn bộ tính năng đã hoàn thành.

## 7. Phạm vi MVP

| Case | Mục tiêu kiểm tra | Cảnh báo đầu ra dự kiến |
|---|---|---|
| **1. Hóa đơn trùng** | So sánh số, ký hiệu, ngày hóa đơn, MST và tổng tiền để phát hiện bản ghi có dấu hiệu trùng. | Hiển thị các bản ghi nghi trùng và trường khớp; yêu cầu người dùng xác minh, không kết luận gian lận. |
| **2. Sai MST hoặc tên người mua** | Đối chiếu thông tin người mua với hồ sơ tham chiếu; phân biệt MST không khớp với sai lệch nhỏ về tên hoặc địa chỉ. | Nêu rõ trường không khớp và mức ưu tiên rà soát; không kết luận hóa đơn vô hiệu. |
| **3. VAT không khớp phép tính** | Tính lại VAT và tổng tiền từ dữ liệu trên chứng từ, có sai số kỹ thuật được cấu hình để xử lý làm tròn. | Hiển thị giá trị gốc, giá trị tính lại và chênh lệch; sai số kỹ thuật không phải quy định pháp lý. |
| **4. Hóa đơn ngoài kỳ dữ liệu đang rà soát** | So sánh ngày hóa đơn với kỳ dữ liệu người dùng lựa chọn. | Gợi ý kiểm tra kỳ kê khai hoặc khả năng kê khai bổ sung theo tình huống; không tự kết luận vi phạm. |
| **5. Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt** | Đối chiếu hóa đơn giá trị lớn với chứng từ thanh toán không dùng tiền mặt trong dữ liệu được cung cấp. | Cảnh báo chưa tìm thấy chứng từ liên quan; không đồng nhất “chưa tìm thấy” với “không tồn tại” và không kết luận chắc chắn chi phí hoặc thuế bị loại. |

## 8. Kiến trúc kỹ thuật dự kiến

| Thành phần | Vai trò trong MVP |
|---|---|
| **Frontend Streamlit** | Giao diện tải dữ liệu, chọn kỳ rà soát và xem kết quả. |
| **Backend FastAPI** | Tiếp nhận yêu cầu và điều phối luồng xử lý. |
| **Parser** | Trích xuất trường dữ liệu từ hóa đơn, chứng từ và sao kê được hỗ trợ. |
| **Data Normalizer** | Đưa dữ liệu từ nhiều nguồn về cấu trúc thống nhất. |
| **Rule Engine** | Kiểm tra năm case MVP bằng các điều kiện rõ ràng. |
| **ChromaDB / RAG pháp lý** | Lưu và truy xuất nội dung pháp lý đã được kiểm chứng để bổ sung ngữ cảnh. |
| **AI Explanation Layer** | Giải thích cảnh báo, lý do và gợi ý kiểm tra bằng ngôn ngữ dễ hiểu. |
| **Report Generator** | Tổng hợp cảnh báo và dữ liệu liên quan thành báo cáo ngắn. |
| **Human Review** | Đối chiếu hồ sơ gốc, xem xét ngoại lệ và đưa ra quyết định cuối cùng. |

Kiến trúc tách rule engine khỏi lớp AI để điều kiện kiểm tra có thể truy ngược. RAG giới hạn nguồn giải thích vào kho tài liệu được kiểm soát, còn human review là bước bắt buộc trước mọi quyết định nghiệp vụ hoặc pháp lý.

## 9. Dữ liệu mẫu và khả năng demo

Nhóm đã chuẩn bị:

- `sample_invoices_mvp.xlsx` gồm **12 hóa đơn giả lập**.
- `sample_bank_payments_mvp.xlsx` gồm **6 giao dịch thanh toán giả lập**.
- Mỗi case MVP có **2 dòng minh họa** và có thêm **2 hóa đơn bình thường** để đối chứng.
- Hai hóa đơn minh họa case 5 không có payment reference và không có giao dịch tương ứng trong dữ liệu thanh toán.

Toàn bộ MST, tên đơn vị, số hóa đơn và mã thanh toán đều mang dấu hiệu `FAKE`, `DEMO` hoặc “Mô phỏng”; không sử dụng dữ liệu cá nhân hoặc doanh nghiệp thật. Bộ dữ liệu giúp mô tả cách rule engine có thể được kiểm thử sau này, nhưng nhãn rủi ro chỉ là kết quả kỳ vọng kỹ thuật, không phải kết luận pháp lý.

## 10. Vai trò của AI

- **AI đọc hiểu:** dự kiến hỗ trợ trích xuất thông tin từ một số định dạng và hiểu câu hỏi của người dùng.
- **AI giải thích:** chuyển kết quả kiểm tra thành nội dung dễ hiểu, nêu dữ liệu đã kích hoạt cảnh báo và bước rà soát tiếp theo.
- **RAG:** truy xuất nội dung liên quan từ kho tài liệu pháp lý đã được kiểm chứng và giữ thông tin nguồn để người dùng đối chiếu.
- **Rule engine:** thực hiện các điều kiện rõ ràng thay vì giao toàn bộ quyết định cho mô hình ngôn ngữ, qua đó giảm nguy cơ ảo giác.
- **Con người:** kiểm tra chứng từ gốc, xem xét ngoại lệ và quyết định cuối cùng.

AI không được tự tạo rule nghiệp vụ, thay đổi kết quả kiểm tra kỹ thuật hoặc đưa ra kết luận pháp lý thay cho người có chuyên môn.

## 11. Tính mới và điểm khác biệt

- **Cảnh báo rủi ro trước khi nộp hoặc lưu hồ sơ:** TaxGPT không chỉ hỗ trợ nhập liệu hoặc kê khai mà tập trung vào bước rà soát chủ động.
- **Kết hợp rule engine, RAG và giải thích bằng AI:** quy tắc minh bạch xử lý điều kiện; RAG bổ sung ngữ cảnh; AI giúp người dùng hiểu kết quả.
- **Thiết kế cho đơn vị quy mô nhỏ:** luồng sử dụng gọn, hướng tới dữ liệu phổ biến và không phụ thuộc một hệ thống ERP lớn.
- **Giải thích có thể truy ngược:** cảnh báo dự kiến hiển thị dữ liệu liên quan, lý do và gợi ý kiểm tra tiếp theo.
- **Kiểm soát rủi ro AI:** giới hạn nguồn RAG, tách rule khỏi AI và yêu cầu human review.
- **Khả năng mở rộng:** có thể bổ sung rule, định dạng dữ liệu và nguồn pháp lý sau khi được kiểm thử, xác nhận.

## 12. Tính khả thi

Nhóm đã có cấu trúc repo, môi trường Python, khung backend FastAPI với endpoint kiểm tra trạng thái, giao diện Streamlit tối thiểu, thư mục lưu ChromaDB, dữ liệu mẫu và tài liệu kiến trúc. Đây là nền tảng ban đầu, không phải sản phẩm hoàn thiện.

Phạm vi năm case giúp nhóm giới hạn bài toán thành các kiểm tra có thể mô tả và kiểm thử bằng dữ liệu mẫu. Trong giai đoạn prototype, nhóm dự kiến xây parser theo từng định dạng, triển khai rule engine, chuẩn bị kho pháp lý đã kiểm chứng, tích hợp RAG và hoàn thiện Dashboard. Cách phát triển theo module cho phép đo lường từng phần và giảm rủi ro phải xây toàn bộ hệ thống cùng lúc.

## 13. Giới hạn và rủi ro

- MVP chỉ xử lý năm case đã chọn, chưa bao phủ toàn bộ nghiệp vụ thuế Việt Nam.
- Chất lượng cảnh báo phụ thuộc vào độ đầy đủ và chính xác của dữ liệu đầu vào.
- Parser hoặc OCR có thể đọc sai MST, ngày, số tiền và tạo cảnh báo nhầm.
- Rule engine có thể cảnh báo thừa hoặc bỏ sót nếu rule, dữ liệu tham chiếu hay tham số kỹ thuật chưa phù hợp.
- Kho pháp lý cần tiếp tục được con người kiểm chứng về nguồn, hiệu lực, phạm vi và bối cảnh áp dụng.
- AI có thể diễn giải quá chắc chắn nếu không có prompt giới hạn và mẫu câu an toàn.
- Dữ liệu thật cần cơ chế xác thực, phân quyền, mã hóa, giới hạn lưu giữ và xóa dữ liệu.
- Người dùng có thể hiểu nhầm cảnh báo là kết luận pháp lý; giao diện và báo cáo phải nêu rõ giới hạn và yêu cầu human review.

## 14. Kế hoạch phát triển tiếp

1. Hoàn thiện parser cho XML, PDF và Excel theo phạm vi dữ liệu MVP.
2. Xây rule engine cho năm case và viết test với dữ liệu bình thường, dữ liệu rủi ro.
3. Chuẩn bị kho tài liệu đã kiểm chứng, gắn nguồn và tích hợp ChromaDB/RAG.
4. Hoàn thiện Dashboard, phần giải thích cảnh báo và báo cáo kết quả.
5. Kiểm thử với dữ liệu mẫu, ghi nhận cảnh báo sai và điều chỉnh rule có xác nhận nghiệp vụ.
6. Chuẩn bị demo, báo cáo và phương án dự phòng cho Vòng 2 nếu dự án vượt qua Vòng 1.

## 15. Kết luận

TaxGPT xuất phát từ nhu cầu thực tế của doanh nghiệp nhỏ và người làm kế toán khi rà soát hóa đơn, chứng từ ở nhiều định dạng. MVP lựa chọn năm case có phạm vi rõ ràng, có thể minh họa bằng dữ liệu giả lập và phát triển theo từng module. Khung FastAPI, giao diện Streamlit tối thiểu, dữ liệu mẫu và thiết kế kiến trúc tạo nền tảng triển khai, trong khi các module nghiệp vụ vẫn cần được xây dựng và kiểm thử. Sự kết hợp giữa rule engine, RAG, lớp giải thích AI và human review hướng tới cân bằng tự động hóa, khả năng giải thích và kiểm soát rủi ro. TaxGPT phù hợp với chủ đề **AI cho Quản trị Rủi ro và Tuân thủ** vì tập trung cảnh báo sớm và hỗ trợ kiểm tra có hệ thống. Giải pháp không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế; quyết định cuối cùng vẫn thuộc về con người và chủ thể có thẩm quyền.
