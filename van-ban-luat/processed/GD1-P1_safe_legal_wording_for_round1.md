# GD1-P1 — Bản diễn đạt pháp lý an toàn cho hồ sơ Vòng 1

## 1. Nguyên tắc sử dụng pháp lý trong hồ sơ

- TaxGPT chỉ phát hiện dấu hiệu bất thường, cảnh báo rủi ro và gợi ý nội dung cần kiểm tra tiếp.
- Kết quả của TaxGPT không phải là kết luận đúng hoặc sai tuyệt đối về mặt pháp lý.
- TaxGPT không thay thế kế toán, luật sư, đại lý thuế, cơ quan thuế hoặc chủ thể có thẩm quyền.
- Hồ sơ không nêu điều, khoản, điểm hoặc ngưỡng định lượng cụ thể nếu nhóm chưa đối chiếu đầy đủ với văn bản gốc và bối cảnh áp dụng.
- Với văn bản được ban hành sau năm 2025, chỉ sử dụng nội dung pháp lý sau khi đã kiểm tra trên nguồn chính thức, xác định hiệu lực và xem xét quy định chuyển tiếp nếu có.
- Khi căn cứ chưa được kiểm chứng đầy đủ, hồ sơ chỉ mô tả logic kiểm tra kỹ thuật và yêu cầu người dùng rà soát tình huống thực tế.
- Nghị định 254/2026/NĐ-CP và Luật Thuế GTGT 48/2024/QH15 đã được xác nhận là văn bản có thật; tuy nhiên, điều khoản áp dụng cho từng case vẫn cần được đối chiếu trực tiếp trước khi trích dẫn.

## 2. Bảng diễn đạt an toàn cho 5 case MVP

| Case | Mục tiêu kiểm tra của TaxGPT | Diễn đạt an toàn nên dùng trong hồ sơ | Điều không nên viết | Ghi chú kiểm chứng pháp lý |
|---|---|---|---|---|
| **1 — Hóa đơn trùng** | So sánh số, ký hiệu hóa đơn, mã số thuế người bán/người mua, ngày hóa đơn và tổng tiền để phát hiện bản ghi có dấu hiệu trùng lặp. | “TaxGPT đối chiếu các trường nhận diện chính và cảnh báo những hóa đơn có khả năng bị nhập hoặc tải lên trùng để người dùng xác minh.” | Không kết luận hóa đơn gian lận, bất hợp pháp hoặc chắc chắn được hạch toán trùng. | Cần phân biệt bản ghi trùng với bản sao, hóa đơn điều chỉnh/thay thế, giao dịch định kỳ và lỗi nhập dữ liệu. Căn cứ về hóa đơn điện tử chỉ được trích sau khi kiểm tra văn bản gốc. |
| **2 — Sai MST/tên người mua** | Đối chiếu mã số thuế và thông tin tên, địa chỉ người mua với dữ liệu tham chiếu; phân biệt mã số thuế không khớp với sai lệch nhỏ về tên hoặc địa chỉ. | “TaxGPT cảnh báo riêng trường hợp mã số thuế không khớp và trường hợp tên hoặc địa chỉ có sai lệch nhỏ, giúp người dùng ưu tiên rà soát theo mức độ.” | Không kết luận mọi sai lệch làm hóa đơn vô hiệu, không có giá trị hoặc không được kê khai. | Cần kiểm tra quy định hiện hành, loại người mua, dữ liệu đăng ký và cơ chế xử lý sai sót trước khi đánh giá hậu quả pháp lý. |
| **3 — VAT không khớp phép tính** | Tính lại số thuế và tổng tiền từ dữ liệu trên chứng từ để phát hiện chênh lệch số học hoặc dữ liệu không nhất quán. | “TaxGPT kiểm tra logic tính toán theo các trường dữ liệu trên hóa đơn và cảnh báo chênh lệch vượt quá sai số kỹ thuật được cấu hình.” | Không mô tả `tolerance` là mức sai số được pháp luật mặc nhiên chấp nhận; không tự kết luận số thuế đúng hoặc sai về pháp lý. | `Tolerance` là tham số kỹ thuật phục vụ xử lý làm tròn và phải do nhóm nghiệp vụ cấu hình. Trường hợp đặc thù vẫn cần người có chuyên môn xem xét. |
| **4 — Hóa đơn ngoài kỳ kê khai** | Phát hiện hóa đơn có ngày lập ngoài kỳ dữ liệu đang được kiểm tra và đưa vào danh sách cần rà soát. | “TaxGPT phát hiện hóa đơn có ngày lập ngoài kỳ dữ liệu đang kiểm tra và gợi ý người dùng rà soát kỳ kê khai hoặc khả năng kê khai bổ sung theo tình huống thực tế.” | Không viết rằng hóa đơn ngoài kỳ đương nhiên là vi phạm, không hợp lệ hoặc không được kê khai. | Cần đối chiếu quy định hiện hành, thời điểm phát hiện, hồ sơ đã kê khai và các điều kiện áp dụng cho việc kê khai bổ sung. |
| **5 — Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt** | Đối chiếu các hóa đơn giá trị lớn với dữ liệu chứng từ thanh toán không dùng tiền mặt và cảnh báo khi chưa tìm thấy liên kết phù hợp. | “Hóa đơn giá trị lớn cần được đối chiếu với chứng từ thanh toán không dùng tiền mặt theo quy định hiện hành; TaxGPT cảnh báo khi dữ liệu được cung cấp chưa thể hiện chứng từ liên quan.” | Không nêu ngưỡng cụ thể khi chưa có điều khoản gốc đã xác minh; không kết luận chi phí hoặc thuế GTGT chắc chắn bị loại; không đồng nhất “chưa tìm thấy” với “không tồn tại”. | Đây là case có rủi ro diễn giải cao. Phải kiểm tra văn bản đang có hiệu lực, điều kiện áp dụng, quy định chuyển tiếp và các trường hợp thanh toán đặc thù trước khi cấu hình ngưỡng hoặc đưa ra nhận định nghiệp vụ. |

