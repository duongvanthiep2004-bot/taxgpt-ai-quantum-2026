# GD1-07 — Bản mô tả ý tưởng Vòng 1 TaxGPT (v2)

## 1. Tên ý tưởng

**TaxGPT — Trợ lý AI hỗ trợ rà soát rủi ro thuế và tuân thủ chứng từ cho doanh nghiệp nhỏ**

## 2. Nhóm chủ đề

**AI cho Quản trị Rủi ro và Tuân thủ**

## 3. Tóm tắt ý tưởng

TaxGPT dự kiến hỗ trợ doanh nghiệp nhỏ, hộ kinh doanh và người làm kế toán rà soát sớm dấu hiệu rủi ro trong dữ liệu chứng từ. Các đơn vị quy mô nhỏ có thể phải xử lý dữ liệu nằm rải rác ở XML, PDF, Excel và sao kê trong khi nguồn lực kế toán hạn chế. TaxGPT hướng tới một lớp kiểm tra trước khi nộp hoặc lưu hồ sơ: rule engine kiểm tra điều kiện rõ ràng; RAG dự kiến truy xuất nội dung đã được kiểm chứng; AI hỗ trợ giải thích cảnh báo.

MVP gồm năm case: hóa đơn nghi trùng; sai MST hoặc tên người mua; VAT lệch phép tính; hóa đơn ngoài kỳ dữ liệu; và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt. Demo trước mắt dùng dữ liệu mẫu có cấu trúc, rule đơn giản và cảnh báo có lý do. TaxGPT không thay thế phần mềm kế toán hoặc công cụ kê khai; cũng không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế. Mỗi cảnh báo phải qua human review.

## 4. Bối cảnh và vấn đề thực tế

Doanh nghiệp nhỏ và hộ kinh doanh thường xử lý hóa đơn, bảng kê và chứng từ thanh toán với nguồn lực kế toán hạn chế. Dữ liệu có thể nằm ở XML, PDF, Excel, ảnh scan hoặc sao kê; người dùng phải mở nhiều file, đọc trường, tính lại số liệu và tự liên kết hóa đơn với thanh toán.

Các thao tác lặp và áp lực thời gian có thể làm người dùng bỏ sót bản ghi nghi trùng, MST không khớp, VAT chênh lệch hoặc ngày hóa đơn ngoài kỳ dữ liệu. Dấu hiệu bất thường chưa đồng nghĩa với vi phạm, nhưng giúp ưu tiên rà soát trước khi nộp, lưu hoặc giải trình hồ sơ.

TaxGPT lựa chọn nhu cầu cảnh báo rủi ro trước, không thay quy trình kế toán hay kê khai. Đây là nhận định định tính từ bài toán thực tế; nhóm **chưa có khảo sát định lượng để chứng minh quy mô nhu cầu**. Giai đoạn sau cần phỏng vấn hoặc quan sát người dùng để xác nhận quy trình và mức ưu tiên của từng case.

## 5. Đối tượng sử dụng

- **Doanh nghiệp nhỏ và vừa:** cần một lớp rà soát bổ sung nhưng chưa có bộ phận thuế chuyên sâu.
- **Hộ kinh doanh:** cần hỗ trợ làm quen với hóa đơn điện tử và đối chiếu chứng từ số.
- **Kế toán nội bộ:** cần ưu tiên nhanh các bản ghi đáng chú ý trong tập dữ liệu.
- **Dịch vụ kế toán hoặc đại lý thuế quy mô nhỏ:** cần chuẩn hóa bước kiểm tra ban đầu trước khi chuyên gia xem xét.
- **Sinh viên và người học nghiệp vụ thuế:** cần môi trường mô phỏng quy trình phát hiện và giải thích cảnh báo.

Nhóm người dùng ưu tiên cần được xác nhận thêm bằng phỏng vấn và thử nghiệm có hướng dẫn trước khi phát triển sản phẩm ngoài phạm vi cuộc thi.

