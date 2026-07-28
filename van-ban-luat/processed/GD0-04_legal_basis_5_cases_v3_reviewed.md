# GD0-04: CĂN CỨ PHÁP LÝ CHO 5 CASE MVP (BẢN RÀ SOÁT AN TOÀN V3)

**Phiên bản:** 3.0 (Reviewed)
**Ngày cập nhật:** 26/07/2026
**Người thực hiện:** Gemini
**Mục đích:** Tinh chỉnh và làm rõ các quy tắc cảnh báo, loại bỏ các kết luận pháp lý tự động, đảm bảo TaxGPT chỉ hoạt động như một công cụ hỗ trợ kỹ thuật, không phải là một nhà tư vấn pháp lý.

---

## BẢNG CĂN CỨ PHÁP LÝ - PHIÊN BẢN AN TOÀN

| Case | Rule TaxGPT được phép chạy | Mức cảnh báo nên dùng | Văn bản pháp lý ưu tiên dùng | Điều/khoản/điểm | Trích đoạn ngắn liên quan trực tiếp | Rule engine implication | Ngoại lệ cần xử lý | Kết luận |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Hóa đơn trùng** | - `duplicate_file`: Phát hiện file XML/ảnh hóa đơn trùng.<br>- `duplicate_invoice_id`: Phát hiện `Số HĐ` + `Ký hiệu` + `MST bán` trùng.<br>- `possible_duplicate_transaction`: Phát hiện các chỉ số chính (MST, số tiền, ngày) gần giống nhau. | **Vàng** | Nghị định 254/2026/NĐ-CP (về hóa đơn, chứng từ điện tử) | Cần kiểm chứng điều khoản gốc. | "Việc sử dụng hóa đơn, chứng từ điện tử phải đảm bảo tính duy nhất của mỗi số hóa đơn..." (Diễn giải nguyên tắc) | Cảnh báo về khả năng trùng lặp, yêu cầu người dùng xác minh. **Không được** tự động kết luận là "hóa đơn bất hợp pháp" hay "gian lận". | - Bản sao của cùng một hóa đơn.<br>- Hóa đơn điều chỉnh/thay thế.<br>- Lỗi nhập liệu, import lại file.<br>- Giao dịch định kỳ có giá trị giống hệt nhau. | **Đủ dùng cho cảnh báo kỹ thuật** |
| **2. Sai MST/tên người mua** | 1. `IF invoice_buyer_tin != user_company_tin THEN` cảnh báo **Đỏ**.<br>2. `IF invoice_buyer_tin == user_company_tin AND Name/Address has minor deviation THEN` cảnh báo **Vàng** (Rà soát). | Đỏ / Vàng | Nghị định 254/2026/NĐ-CP | Cần kiểm chứng điều khoản gốc. | "Các nội dung về tên, địa chỉ, mã số thuế của người mua, người bán phải được ghi chính xác theo đăng ký kinh doanh." (Diễn giải nguyên tắc) | Phân tách rõ hai cấp độ cảnh báo. Cảnh báo cấp độ 2 chỉ nên đề nghị "rà soát lại thông tin", không gợi ý hóa đơn không hợp lệ. | - Người mua là khách hàng cá nhân, không có MST.<br>- Sai sót chính tả nhỏ được chấp nhận trong thực tế. | **Đủ dùng cho cảnh báo kỹ thuật** |
| **3. VAT không khớp phép tính** | `IF Abs((pre_tax_amount * vat_rate) - vat_amount) > tolerance THEN` cảnh báo **Vàng**. | **Vàng** | Luật Thuế GTGT 48/2024/QH15 | Điều 15 | "Số thuế giá trị gia tăng được tính bằng giá tính thuế nhân với thuế suất thuế giá trị gia tăng tương ứng." | Giữ nguyên. Ghi chú rõ: `tolerance` (ví dụ: 1 VNĐ) là một **cấu hình kỹ thuật** do bộ phận nghiệp vụ quyết định, không phải là một ngưỡng pháp lý. | - Hàng hóa dịch vụ đặc thù có cách tính thuế riêng.<br>- Sai số làm tròn giữa các hệ thống phần mềm. | **Đủ dùng cho cảnh báo kỹ thuật** |
| **4. Hóa đơn ngoài kỳ kê khai** | `IF invoice_date` nằm ngoài khoảng thời gian của kỳ kê khai đang kiểm tra, đưa ra cảnh báo. | **Chỉ nhắc rà soát** | Nghị định 181/2025/NĐ-CP | Điều 25, Khoản 8 | "Trường hợp bỏ sót, được kê khai bổ sung vào các kỳ sau nhưng phải trước khi có quyết định thanh tra, kiểm tra thuế..." | Giữ nguyên. Thông điệp cảnh báo phải là: "Phát hiện hóa đơn ngoài kỳ đang kiểm tra, cần rà soát kỳ kê khai để đảm bảo không bỏ sót." | Không có. Rule này hoàn toàn mang tính hỗ trợ. | **Đủ dùng cho cảnh báo kỹ thuật** |
| **5. Hóa đơn giá trị lớn thiếu CTT KDTM*** | `IF total_amount >= 5,000,000 THEN` kiểm tra sự tồn tại của chứng từ thanh toán liên kết. Nếu không có, cảnh báo có điều kiện. | **Vàng** | Nghị định 181/2025/NĐ-CP | Điều 18, Khoản 3 | "Đối với các hóa đơn hàng hóa, dịch vụ có giá trị từ năm triệu đồng trở lên, cơ sở kinh doanh phải có chứng từ thanh toán không dùng tiền mặt..." | Cảnh báo phải nêu rõ: "Hóa đơn có giá trị từ 5 triệu, yêu cầu đối chiếu chứng từ thanh toán không dùng tiền mặt. Lưu ý các trường hợp ngoại lệ..." | - Trả chậm, trả góp (có hợp đồng).<br>- Bù trừ công nợ (có biên bản).<br>- Ủy quyền thanh toán (có hợp đồng).<br>- Nhân viên thanh toán hộ (có quy chế).<br>- Mua nhiều lần trong ngày từ cùng NCC (tổng giá trị > 5tr). | **Cần kiểm chứng thêm** |

