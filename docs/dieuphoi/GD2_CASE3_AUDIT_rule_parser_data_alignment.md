# GD2-CASE3-AUDIT — Đối chiếu rule, parser, dữ liệu và test Case 3

**Ngày audit:** 01/09/2026  
**Phạm vi:** Audit kỹ thuật chỉ đọc; không phải legal review.  
**Trạng thái kiểm soát:** Không sửa rule, parser, test, dữ liệu, legal draft hoặc RAG. RAG vẫn `LOCKED`.

## 1. Tóm tắt kết quả

| Hạng mục | Phát hiện | Phân loại |
|---|---|---|
| Công thức VAT hiện có | Rule kiểm tra `vat_amount` với `taxable_amount × vat_rate`, có chuẩn hóa thuế suất và tolerance mặc định `1.0` | Đã khớp với sample và test Case 3 hiện tại |
| `net_amount` | Parser biết và kiểm tra số nếu cột tồn tại, nhưng rule không đọc `net_amount` | Chưa khớp |
| `total_amount` | Parser bắt buộc cột này, nhưng rule Case 3 không dùng và không kiểm tra tổng tiền | Chưa khớp |
| Sample Excel | Có `taxable_amount`, `vat_rate`, `vat_amount`, `total_amount` và nhãn Case 3; không có `net_amount` | Đã khớp với rule hiện tại |
| Template Excel | Chỉ có `invoice_id`, `invoice_no`, `invoice_date`, `total_amount`; không đủ đầu vào cho Case 3 | Rủi ro cao |
| Điều kiện nhãn demo | Rule chỉ xử lý dòng có `expected_risk_case = CASE_3_VAT_CALC_MISMATCH` | Rủi ro cao đối với upload thực |
| Test chuyên biệt | Bao phủ sample dùng `taxable_amount`, công thức, evidence và message an toàn | Đã khớp trong phạm vi demo |
| Test upload | Upload sample thật và kiểm tra tổng `9` cảnh báo, nhưng không assert riêng Case 3 hoặc tình huống `net_amount` | Chưa đủ để bắt lỗi alignment |
| Legal review scaffold | Đã phân biệt logic mục tiêu với logic code và ghi rõ chưa kiểm tra tổng tiền | Cơ bản an toàn, nhưng phần mục tiêu có thể được làm rõ hơn |

**Kết luận ngắn:** Case 3 đang hoạt động với bộ sample được gắn nhãn sẵn, nhưng hợp đồng dữ liệu upload chưa thống nhất. Template hiện không cung cấp đầu vào cần thiết; parser không ánh xạ `net_amount` sang `taxable_amount`; rule lại không đọc `net_amount` và chỉ chạy trên dòng đã có nhãn rủi ro. Vì vậy chưa thể coi Case 3 là hoạt động đúng cho file upload thông thường.

## 2. Phạm vi và nguồn đã đọc

Đã đọc trực tiếp:

- `backend/app/rules/vat_mismatch.py`
- `backend/app/parsers/excel_parser.py`
- `backend/app/main.py` ở phần nối upload với `build_scan_result`
- `backend/tests/test_case_3_vat_mismatch.py`
- `backend/tests/test_scan_uploaded.py`
- `data-mau/excel/sample_invoices_mvp.xlsx`
- `data-mau/excel/template_invoices_mvp.xlsx`
- `van-ban-luat/processed/GD1_5_CASE3_internal_review_vat_mismatch.md`

Hai file Excel đã đọc được trực tiếp từ cấu trúc workbook. Không cần suy luận header từ parser/test.

## 3. Rule Case 3 hiện tại

### 3.1 Field được đọc

Rule đọc các field sau từ mỗi invoice:

- `expected_risk_case`: dùng để quyết định có chạy Case 3 cho dòng đó hay không.
- `taxable_amount`: giá trị tính thuế dùng trong phép tính.
- `vat_rate`: thuế suất.
- `vat_amount`: tiền thuế cần so sánh.
- `invoice_id`: đưa vào cảnh báo.
- `note`: đưa vào evidence.