## 6. Mô tả giải pháp

TaxGPT dự kiến cung cấp luồng làm việc:

**Upload dữ liệu mẫu → Đọc và chuẩn hóa → Rule Engine → RAG pháp lý → Giải thích cảnh báo → Dashboard → Human review**

Người dùng tải bảng hóa đơn và thanh toán. Hệ thống chuẩn hóa trường cần thiết; rule engine kiểm tra năm case bằng điều kiện có thể kiểm thử và truy ngược. RAG dự kiến truy xuất từ kho pháp lý đã được con người kiểm chứng; AI có thể diễn giải dấu hiệu, dữ liệu kích hoạt và bước rà soát.

Khi dữ liệu hoặc nguồn chưa đủ, hệ thống cần báo giới hạn thay vì suy đoán. Người dùng thực hiện human review trước quyết định nghiệp vụ hoặc pháp lý. Parser hoàn chỉnh, rule engine, RAG, AI và Dashboard nghiệp vụ vẫn là phạm vi dự kiến.

## 7. Phạm vi MVP

| Case | Mục tiêu kiểm tra | Cảnh báo đầu ra dự kiến |
|---|---|---|
| **1. Hóa đơn trùng** | So sánh số, ký hiệu, ngày hóa đơn, MST và tổng tiền để tìm bản ghi có dấu hiệu trùng. | Hiển thị các trường khớp và yêu cầu xác minh; không kết luận gian lận. |
| **2. Sai MST hoặc tên người mua** | Đối chiếu thông tin người mua với hồ sơ tham chiếu; phân biệt MST không khớp với sai lệch nhỏ về tên. | Nêu rõ trường không khớp và gợi ý rà soát; không kết luận hóa đơn vô hiệu. |
| **3. VAT không khớp phép tính** | Tính lại VAT và tổng tiền từ dữ liệu trên chứng từ, sử dụng sai số kỹ thuật được cấu hình cho việc làm tròn. | Hiển thị giá trị gốc, giá trị tính lại và chênh lệch; sai số kỹ thuật không phải quy định pháp lý. |
| **4. Hóa đơn ngoài kỳ dữ liệu đang rà soát** | So sánh ngày hóa đơn với kỳ dữ liệu do người dùng lựa chọn. | Gợi ý kiểm tra kỳ kê khai hoặc khả năng kê khai bổ sung theo tình huống; không tự kết luận vi phạm. |
| **5. Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt** | Tìm liên kết giữa hóa đơn cần đối chiếu với dữ liệu thanh toán không dùng tiền mặt được cung cấp. | Cảnh báo chưa tìm thấy chứng từ liên quan; không đồng nhất “chưa tìm thấy” với “không tồn tại” và không kết luận chắc chắn về hậu quả thuế hoặc chi phí. |

Rule của case 2 phụ thuộc hồ sơ người mua tham chiếu. Việc ghép nối ở case 5 có thể bị ảnh hưởng bởi thanh toán từng phần, thanh toán gộp, nội dung chuyển khoản không rõ hoặc dữ liệu chưa đầy đủ. Các trường hợp này phải được hiển thị như giới hạn cần con người xem xét.

## 8. Kiến trúc kỹ thuật dự kiến