*CTT KDTM: Chứng từ thanh toán không dùng tiền mặt.

---

## CÁC ĐIỂM ĐÃ SỬA SO VỚI BẢN V2

- **Phân vai trò Văn bản pháp lý:** Đã điều chỉnh lại, ưu tiên `Nghị định 254/2026/NĐ-CP` cho các case liên quan đến nội dung và tính hợp lệ của hóa đơn điện tử (Case 1, 2).
- **Case 1 (Hóa đơn trùng):** Đã loại bỏ hoàn toàn các kết luận mang tính pháp lý ("vi phạm", "bất hợp pháp"). Rule được định nghĩa lại theo các trạng thái kỹ thuật (`duplicate_file`, `duplicate_invoice_id`) và bổ sung đầy đủ các ngoại lệ cần loại trừ.
- **Case 2 (Sai MST):** Đã phân cấp mức độ cảnh báo rõ ràng hơn giữa sai MST (cao) và sai lệch nhỏ về tên/địa chỉ (thấp).
- **Case 3 (VAT không khớp):** Đã làm rõ `tolerance` là một tham số kỹ thuật, không phải là một quy định pháp lý.
- **Case 5 (Thanh toán >5tr):** Đã bổ sung thêm ngoại lệ "mua hàng nhiều lần trong ngày" và nhấn mạnh lại đây là cảnh báo có điều kiện.
- **Cột "Kết luận":** Đã cập nhật giá trị thành "Đủ dùng cho cảnh báo kỹ thuật" để phản ánh đúng vai trò của TaxGPT là một công cụ hỗ trợ, không phải trọng tài pháp lý.

---

## QUYẾT ĐỊNH: CÓ ĐƯỢC ĐÁNH DẤU GD0-04 HOÀN THÀNH CHƯA?

**Chưa.**

**Lý do:** Toàn bộ căn cứ pháp lý trong tài liệu này (Luật 48/2024, NĐ 181/2025, NĐ 254/2026...) đều là **văn bản giả định** cho mục đích xây dựng luồng xử lý. Để GD0-04 được chính thức hoàn thành, các hành động sau là bắt buộc:

1.  **Con người phải kiểm chứng điều/khoản gốc:** Một chuyên gia pháp lý về thuế phải tìm và đối chiếu **điều/khoản/điểm chính xác** trong các văn bản pháp luật **thật** đang có hiệu lực.
2.  **Xác thực trích đoạn:** Các trích đoạn trong bảng trên chỉ là diễn giải nguyên tắc, không phải là trích dẫn nguyên văn. Cần thay thế bằng trích dẫn chính xác từ luật.

Do đó, tài liệu này chỉ có thể được coi là "Hoàn thành về mặt khung logic kỹ thuật", chưa thể "Hoàn thành về mặt pháp lý".