Rule không đọc `net_amount` hoặc `total_amount`.

### 3.2 Điều kiện và công thức chính xác

1. Chuẩn hóa `expected_risk_case` bằng `strip().upper()`.
2. Bỏ qua dòng nếu nhãn không đúng `CASE_3_VAT_CALC_MISMATCH`.
3. Chuyển `taxable_amount`, `vat_rate`, `vat_amount` thành số hữu hạn; bỏ qua dòng nếu một trong ba giá trị không hợp lệ hoặc thiếu.
4. Chuẩn hóa thuế suất:
   - Nếu `vat_rate > 1`: dùng `vat_rate / 100`.
   - Nếu `vat_rate <= 1`: dùng trực tiếp.
5. Tính `recalculated_vat = taxable_amount × normalized_vat_rate`.
6. Tính `difference = abs(vat_amount - recalculated_vat)`.
7. Chỉ cảnh báo khi `difference > tolerance`.

Trả lời trực tiếp:

- Có kiểm tra `vat_amount` với `taxable_amount × vat_rate`: **Có**.
- Có kiểm tra `vat_amount` với `net_amount × vat_rate`: **Không**.
- Có kiểm tra `total_amount = net_amount + vat_amount`: **Không**.
- Tolerance mặc định: **`1.0`**, theo đơn vị số tiền của dữ liệu; đây là tham số kỹ thuật, không phải ngưỡng pháp luật.

### 3.3 Message hiện tại

Message trong code:

> Số tiền VAT có dấu hiệu không khớp với phép tính kỹ thuật từ giá trị tính thuế và thuế suất, cần người dùng rà soát lại.

Message này là cảnh báo kỹ thuật và không kết luận sai phạm. Nội dung phù hợp với công thức đang triển khai vì không nói rule đã kiểm tra `total_amount`.

## 4. Parser hóa đơn hiện tại

### 4.1 Cột bắt buộc

`REQUIRED_INVOICE_COLUMNS` gồm đúng bốn cột:

- `invoice_id`
- `invoice_no`
- `invoice_date`
- `total_amount`

Parser tìm header dựa trên các cột này, bắt buộc giá trị của bốn cột không được trống, parse `invoice_date`, và kiểm tra `total_amount` là số.

### 4.2 Cách parser xử lý field

- Parser đọc toàn bộ cột có trong sheet `invoices`, không chỉ bốn cột bắt buộc.
- Tên cột được chuyển thành chuỗi và loại bỏ khoảng trắng hai đầu.
- Parser giữ nguyên tên cột khi chuyển từng dòng thành `dict`.
- Parser không tạo `taxable_amount`.
- Parser không tạo `net_amount`.
- Parser không đổi tên `net_amount` thành `taxable_amount`.
- `INVOICE_AMOUNT_COLUMNS` gồm `net_amount`, `vat_amount`, `total_amount`; parser chỉ kiểm tra kiểu số cho các cột này nếu chúng tồn tại.
- `taxable_amount` và `vat_rate` không nằm trong `INVOICE_AMOUNT_COLUMNS`, nên parser không kiểm tra kiểu số của hai field này. Rule tự thử chuyển chúng sang số và âm thầm bỏ qua dòng nếu chuyển đổi thất bại.

**Hệ quả:** Parser và rule không có một bước chuẩn hóa schema chung cho giá trị tính thuế. Dữ liệu mang tên `net_amount` vẫn đi qua parser nhưng Case 3 không sử dụng; dữ liệu mang tên `taxable_amount` được rule sử dụng nhưng parser không validate như một cột số.

## 5. Dữ liệu mẫu và template

### 5.1 Sample `sample_invoices_mvp.xlsx`

Header tại dòng Excel 4 gồm:

`invoice_id`, `invoice_no`, `invoice_symbol`, `invoice_date`, `seller_tax_code`, `seller_name`, `buyer_tax_code`, `buyer_name`, `taxable_amount`, `vat_rate`, `vat_amount`, `total_amount`, `declaration_period`, `payment_method`, `bank_payment_ref`, `expected_risk_case`, `note`.

