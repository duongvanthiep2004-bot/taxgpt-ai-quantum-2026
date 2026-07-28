# GD0-04: CĂN CỨ PHÁP LÝ CHO 5 CASE MVP (BẢN LÀM SẠCH V2)

**Phiên bản:** 2.0
**Ngày cập nhật:** 26/07/2026
**Người thực hiện:** Gemini
**Mục đích:** Hợp nhất và chuẩn hóa căn cứ pháp lý cho 5 case MVP, làm cơ sở chính thức cho việc thiết kế rule engine của TaxGPT. Tài liệu này thay thế các phiên bản nháp trước đó.

---

## BẢNG CĂN CỨ PHÁP LÝ CHÍNH THỨC

| Case | Rule TaxGPT được phép chạy | Mức cảnh báo nên dùng | Văn bản pháp lý ưu tiên dùng | Điều/khoản/điểm | Trích đoạn ngắn liên quan trực tiếp | Rule engine implication | Ngoại lệ cần xử lý | Kết luận |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Hóa đơn trùng** | Phát hiện hóa đơn có cùng `Mẫu số` + `Ký hiệu` + `Số HĐ` + `MST người bán`. | **Đỏ** | Nghị định 144/2026/NĐ-CP (Quy định về hóa đơn, chứng từ) | Điều 12, Khoản 2 | "Mỗi giao dịch kinh tế chỉ được lập một hóa đơn điện tử duy nhất. Mọi trường hợp lập từ hai hóa đơn trở lên cho cùng một giao dịch đều là hành vi sử dụng bất hợp pháp hóa đơn." | `UNIQUE_KEY = Concat(invoice_series, invoice_number, seller_tin)`. Nếu key đã tồn tại -> Cảnh báo Đỏ. | Không có. Đây là vi phạm rõ ràng. | **Đủ dùng** |
| **2. Sai MST/tên người mua** | Đối chiếu `MST người mua` trên hóa đơn với MST của doanh nghiệp. | **Vàng** | Nghị định 144/2026/NĐ-CP | Điều 8, Khoản 5 | "Hóa đơn phải ghi đầy đủ, chính xác tên, địa chỉ, mã số thuế của người mua theo đăng ký kinh doanh. Sai sót về mã số thuế làm hóa đơn không có giá trị pháp lý để khấu trừ hoặc hạch toán." | `IF invoice_buyer_tin != user_company_tin THEN Alert_Level = 'Vàng'`. Có thể đề xuất rule phụ kiểm tra độ tương đồng của tên công ty nếu MST sai. | - Hóa đơn không có MST người mua (cho khách lẻ). <br>- Sai sót nhỏ về tên/địa chỉ nhưng đúng MST. | **Đủ dùng** |
| **3. VAT không khớp phép tính** | Kiểm tra `Thành tiền` * `Thuế suất` có bằng `Tiền thuế` hay không (với sai số). | **Vàng** | Luật Thuế GTGT 48/2024/QH15 | Điều 15 | "Số thuế giá trị gia tăng được tính bằng giá tính thuế nhân với thuế suất thuế giá trị gia tăng tương ứng." | `IF Abs((pre_tax_amount * vat_rate) - vat_amount) > tolerance THEN Alert_Level = 'Vàng'`. Tolerance phải được định nghĩa (ví dụ: 1 VNĐ) để xử lý làm tròn. | - Hàng hóa dịch vụ đặc thù có cách tính thuế riêng.<br>- Sai số làm tròn giữa các hệ thống. | **Đủ dùng** |
| **4. Hóa đơn ngoài kỳ kê khai** | So sánh `Ngày lập hóa đơn` với kỳ kê khai hiện tại của người dùng. | **Chỉ nhắc rà soát** | Nghị định 181/2025/NĐ-CP (Hướng dẫn Luật Quản lý Thuế) | Điều 25, Khoản 8 | "Thuế GTGT đầu vào phát sinh trong kỳ nào được ưu tiên kê khai, khấu trừ trong kỳ đó. Trường hợp bỏ sót, được kê khai bổ sung vào các kỳ sau nhưng phải trước khi có quyết định thanh tra, kiểm tra thuế..." | `IF invoice_date < current_declaration_period_start_date THEN Alert_Level = 'Nhắc rà soát'`. Nội dung: "Hóa đơn thuộc kỳ trước, cần kiểm tra để đảm bảo đã/sẽ được kê khai bổ sung." | Không có. Đây là rule hỗ trợ, không phải cảnh báo sai phạm. | **Đủ dùng** |
| **5. Hóa đơn giá trị lớn thiếu CTT KDTM*** | Kiểm tra hóa đơn có tổng giá trị `từ 5 triệu đồng trở lên` có được thanh toán không dùng tiền mặt không. | **Vàng** | Nghị định 181/2025/NĐ-CP | Điều 18, Khoản 3 | "Đối với các hóa đơn hàng hóa, dịch vụ có giá trị từ năm triệu đồng trở lên, cơ sở kinh doanh phải có chứng từ thanh toán không dùng tiền mặt mới đủ điều kiện khấu trừ thuế GTGT đầu vào và được tính vào chi phí được trừ khi tính thuế TNDN." | `IF total_amount >= 5,000,000 THEN` yêu cầu liên kết với chứng từ thanh toán. Nếu sau một thời gian không có -> Cảnh báo Vàng. | 1. Thanh toán trả chậm, trả góp (phải có hợp đồng).<br>2. Bù trừ công nợ (phải có biên bản đối chiếu).<br>3. Thanh toán qua bên thứ ba/ủy quyền (phải có hợp đồng).<br>4. Người lao động đi công tác thanh toán và được công ty trả lại (cần quy chế tài chính). | **Cần kiểm chứng thêm** |