| Thành phần | Vai trò trong MVP | Trạng thái tại thời điểm lập hồ sơ |
|---|---|---|
| **Frontend Streamlit** | Tải dữ liệu và xem cảnh báo. | Đã có giao diện tối thiểu; màn hình nghiệp vụ còn dự kiến. |
| **Backend FastAPI** | Tiếp nhận yêu cầu và điều phối xử lý. | Đã có khung ứng dụng và endpoint kiểm tra trạng thái; API nghiệp vụ chưa hoàn thiện. |
| **Parser / Data Normalizer** | Đọc bảng mẫu và đưa trường dữ liệu về cấu trúc chung. | Chưa hoàn thiện; MVP ưu tiên dữ liệu Excel có cấu trúc. |
| **Rule Engine** | Kiểm tra năm case bằng điều kiện rõ ràng và lưu lý do kích hoạt. | Dự kiến triển khai và kiểm thử với dữ liệu mẫu. |
| **ChromaDB / RAG** | Truy xuất nội dung đã được kiểm chứng, có nguồn để đối chiếu. | Mới có thư mục lưu trữ; kho tài liệu và pipeline chưa hoàn thiện. |
| **AI Explanation Layer** | Diễn giải cảnh báo và gợi ý bước kiểm tra bằng ngôn ngữ dễ hiểu. | Dự kiến; không được thay đổi kết quả rule hoặc kết luận pháp lý. |
| **Dashboard / Report** | Hiển thị dữ liệu liên quan, lý do cảnh báo và báo cáo ngắn. | Dự kiến phát triển từ giao diện tối thiểu. |
| **Human Review** | Đối chiếu chứng từ gốc, ngoại lệ và nguồn tham khảo. | Bước bắt buộc trong quy trình dự kiến. |

Rule engine được tách khỏi AI để điều kiện có thể kiểm thử. RAG chỉ nên dùng nội dung đã được con người kiểm chứng, có nguồn và trạng thái hiệu lực. Cách này giảm rủi ro AI nhưng không biến cảnh báo thành kết luận pháp lý.

## 9. Dữ liệu mẫu và khả năng demo

Nhóm đã chuẩn bị **12 hóa đơn** và **6 giao dịch giả lập**. Mỗi case có hai dòng; hai hóa đơn bình thường dùng làm đối chứng. Hai hóa đơn case 5 không có payment reference hay giao dịch tương ứng. Dữ liệu mang dấu hiệu `FAKE`, `DEMO` hoặc “Mô phỏng”, không dùng thông tin thật.

Phạm vi demo dự kiến:

1. Tải bảng hóa đơn và thanh toán mẫu lên giao diện.
2. Đọc các trường có cấu trúc và hiển thị dữ liệu đã nhận.
3. Chạy rule đơn giản cho năm case MVP.
4. Hiển thị loại cảnh báo, trường kích hoạt, lý do và gợi ý kiểm tra.
5. Mở một cảnh báo để minh họa human review và xuất kết quả ngắn.

Demo không nhằm xử lý mọi hóa đơn thật hay ngoại lệ. XML có thể bổ sung sau; PDF, ảnh scan và OCR là hướng mở rộng, không phải cam kết của demo lõi.

## 10. Vai trò của AI

- **Rule engine:** tạo cảnh báo cho điều kiện xác định và lưu dữ liệu kích hoạt.
- **RAG:** dự kiến tìm nội dung trong kho đã được con người kiểm chứng; không tự bổ sung căn cứ khi thiếu nguồn.
- **AI giải thích:** có thể diễn giải kết quả rule, hỗ trợ hỏi đáp và nêu bước rà soát.
- **AI đọc dữ liệu:** là hướng nghiên cứu cho định dạng khó; MVP ưu tiên bảng có cấu trúc.
- **Con người:** kiểm tra dữ liệu gốc, ngoại lệ và quyết định.

AI không được tự tạo rule, sửa kết quả hoặc phán quyết pháp lý. Giá trị AI trong MVP là giải thích theo ngữ cảnh; kiểm tra điều kiện vẫn thuộc rule engine.

## 11. Tính mới và điểm khác biệt

TaxGPT không phải phần mềm kế toán hoặc kê khai mới mà là **lớp rà soát rủi ro bổ sung** trước khi nộp hoặc lưu hồ sơ.