- Có `taxable_amount`.
- Không có `net_amount`.
- Hai dòng Case 3 là `INV-DEMO-007` và `INV-DEMO-008`.
- Cả hai dùng `taxable_amount`, `vat_rate`, `vat_amount`, `total_amount` và nhãn `CASE_3_VAT_CALC_MISMATCH`.
- `INV-DEMO-007`: `8.000.000 × 10% = 800.000`, trong khi `vat_amount = 700.000`.
- `INV-DEMO-008`: `12.000.000 × 8% = 960.000`, trong khi `vat_amount = 900.000`.

Sample khớp với rule hiện tại và giải thích vì sao test chuyên biệt tìm được đúng hai cảnh báo.

### 5.2 Template `template_invoices_mvp.xlsx`

Template chỉ có:

- `invoice_id`
- `invoice_no`
- `invoice_date`
- `total_amount`

Template không có `taxable_amount`, `net_amount`, `vat_rate`, `vat_amount`, `expected_risk_case` hoặc `note`.

### 5.3 Rủi ro upload

Có rủi ro rõ ràng, gồm hai lớp:

1. File tạo đúng theo template hiện tại không có đủ field để Case 3 tính VAT; rule sẽ không phát cảnh báo.
2. Nếu người dùng tự bổ sung `net_amount`, `vat_rate`, `vat_amount`, parser vẫn giữ `net_amount` nhưng rule tìm `taxable_amount`; dòng tiếp tục bị bỏ qua.

Ngoài ra, ngay cả file có `taxable_amount`, `vat_rate`, `vat_amount` cũng không được Case 3 xử lý nếu thiếu nhãn `expected_risk_case` đúng giá trị. Đây là thiết kế phù hợp cho dữ liệu demo gắn nhãn trước, nhưng không phù hợp với mục tiêu phát hiện rủi ro từ upload thực.

## 6. Test Case 3 hiện tại

### 6.1 `test_case_3_vat_mismatch.py`

- Ba test chính đọc sample Excel có field `taxable_amount` và nhãn Case 3.
- Test dữ liệu tạo trực tiếp cũng dùng `taxable_amount`, không dùng `net_amount`.
- Test xác nhận hai invoice mẫu bị cảnh báo.
- Test xác nhận `recalculated_vat` và `difference`.
- Test xác nhận thuế suất dạng `10` được hiểu là `10%`.
- Test xác nhận cấu trúc evidence và loại một số wording pháp lý không an toàn.
- Không có test dùng `net_amount`.
- Không có test thiếu `expected_risk_case` nhưng vẫn có sai lệch VAT.
- Không có test cho `total_amount = net_amount + vat_amount`.

### 6.2 `test_scan_uploaded.py`

Test `test_scan_uploaded_returns_same_totals_as_demo` upload thật file sample, đi qua parser, endpoint `/demo/scan-uploaded`, `build_scan_result` và rule Case 3. Tuy nhiên test chỉ assert tổng cộng `9` cảnh báo và `5` mục case summary; không assert riêng:

- Case 3 có đúng `2` cảnh báo.
- Invoice Case 3 là `INV-DEMO-007` và `INV-DEMO-008`.
- Evidence Case 3 dùng field nào.
- Upload có `net_amount` nhưng không có `taxable_amount` sẽ được xử lý ra sao.
- Upload theo đúng template có đủ dữ liệu cho Case 3 hay không.
- Sai lệch `total_amount` có bị phát hiện hay không.

Test template chỉ xác nhận parser đọc được một dòng và tập field trả về đúng bằng `REQUIRED_INVOICE_COLUMNS`. Điều này xác nhận template tối giản hợp lệ với parser, nhưng đồng thời xác nhận template không có đầu vào Case 3.

**Kết luận test:** Test hiện tại chứng minh luồng demo gắn nhãn sẵn hoạt động. Test chưa bắt được lỗi alignment `taxable_amount`/`net_amount`, chưa chứng minh Case 3 hoạt động với upload thông thường, và chưa kiểm tra tổng tiền.