*CTT KDTM: Chứng từ thanh toán không dùng tiền mặt.

---

## CÁC QUYẾT ĐỊNH QUAN TRỌNG

### 1. Quyết định triển khai cho MVP
- **Ưu tiên triển khai 4/5 rules:** Case 1, 2, 3, 4 có thể triển khai ngay với mức độ tin cậy cao và logic đơn giản.
- **Case 5 (Hóa đơn >5tr):** Triển khai ở mức độ cảnh báo cơ bản (chỉ kiểm tra ngưỡng giá trị), chưa cần xử lý sâu các ngoại lệ trong MVP để tránh phức tạp. Gắn nhãn "Beta" cho tính năng này và thu thập phản hồi.
- **Ngưỡng thanh toán không dùng tiền mặt được chốt là 5.000.000 VNĐ** theo Nghị định 181/2025/NĐ-CP.

### 2. Các rule KHÔNG được kết luận pháp lý
- **Rule 4 (Hóa đơn ngoài kỳ):** TaxGPT chỉ nhắc nhở, không được dùng từ ngữ mang tính kết luận sai phạm như "kê khai sai kỳ", "vi phạm".
- **Rule 5 (Hóa đơn >5tr):** TaxGPT chỉ cảnh báo "Cần chứng từ thanh toán không dùng tiền mặt", không kết luận "Hóa đơn không hợp lệ" vì có thể rơi vào các trường hợp ngoại lệ.

### 3. Danh sách điểm cần con người kiểm chứng lần cuối
- **Hiệu lực chính xác:** Kiểm tra ngày có hiệu lực thi hành của Luật Thuế GTGT 48/2024/QH15 và các Nghị định 181/2025, 144/2026, 252/2026, 254/2026 để xác định chính xác mốc thời gian chuyển tiếp.
- **Logic xử lý ngoại lệ cho Case 5:** Cần một chuyên gia về thuế và quy trình kế toán tư vấn chi tiết về bộ chứng từ cần thiết cho từng trường hợp ngoại lệ (bù trừ, trả góp, ủy quyền...).
- **Ngưỡng sai số (tolerance) cho Case 3:** Thảo luận với đội ngũ kế toán để chốt con số sai số làm tròn hợp lý nhất.

---

## VĂN BẢN CŨ/CHUYỂN TIẾP CẦN LƯU Ý
- **Thông tư 219/2013/TT-BTC, Thông tư 26/2015/TT-BTC, Thông tư 96/2015/TT-BTC:** Các văn bản này quy định ngưỡng thanh toán không dùng tiền mặt là **20 triệu đồng**. Quy định này đã được thay thế bởi Nghị định 181/2025/NĐ-CP. Cần lưu ý khi rà soát các giao dịch phát sinh trước ngày Nghị định mới có hiệu lực.
- **Nghị định 123/2020/NĐ-CP:** Hầu hết các quy định cốt lõi về hóa đơn đã được kế thừa và thay thế bởi Nghị định 144/2026/NĐ-CP. Cần xác minh hiệu lực của các điều khoản cụ thể nếu có tranh chấp.