- **Cảnh báo rủi ro trước:** ưu tiên chỉ ra bản ghi cần xem lại thay vì thực hiện hạch toán hay lập tờ khai.
- **Rule minh bạch:** cảnh báo cho biết điều kiện và dữ liệu kích hoạt, giúp người dùng truy ngược.
- **RAG có kiểm soát:** phần giải thích pháp lý chỉ dự kiến dùng nội dung đã được kiểm chứng và có nguồn đối chiếu.
- **AI giải thích theo ngữ cảnh:** hỗ trợ người không chuyên hiểu dấu hiệu và bước kiểm tra, không tự quyết định đúng/sai.
- **Human review bắt buộc:** ngăn việc hiểu cảnh báo tự động như kết luận nghiệp vụ hoặc pháp lý.
- **Thiết kế cho đơn vị nhỏ:** là lớp hỗ trợ, không thay hệ thống kế toán hoặc ERP.

Khác biệt cốt lõi là chuỗi **rule rõ ràng → nguồn được kiểm soát → giải thích có giới hạn → con người quyết định**, không phải việc “có AI”. Nhóm vẫn cần khảo sát thị trường trước khi so sánh sản phẩm cụ thể.

## 12. Tính khả thi

Nhóm đã có repo, môi trường Python, khung FastAPI, Streamlit tối thiểu, thư mục ChromaDB, dữ liệu mẫu và kiến trúc. Đây chưa phải sản phẩm hoàn thiện. Nhóm dự kiến làm theo thứ tự: đọc Excel mẫu, chuẩn hóa, chạy năm rule, hiển thị lý do; sau đó mới bổ sung RAG và AI. XML, PDF/OCR chỉ mở rộng khi luồng lõi ổn định.

**Tiêu chí kiểm thử MVP dự kiến:**

1. Chạy được năm case bằng dữ liệu mẫu, mỗi case có ít nhất hai tình huống minh họa.
2. Hai hóa đơn bình thường không bị gắn cảnh báo sai cho năm case trong bộ test hiện tại.
3. Dashboard hiển thị đúng loại cảnh báo, dữ liệu kích hoạt, lý do và gợi ý rà soát.
4. Rule VAT hiển thị phép tính và sai số kỹ thuật cấu hình; không trình bày sai số đó như quy định pháp lý.
5. Hệ thống không đưa ra kết luận pháp lý tuyệt đối hoặc thay quyết định của con người.
6. Case 5 không hiển thị ngưỡng tiền chưa được kiểm chứng nếu chưa có xác nhận nghiệp vụ và pháp lý.
7. Khi dữ liệu hoặc nguồn tham khảo không đủ, đầu ra phải nêu giới hạn thay vì suy đoán.

Đây là kế hoạch; chỉ công bố kết quả sau khi triển khai, chạy thử và lưu bằng chứng.

## 13. Giới hạn và rủi ro

- MVP chỉ xử lý năm case và chưa bao phủ toàn bộ nghiệp vụ thuế Việt Nam.
- Bộ dữ liệu nhỏ, chỉ để minh họa và chưa chứng minh độ chính xác thực tế.
- Chất lượng cảnh báo phụ thuộc dữ liệu đầu vào và hồ sơ tham chiếu do người dùng cung cấp.
- Parser hoặc OCR có thể đọc sai MST, ngày và số tiền; OCR/PDF chưa phải cam kết của demo lõi.
- Rule engine có thể cảnh báo thừa hoặc bỏ sót trong trường hợp biên, dữ liệu thiếu hay nghiệp vụ đặc thù.
- Ghép hóa đơn với thanh toán có thể không rõ khi thanh toán từng phần, gộp hoặc thiếu nội dung.
- Kho pháp lý cần tiếp tục được kiểm chứng về nguồn, hiệu lực và phạm vi.
- AI có thể diễn giải quá chắc chắn; cần prompt giới hạn, trích nguồn và từ chối khi thiếu căn cứ.
- Dữ liệu thật cần xác thực, phân quyền, mã hóa, giới hạn lưu giữ và cơ chế xóa.
- Người dùng có thể hiểu nhầm cảnh báo là kết luận; Dashboard và báo cáo phải nêu rõ human review.

