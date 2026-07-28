# GD1-03 — Kế hoạch dữ liệu mẫu cho TaxGPT

## 1. Mục tiêu dữ liệu mẫu

Bộ dữ liệu được xây dựng để minh họa khả năng rà soát năm case MVP của TaxGPT bằng các tình huống đơn giản, dễ đọc và có kết quả kỳ vọng rõ ràng. Toàn bộ hóa đơn, giao dịch thanh toán, mã số thuế, tên đơn vị và số chứng từ đều là dữ liệu giả lập; không sử dụng dữ liệu doanh nghiệp hoặc cá nhân thật.

Dữ liệu này phục vụ việc trình bày tính khả thi của MVP, chuẩn bị cho bước xây rule engine và kiểm thử Dashboard sau này. Các nhãn rủi ro trong file là kết quả kỳ vọng cho kiểm thử, không phải kết luận pháp lý.

## 2. Danh sách file dữ liệu mẫu

- `data-mau/excel/sample_invoices_mvp.xlsx`: 12 dòng hóa đơn giả lập trong sheet `invoices`.
- `data-mau/bank_statements/sample_bank_payments_mvp.xlsx`: 6 giao dịch thanh toán giả lập trong sheet `payments`.

## 3. Mapping dữ liệu với 5 case MVP

| Case | Dòng dữ liệu minh họa | Mục tiêu kiểm tra | Kết quả cảnh báo kỳ vọng |
|---|---|---|---|
| Đối chứng bình thường | `INV-DEMO-001`, `INV-DEMO-002` (dòng Excel 5–6) | Xác nhận dữ liệu hợp lệ không bị gắn nhãn rủi ro; payment reference khớp file thanh toán. | `NORMAL`; không tạo cảnh báo cho 5 case MVP. |
| 1. Hóa đơn trùng | `INV-DEMO-003`, `INV-DEMO-004` (dòng Excel 7–8) | So sánh số, ký hiệu, ngày hóa đơn, MST và tổng tiền để nhận diện hai bản ghi trùng. | `CASE_1_DUPLICATE`; yêu cầu người dùng xác minh bản ghi nhập lặp. |
| 2. Sai MST hoặc tên người mua | `INV-DEMO-005`, `INV-DEMO-006` (dòng Excel 9–10) | Phân biệt MST người mua sai với sai lệch nhỏ trong tên người mua. | `CASE_2_BUYER_INFO_MISMATCH`; hiển thị trường không khớp, không kết luận hóa đơn vô hiệu. |
| 3. VAT không khớp phép tính | `INV-DEMO-007`, `INV-DEMO-008` (dòng Excel 11–12) | Tính lại VAT từ giá trị chịu thuế và thuế suất rồi so sánh với số đã ghi. | `CASE_3_VAT_CALC_MISMATCH`; hiển thị số liệu và mức chênh lệch cần rà soát. |
| 4. Hóa đơn ngoài kỳ dữ liệu đang rà soát | `INV-DEMO-009`, `INV-DEMO-010` (dòng Excel 13–14) | So sánh ngày hóa đơn với kỳ dữ liệu demo `2026-07`. | `CASE_4_OUTSIDE_REVIEW_PERIOD`; gợi ý kiểm tra kỳ kê khai hoặc khả năng kê khai bổ sung, không kết luận vi phạm. |
| 5. Hóa đơn giá trị lớn thiếu chứng từ thanh toán không dùng tiền mặt | `INV-DEMO-011`, `INV-DEMO-012` (dòng Excel 15–16) | Đối chiếu hóa đơn giá trị lớn với payment reference và file giao dịch thanh toán. | `CASE_5_MISSING_NONCASH_PAYMENT`; cảnh báo chưa tìm thấy chứng từ phù hợp. Hai hóa đơn này không có payment reference và không có giao dịch tương ứng trong sheet `payments`. |

**Giả định cấu hình khi phát triển rule engine:**

- Case 2 dùng hồ sơ người mua tham chiếu gồm MST `FAKE-BUYER-000` và tên `Công ty TaxGPT Demo`.
- Case 5 cần một ngưỡng demo do người phụ trách nghiệp vụ cấu hình như tham số kỹ thuật. Không được suy ra ngưỡng pháp lý từ giá trị của các hóa đơn mẫu.