## 7. Đối chiếu legal review scaffold

File `GD1_5_CASE3_internal_review_vat_mismatch.md` hiện:

- Mô tả phạm vi mục tiêu gồm so sánh `vat_amount` với `net_amount × vat_rate` và `total_amount` với `net_amount + vat_amount`.
- Ngay sau đó ghi đúng rằng code đang dùng `taxable_amount`, tolerance `1.0`, chưa kiểm tra tổng tiền và cần đối chiếu khác biệt tên field.
- Ghi rõ ngưỡng là tham số kỹ thuật, không phải ngưỡng pháp luật.
- Giữ legal confidence ở `Pending` và RAG ở `LOCKED`.

Không có câu khẳng định trực tiếp rằng rule hiện tại đã kiểm tra `total_amount`. Tuy nhiên, đoạn “Ở mức khái quát, Case 3 hướng tới...” và phần mục tiêu nhắc “tổng thanh toán” có thể bị đọc tách khỏi phần giải thích phía dưới và bị hiểu nhầm là tính năng đã triển khai.

Khuyến nghị ở bước tài liệu sau audit:

- Đổi nhãn đoạn đầu thành **“Logic mục tiêu/chưa triển khai đầy đủ”**.
- Giữ một mục riêng **“Logic thực tế trong code hiện tại”**.
- Ghi ngay cạnh phép kiểm tra tổng tiền: **“Chưa có trong rule hiện tại”**.

Chưa sửa file review trong bước audit này.

## 8. Kết luận audit theo phân loại

### Đã khớp

- Rule, sample Excel và test chuyên biệt cùng dùng `taxable_amount`.
- Công thức thực thi, tolerance và evidence trong test khớp code.
- Message hiện tại là cảnh báo kỹ thuật an toàn.
- Legal review scaffold đã nhận diện sự khác biệt tên field và việc chưa kiểm tra tổng tiền.

### Chưa khớp

- Parser định nghĩa `net_amount` là cột số tùy chọn, trong khi rule chỉ đọc `taxable_amount`.
- Template không có field đầu vào cho Case 3.
- Parser không normalize `net_amount`/`taxable_amount` và không validate số cho `taxable_amount`, `vat_rate`.
- Mục tiêu Case 3 có nhắc tổng tiền nhưng rule chưa kiểm tra `total_amount`.

### Rủi ro

- Case 3 có thể âm thầm không chạy với file upload theo template.
- Dòng dùng `net_amount` có thể bị bỏ qua dù có đủ thuế suất và tiền thuế.
- Dòng không có nhãn demo `expected_risk_case` luôn bị bỏ qua; đây là rủi ro lớn nhất đối với chức năng phát hiện trên dữ liệu người dùng.
- Field thiếu hoặc không parse được bị rule bỏ qua mà không sinh lỗi/cảnh báo chất lượng dữ liệu Case 3.
- Test tổng `9` cảnh báo có thể không chỉ rõ hồi quy riêng của Case 3.
- `total_amount` bắt buộc ở parser có thể tạo cảm giác đã được dùng trong Case 3 dù thực tế chưa dùng.

### Khuyến nghị sửa

- Chốt một hợp đồng schema rõ ràng cho giá trị tính thuế trước khi sửa rule.
- Tách nhãn dữ liệu demo khỏi điều kiện kích hoạt phát hiện trong luồng upload thực.
- Đồng bộ parser, template, sample, rule và test theo cùng hợp đồng field.
- Bổ sung test Case 3 qua upload ở bước triển khai sau; không chỉ assert tổng số cảnh báo.
- Chỉ bổ sung kiểm tra tổng tiền sau khi xác định rõ ngữ nghĩa field, tolerance và ngoại lệ làm tròn.

## 9. Phương án xử lý tiếp theo

### Phương án A — Giữ `taxable_amount` là tên chuẩn