## 14. Kế hoạch phát triển tiếp

1. Phỏng vấn hoặc quan sát một số người dùng mục tiêu để kiểm chứng nhu cầu, quy trình và thứ tự ưu tiên; chỉ công bố kết quả có bằng chứng.
2. Hoàn thiện luồng Excel mẫu, Data Normalizer và năm rule có test tự động.
3. Xây kịch bản demo 2–3 phút và ghi nhận kết quả theo các tiêu chí kiểm thử.
4. Chuẩn bị kho tài liệu đã kiểm chứng, gắn nguồn, hiệu lực, phạm vi và tích hợp RAG ở mức phù hợp.
5. Bổ sung lớp giải thích AI với mẫu câu an toàn và kiểm thử trường hợp thiếu căn cứ.
6. Mở rộng XML, sau đó đánh giá riêng PDF/OCR và dữ liệu thật khi có biện pháp bảo mật.
7. Hoàn thiện Dashboard, báo cáo và phương án demo dự phòng cho giai đoạn tiếp theo.

## 15. Kết luận

TaxGPT hướng tới hỗ trợ doanh nghiệp nhỏ và người làm kế toán rà soát sớm chứng từ. MVP gồm năm case có thể kiểm thử bằng dữ liệu giả lập. Bản v2 thu hẹp demo vào dữ liệu có cấu trúc, cảnh báo có lý do và human review; XML, PDF/OCR, RAG và AI được phát triển theo từng bước.

TaxGPT là lớp rà soát bổ sung, không thay phần mềm kế toán hay kê khai. Rule engine tạo điều kiện truy vết; RAG dự kiến giới hạn nguồn; AI hỗ trợ diễn giải; con người quyết định. Nhóm đã có nền tảng và dữ liệu mẫu nhưng vẫn cần triển khai rule, đo kết quả, khảo sát người dùng và kiểm chứng pháp lý. Hồ sơ không khẳng định sản phẩm đã hoàn thiện hoặc kết quả pháp lý tuyệt đối.

## Phụ lục — Những điểm đã cải thiện so với bản GD1-05

| Nhóm vấn đề từ phản biện | Cách đã chỉnh trong bản v2 | Mức độ xử lý |
|---|---|---|
| Bằng chứng nhu cầu người dùng | Ghi rõ nhận định định tính, chưa có khảo sát và đưa phỏng vấn/quan sát vào kế hoạch. | **Còn cần kiểm tra** bằng người dùng thực tế. |
| Điểm khác biệt | Định vị lớp rà soát bổ sung; làm rõ rule, RAG, AI và human review. | **Đã xử lý** trong hồ sơ; còn cần khảo sát cạnh tranh. |
| Vai trò của AI | Tách AI giải thích khỏi rule engine và không coi việc “có AI” là điểm mới tự thân. | **Đã xử lý** ở cấp mô tả. |
| Phạm vi demo | Thu hẹp vào Excel mẫu, năm rule, cảnh báo và human review; không cam kết OCR/PDF. | **Đã xử lý** ở cấp kế hoạch; cần triển khai. |
| Tiêu chí kiểm thử | Bổ sung bảy tiêu chí về case, đối chứng, Dashboard và giới hạn pháp lý. | **Đã xử lý** ở cấp kế hoạch; cần chạy test. |
| Tuyên bố quá tham vọng | Dùng nhất quán các từ “dự kiến”, “hướng tới”, “có thể hỗ trợ” và phân biệt rõ thành phần đã có/chưa hoàn thiện. | **Đã xử lý**. |
| Rủi ro pháp lý và AI | Bổ sung báo thiếu căn cứ, nguồn RAG được kiểm chứng và human review. | **Đã xử lý** về diễn đạt; pháp lý vẫn cần kiểm chứng. |