## 3. Đoạn văn có thể đưa trực tiếp vào hồ sơ

TaxGPT hỗ trợ rà soát ban đầu dữ liệu hóa đơn và chứng từ. Hệ thống kết hợp quy tắc minh bạch với AI để phát hiện dấu hiệu trùng lặp, thông tin người mua không nhất quán, chênh lệch phép tính VAT, hóa đơn có ngày lập ngoài kỳ dữ liệu đang kiểm tra và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt. Mỗi kết quả chỉ là cảnh báo rủi ro kèm lý do và gợi ý kiểm tra, không phải kết luận vi phạm hoặc xác nhận giá trị pháp lý của chứng từ. Tham số kỹ thuật, nguồn pháp lý và tình huống ngoại lệ phải được người có chuyên môn rà soát trước khi sử dụng. TaxGPT không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế. Quyết định cuối cùng thuộc về người dùng và chủ thể có thẩm quyền, dựa trên hồ sơ thực tế và quy định hiện hành.

## 4. Trạng thái GD1-P1

- GD1-P1 **chưa phải là kết quả kiểm chứng pháp lý tuyệt đối**. Tài liệu này không xác nhận đầy đủ điều, khoản, điểm, ngưỡng áp dụng hoặc mọi quy định chuyển tiếp cho năm case.
- Tài liệu **đủ để tạo bản diễn đạt pháp lý an toàn cho hồ sơ Vòng 1**, với điều kiện nhóm giữ nguyên các giới hạn và không bổ sung kết luận hoặc con số chưa được kiểm chứng.
- Đề xuất trạng thái:
  - Giữ **`[~]`** nếu GD1-P1 được định nghĩa là kiểm chứng pháp lý đầy đủ.
  - Có thể ghi **`[x - hồ sơ an toàn]`** nếu GD1-P1 chỉ được đánh giá theo mục tiêu tạo nội dung an toàn phục vụ hồ sơ Vòng 1.
- Việc cần làm sau: chuyên gia hoặc thành viên phụ trách nghiệp vụ tiếp tục đối chiếu văn bản gốc, hiệu lực, điều khoản áp dụng, quy định chuyển tiếp và ngoại lệ trước khi cấu hình rule engine hoặc demo chính thức.
