# GD1-DASH — Bản nháp nội dung nộp Dashboard Vòng 1

## 1. Loại bài nộp

Hồ sơ ý tưởng - Vòng 1

## 2. Tên bài dự thi

TaxGPT — Trợ lý AI hỗ trợ phát hiện rủi ro thuế và tuân thủ chứng từ cho SMEs Việt Nam

## 3. Tóm tắt bài dự thi

Doanh nghiệp nhỏ, hộ kinh doanh và người làm kế toán thường phải rà soát hóa đơn, bảng kê và chứng từ thanh toán nằm ở nhiều nguồn trong khi nguồn lực chuyên môn còn hạn chế. Kiểm tra thủ công có nhiều thao tác lặp lại và có thể bỏ sót các bản ghi cần xem xét trước khi nộp hoặc lưu hồ sơ.

TaxGPT được đề xuất như một lớp hỗ trợ rà soát rủi ro, không thay thế phần mềm kế toán hoặc công cụ kê khai. MVP tập trung vào năm tình huống: hóa đơn nghi trùng; sai mã số thuế hoặc tên người mua; VAT không khớp phép tính; hóa đơn có ngày lập ngoài kỳ dữ liệu đang rà soát; và hóa đơn giá trị lớn chưa tìm thấy chứng từ thanh toán không dùng tiền mặt. Rule engine dự kiến thực hiện các kiểm tra rõ ràng, còn RAG và AI hỗ trợ giải thích cảnh báo bằng ngôn ngữ dễ hiểu.

Giải pháp hướng tới giúp người dùng ưu tiên nội dung cần kiểm tra, thấy dữ liệu đã kích hoạt cảnh báo và chuẩn bị bước đối chiếu tiếp theo. Mỗi kết quả chỉ là cảnh báo rủi ro, không phải kết luận đúng hoặc sai pháp lý. TaxGPT không thay thế kế toán, luật sư, đại lý thuế hoặc cơ quan thuế; quyết định cuối cùng thuộc về con người và chủ thể có thẩm quyền.

## 4. Phương pháp và công nghệ sử dụng

Kiến trúc MVP dự kiến gồm Frontend Streamlit, Backend FastAPI, parser dữ liệu, lớp chuẩn hóa, rule engine, ChromaDB/RAG pháp lý, lớp giải thích AI và human review. Người dùng tải dữ liệu mẫu; parser đọc các trường có cấu trúc; rule engine kiểm tra năm case và lưu lý do kích hoạt cảnh báo. RAG dự kiến chỉ truy xuất nội dung pháp lý đã được con người kiểm chứng, còn AI explanation layer hỗ trợ diễn giải kết quả và gợi ý bước rà soát. Con người đối chiếu chứng từ gốc và đưa ra quyết định cuối cùng.

Nhóm đã chuẩn bị 12 hóa đơn và 6 giao dịch giả lập để minh họa, gồm tình huống rủi ro và hóa đơn bình thường đối chứng. Hiện dự án mới có khung FastAPI, giao diện Streamlit tối thiểu, dữ liệu mẫu và thiết kế kiến trúc. Parser hoàn chỉnh, rule engine, kho RAG, lớp giải thích và Dashboard nghiệp vụ vẫn cần được triển khai, kiểm thử.

## 5. Ghi chú của đội thi

Dữ liệu demo hoàn toàn giả lập, không chứa thông tin doanh nghiệp hoặc cá nhân thật. TaxGPT chỉ hỗ trợ rà soát, cảnh báo dấu hiệu rủi ro và gợi ý nội dung cần kiểm tra; hệ thống không đưa ra kết luận pháp lý thay người có chuyên môn. Các căn cứ và nội dung pháp lý chi tiết sẽ tiếp tục được nhóm đối chiếu với nguồn chính thức trước khi dùng trong prototype hoặc trình bày chuyên sâu. Nhóm sẽ bổ sung link báo cáo, slide, GitHub và demo khi các tài liệu, mã nguồn và môi trường triển khai đã được hoàn thiện, rà soát.

## 6. Link báo cáo

Chưa có — sẽ bổ sung sau khi xuất bản báo cáo PDF/DOCX.

## 7. Link slide trình bày

Chưa có — sẽ bổ sung sau.

## 8. Link GitHub / mã nguồn

Chưa công khai — sẽ bổ sung khi mã nguồn được rà soát.

## 9. Link demo sản phẩm

Chưa có demo online — hiện có prototype cục bộ.

## 10. File bài dự thi cần chuẩn bị

- Ưu tiên upload PDF hoặc DOCX bản mô tả ý tưởng.
- Nội dung nên được xuất từ bản GD1-07 hoặc từ bản rút gọn có cấu trúc trình bày rõ ràng.
- File phải thuộc định dạng Dashboard chấp nhận và có dung lượng dưới 30 MB.
- Lần nộp đầu tiên phải đính kèm file.

## Checklist trước khi nộp

- [ ] Kiểm tra tên bài dự thi.
- [ ] Kiểm tra tóm tắt không quá dài.
- [ ] Kiểm tra phương pháp/công nghệ không mô tả quá mức.
- [ ] Không nêu ngưỡng tiền case 5.
- [ ] Không cam kết tuân thủ 100%.
- [ ] Không viết TaxGPT thay thế chuyên gia.
- [ ] Chuẩn bị file PDF/DOCX dưới 30 MB.
- [ ] Kiểm tra link nếu có.
- [ ] Chụp màn hình sau khi nộp thành công.