- Giữ công thức rule hiện tại.
- Bổ sung `taxable_amount`, `vat_rate`, `vat_amount` vào schema/template phù hợp.
- Cho parser validate các field này và tài liệu hóa rõ.
- Cập nhật sample/test/template đồng bộ.

**Ưu điểm:** Ít thay đổi rule, tên field sát với “giá trị tính thuế”.  
**Nhược điểm:** Phải thay hợp đồng upload hiện đang có dấu hiệu dùng `net_amount`; cần quyết định cách xử lý file cũ.

### Phương án B — Dùng `net_amount` làm tên chuẩn

- Đổi rule sang đọc `net_amount`.
- Đổi sample Case 3 từ `taxable_amount` sang `net_amount`.
- Bổ sung `net_amount`, `vat_rate`, `vat_amount` vào template và test upload.

**Ưu điểm:** Khớp với `INVOICE_AMOUNT_COLUMNS` hiện tại.  
**Nhược điểm:** `net_amount` có thể không luôn đồng nghĩa với giá tính thuế trong mọi ngoại lệ nghiệp vụ; cần chốt định nghĩa trước.

### Phương án C — Mapping rõ ràng về một field nội bộ chuẩn

- Chọn một tên nội bộ duy nhất, ưu tiên `taxable_amount` nếu ý nghĩa là giá trị làm căn cứ tính VAT.
- Parser chấp nhận có kiểm soát `taxable_amount` hoặc alias `net_amount`, rồi normalize về field nội bộ.
- Nếu cả hai field cùng tồn tại nhưng khác nhau, trả lỗi dữ liệu rõ ràng; không fallback âm thầm.
- Template chỉ trình bày một tên chuẩn và giải thích ngữ nghĩa.
- Rule chỉ đọc field nội bộ đã normalize.

**Ưu điểm:** Có đường chuyển tiếp và tránh logic fallback mơ hồ.  
**Nhược điểm:** Cần thêm validation và test mapping/conflict.

### Phương án D — Bổ sung kiểm tra tổng tiền

Có thể bổ sung `abs(total_amount - (taxable_amount + vat_amount)) > tolerance` dưới dạng một phép kiểm tra kỹ thuật riêng. Không nên gộp ngay nếu chưa chốt:

- Field chuẩn cho giá trị tính thuế.
- Cách xử lý nhiều dòng/mức thuế suất, chiết khấu, điều chỉnh và làm tròn.
- Dùng chung hay tách tolerance cho tiền thuế và tổng tiền.
- Wording/evidence riêng để người dùng biết phép kiểm tra nào bị lệch.

## 10. Khuyến nghị cụ thể cho bước sửa code tiếp theo

Khuyến nghị ưu tiên **Phương án C**, triển khai theo thứ tự:

1. Chốt `taxable_amount` là field nội bộ chuẩn, đồng thời xác nhận định nghĩa nghiệp vụ trước khi code.
2. Cho parser normalize alias `net_amount` về `taxable_amount` với kiểm tra xung đột rõ ràng; validate `taxable_amount`, `vat_rate`, `vat_amount` khi Case 3 có thể chạy.
3. Loại bỏ sự phụ thuộc vào `expected_risk_case` trong luồng phát hiện upload thực; nếu cần giữ nhãn, chỉ dùng cho fixture/đánh giá kỳ vọng của demo.
4. Cập nhật template để có đầu vào Case 3 rõ ràng và cập nhật sample theo schema đã chốt.
5. Ở bước test sau, thêm test unit và upload cho `taxable_amount`, alias `net_amount`, xung đột hai field, thiếu field, dòng không có nhãn demo và assertion riêng Case 3.
6. Sau khi alignment trên ổn định, cân nhắc Phương án D như một cảnh báo kỹ thuật riêng.

**Có cần sửa code ở bước sau:** Có. Ít nhất cần sửa hợp đồng parser/rule và điều kiện nhãn trước khi tuyên bố Case 3 hỗ trợ upload thực. Việc sửa code không nằm trong phạm vi audit hiện tại.