## 4. Mô tả các cột dữ liệu

### 4.1. Sheet `invoices`

| Cột | Mô tả |
|---|---|
| `invoice_id` | Mã duy nhất của bản ghi trong bộ dữ liệu demo. |
| `invoice_no`, `invoice_symbol` | Số và ký hiệu hóa đơn giả lập, dùng để nhận diện và kiểm tra trùng. |
| `invoice_date` | Ngày lập hóa đơn, dùng để đối chiếu kỳ dữ liệu đang rà soát. |
| `seller_tax_code`, `seller_name` | MST và tên người bán giả lập. |
| `buyer_tax_code`, `buyer_name` | MST và tên người mua giả lập, dùng cho case kiểm tra thông tin người mua. |
| `taxable_amount` | Giá trị tính thuế được dùng làm đầu vào kiểm tra số học. |
| `vat_rate` | Thuế suất ghi trong dữ liệu demo. |
| `vat_amount` | Tiền VAT ghi nhận trên hóa đơn mẫu. |
| `total_amount` | Tổng giá trị hóa đơn mẫu. |
| `declaration_period` | Kỳ dữ liệu người dùng đang rà soát; không phải kết luận kỳ kê khai đúng về pháp lý. |
| `payment_method` | Phương thức thanh toán mô phỏng. |
| `bank_payment_ref` | Mã liên kết đến giao dịch trong file payments; để trống có chủ đích ở case 5. |
| `expected_risk_case` | Nhãn kết quả kỳ vọng để kiểm thử MVP. |
| `note` | Giải thích ngắn tình huống giả lập và lý do gắn nhãn. |

### 4.2. Sheet `payments`

| Cột | Mô tả |
|---|---|
| `payment_ref` | Mã giao dịch thanh toán giả lập, dùng để liên kết với `bank_payment_ref`. |
| `payment_date` | Ngày thanh toán giả lập. |
| `payer_name`, `payee_name` | Tên bên trả và bên nhận, đều là tên mô phỏng. |
| `amount` | Số tiền giao dịch giả lập. |
| `payment_method` | Phương thức thanh toán mô phỏng. |
| `related_invoice_no` | Số hóa đơn giả lập được liên kết với giao dịch. |
| `note` | Giải thích vai trò của giao dịch trong bộ dữ liệu demo. |

## 5. Nguyên tắc bảo mật và đạo đức dữ liệu

- Dữ liệu hoàn toàn giả lập và được tạo riêng cho TaxGPT.
- Không sử dụng hóa đơn, sao kê hoặc chứng từ thật.
- Không chứa thông tin cá nhân hoặc thông tin doanh nghiệp thật.
- Tên đơn vị, MST, số hóa đơn và mã thanh toán đều có dấu hiệu `Demo`, `Mô phỏng` hoặc `FAKE` để tránh nhầm lẫn.
- Bộ dữ liệu chỉ phục vụ demo và kiểm thử MVP, không dùng để kê khai, hạch toán hoặc đưa ra kết luận pháp lý.

## 6. Giới hạn dữ liệu mẫu

- Dữ liệu đã được đơn giản hóa để mỗi nhóm rủi ro có thể quan sát và giải thích rõ ràng.
- Bộ mẫu chưa phản ánh đầy đủ các loại hóa đơn, nghiệp vụ điều chỉnh/thay thế, nhiều thuế suất, thanh toán từng phần, bù trừ công nợ hoặc các tình huống ngoại lệ khác.
- Nhãn `expected_risk_case` là kỳ vọng kiểm thử kỹ thuật, không phải xác nhận vi phạm.
- Giá trị của các hóa đơn trong case 5 chỉ dùng để tạo tình huống demo, không đại diện cho ngưỡng pháp lý.
- Khi phát triển prototype thật, nhóm cần mở rộng số lượng mẫu, bổ sung trường hợp biên, kiểm chứng nguồn pháp lý và xây quy trình ẩn danh dữ liệu đầu vào.
