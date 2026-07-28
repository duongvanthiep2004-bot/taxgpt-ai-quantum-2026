# KẾ HOẠCH THỰC HIỆN DỰ ÁN TaxGPT
## AI-Quantum Challenge 2026 — Học viện Tài chính

**Ngày lập kế hoạch:** 06/07/2026
**Hạn nộp hồ sơ Vòng 1:** 30/07/2026 → **còn 24 ngày**

---

## 0. NGUYÊN TẮC PHÂN CÔNG CÔNG CỤ AI

Ba công cụ có thế mạnh khác nhau. Dùng sai công cụ cho sai việc sẽ mất thời gian và dễ tạo ra nội dung "AI viết hộ toàn bộ" — vi phạm Điều 14 của thể lệ. Nguyên tắc chung: **AI hỗ trợ tư duy và tăng tốc, người trong đội ra quyết định và chỉnh sửa cuối cùng.**

| Công cụ | Vai trò chính | Không nên dùng để |
|---|---|---|
| **ChatGPT Plus** | Brainstorm, viết/chỉnh văn bản (mô tả ý tưởng, báo cáo, slide script), đóng vai BGK để phản biện thử, tạo dữ liệu giả lập (hóa đơn mẫu, tình huống thuế) | Viết toàn bộ báo cáo cuối rồi nộp nguyên văn |
| **Gemini Pro** | Xử lý tài liệu dài (nhiều văn bản luật thuế/VAT cùng lúc nhờ context window lớn), tóm tắt/đối chiếu chéo điều luật, đọc ảnh hóa đơn scan để test OCR sơ bộ | Làm nguồn duy nhất cho căn cứ pháp lý — luôn đối chiếu với văn bản luật gốc |
| **VSCode AI (Copilot/Cursor…)** | Viết code thật: parser XML/PDF, rule engine, RAG pipeline, dashboard, debug, viết test | Thiết kế nghiệp vụ thuế (đội phải tự xác định rule, AI chỉ code theo) |

**Lưu ý bắt buộc:** Điều 5 thể lệ yêu cầu khai báo công cụ AI đã dùng khi chuẩn bị hồ sơ. Từ hôm nay, hãy lập một file `AI_usage_log.md` ghi lại: ngày dùng, công cụ, mục đích, phần nào con người chỉnh sửa lại. Việc này giúp bạn viết mục khai báo AI trong hồ sơ dễ dàng và minh bạch, tránh bị nghi ngờ vi phạm Điều 14.

---

## 1. GIAI ĐOẠN 0 — CHUẨN BỊ NỀN TẢNG (06/07 – 12/07, tuần này)

**Mục tiêu:** Chốt đội, chốt bài toán, dựng khung làm việc.

- [ ] Chốt danh sách đội (3–5 người), phân vai trò theo mẫu ở phần 8 (đã thống nhất trước đó: nghiệp vụ thuế / AI-backend / dashboard-pitch), cân nhắc mời giảng viên hướng dẫn.
- [ ] Tạo workspace dùng chung: 1 repo Git (để VSCode AI làm việc), 1 thư mục tài liệu chung (Google Drive/Notion) chứa: bản mô tả ý tưởng, dữ liệu mẫu, văn bản luật, log dùng AI.
- [ ] Dùng **ChatGPT Plus**: brainstorm nhanh danh sách 8–10 rủi ro thuế phổ biến ở SMEs, sau đó đội tự chọn ra 3–5 case khả thi nhất để làm demo (đã có gợi ý 5 case ở lần phân tích trước — dùng làm điểm khởi đầu, không cần làm lại từ đầu).
- [ ] Dùng **Gemini Pro**: upload các văn bản luật thuế/VAT liên quan đến 5 case đã chọn (ví dụ: quy định về ô tô >1,6 tỷ, điều kiện chứng từ khấu trừ, hóa đơn hợp lệ) để Gemini tóm tắt và trích đúng điều/khoản — đây là bước dựng "ngân hàng kiến thức pháp lý" ban đầu cho RAG.
- [ ] Cài môi trường code: Python, FastAPI, Streamlit, ChromaDB — để VSCode AI có thể bắt đầu code ngay tuần sau.

**Output tuần này:** danh sách case đã chốt, khung repo, danh sách văn bản luật cần dùng.

---

## 2. GIAI ĐOẠN 1 — HỒ SƠ VÒNG 1 (06/07 – 30/07) ⚠️ ƯU TIÊN CAO NHẤT

Hồ sơ Vòng 1 theo Điều 5 gồm: Phiếu đăng ký (theo mẫu) + Bản mô tả ý tưởng (vấn đề cần giải quyết, phương pháp AI dự kiến và lý do chọn, nguồn dữ liệu dự kiến, tính mới/tính khả thi, khai báo công cụ AI đã dùng).

Tiêu chí chấm Vòng 1 quan trọng nhất: **"Mức độ rõ ràng và đúng đắn của bài toán thực tiễn" chiếm 25%** — trọng số cao nhất trong toàn vòng. Vì vậy tuần đầu nên dồn lực vào việc mô tả bài toán thật sắc, có số liệu/dẫn chứng, hơn là vẽ kiến trúc kỹ thuật cầu kỳ.

### Tuần 1 (07/07 – 13/07): Xác định bài toán
- Viết draft mô tả vấn đề bằng **ChatGPT Plus**: nêu rõ SMEs gặp khó khăn gì cụ thể (số liệu về tỷ lệ sai sót kê khai, chi phí bị loại trừ do chứng từ không hợp lệ — nếu tìm được thống kê công khai thì trích, không thì nêu là quan sát thực tế phổ biến).
- Dùng **Gemini Pro** đối chiếu: kiểm tra các con số/điều luật ChatGPT nêu ra có đúng văn bản gốc không (bước chống hallucination chéo giữa 2 mô hình).

### Tuần 2 (14/07 – 20/07): Viết bản mô tả ý tưởng + sơ đồ
- Hoàn thiện bản mô tả ý tưởng theo đúng 4 mục Điều 5 yêu cầu.
- Vẽ sơ đồ kiến trúc (đã có sẵn workflow từ lần phân tích trước: Upload → Đọc dữ liệu → Rule Engine → RAG → LLM → Dashboard) — dùng ChatGPT Plus để viết mô tả từng bước súc tích cho phiếu đăng ký.
- Bắt đầu để **VSCode AI** dựng khung code rỗng (skeleton): cấu trúc thư mục backend/frontend, chưa cần chạy được, chỉ cần sẵn sàng để tuần sau code thật — việc này không bắt buộc cho Vòng 1 nhưng giúp Vòng 2 khởi động nhanh hơn.

### Tuần 3 (21/07 – 27/07): Phản biện và chỉnh sửa
- Dùng **ChatGPT Plus đóng vai giám khảo khó tính**: yêu cầu nó chấm thử bản mô tả ý tưởng theo đúng bảng tiêu chí Vòng 1 (6 tiêu chí, trọng số như trong thể lệ) và chỉ ra điểm yếu.
- Chỉnh sửa dựa trên phản biện, đặc biệt củng cố phần "tính khả thi của dữ liệu" (15%) — chuẩn bị sẵn ví dụ dữ liệu mẫu (hóa đơn giả lập) để chứng minh đã có dữ liệu, không chỉ nói suông.

### Tuần 4 (28/07 – 30/07): Hoàn thiện và nộp
- Rà soát chính tả, format, đúng mẫu phiếu đăng ký.
- Viết mục khai báo công cụ AI dựa trên `AI_usage_log.md` đã ghi từ đầu.
- Nộp hồ sơ trước 30/07, không để sát giờ chót vì hệ thống nộp online có thể quá tải.

---

## 3. GIAI ĐOẠN CHỜ (30/07 – 20/08): Chuẩn bị trước cho Vòng 2

Đây là thời gian "chết" về mặt thi đấu (chờ kết quả) nhưng đừng để lãng phí — vì Vòng 2 chỉ có 6 tuần và bạn có tối đa 20 đội cạnh tranh.

- Dùng thời gian này để **VSCode AI** bắt đầu code thật các module không phụ thuộc kết quả: đọc XML hóa đơn, đọc PDF, chuẩn hóa dữ liệu, rule engine cơ bản cho 5 case đã chọn.
- Dùng **Gemini Pro** tiếp tục mở rộng ngân hàng văn bản pháp luật (thêm các tình huống case 2–5), chuẩn bị sẵn dữ liệu để nạp vào ChromaDB.
- 09/08: phỏng vấn sơ loại (nếu được gọi) — luyện trả lời bằng cách để **ChatGPT Plus** đóng vai giám khảo đặt câu hỏi phản biện, đội trả lời và ghi âm để tự rút kinh nghiệm.
- 20/08: công bố kết quả Vòng 1.

---

## 4. GIAI ĐOẠN 2 — VÒNG 2: XÂY DỰNG PROTOTYPE (25/08 – 10/10, 6 tuần)

Sản phẩm cần nộp: báo cáo giải pháp 8–12 trang, slide, prototype chạy được, mã nguồn/hướng dẫn cài đặt. Tiêu chí nặng nhất: **"Chất lượng prototype" 20%** và **"Chất lượng dữ liệu"15%** — ưu tiên chạy ổn định hơn là nhiều tính năng.

| Tuần | Nội dung | Công cụ chính |
|---|---|---|
| Tuần 1 (25/08–31/08) | Kick-off BTC, chốt phạm vi 5 case, hoàn thiện workflow | ChatGPT Plus (viết tài liệu), Gemini Pro (rà luật) |
| Tuần 2 (01/09–07/09) | Code module đọc XML/PDF/Excel, chuẩn hóa bảng hóa đơn | VSCode AI |
| Tuần 3 (08/09–14/09) | Code rule engine cho 5 case rủi ro | VSCode AI, ChatGPT Plus (viết logic nghiệp vụ dạng pseudo-code trước khi code) |
| Tuần 4 (15/09–21/09) | Xây RAG: nạp văn bản luật vào ChromaDB, tách chunk theo điều/khoản, gắn metadata hiệu lực | Gemini Pro (chuẩn bị & rà soát nội dung luật), VSCode AI (code pipeline) |
| Tuần 5 (22/09–28/09) | Xây dashboard 3 màn hình (upload, bảng cảnh báo, căn cứ pháp lý), tích hợp LLM sinh giải thích có trích dẫn | VSCode AI |
| Tuần 6 (29/09–10/10) | Test 15–20 tình huống, sửa lỗi, viết báo cáo 8–12 trang, làm slide, quay video demo dự phòng | ChatGPT Plus (viết báo cáo/slide script), VSCode AI (fix bug) |

**Cơ chế chống AI bịa luật (phải thể hiện rõ trong báo cáo):** mỗi câu trả lời của hệ thống phải có citation; nếu RAG không tìm thấy văn bản phù hợp, hệ thống phải từ chối trả lời thay vì tự bịa — đây là điểm khác biệt cạnh tranh quan trọng nhất của TaxGPT, cần làm chắc.

25/08: kick-off & training chung 20 đội. 10/10: hạn nộp sản phẩm Vòng 2. 25/10: thuyết trình chọn 6 đội vào chung kết.

---

## 5. GIAI ĐOẠN 3 — CHUẨN BỊ THUYẾT TRÌNH VÒNG 2 (đến 25/10)

- Luyện pitch bằng cách để **ChatGPT Plus** đóng vai BGK, đặt câu hỏi phản biện dựa đúng 6 tiêu chí Vòng 2 (mức độ làm rõ bài toán, chất lượng dữ liệu, tính hợp lý giải pháp, chất lượng prototype, khả năng ứng dụng, trình bày).
- Chuẩn bị kịch bản demo dự phòng (video quay sẵn) — phòng trường hợp lỗi mạng/thiết bị khi thuyết trình trực tiếp.

---

## 6. GIAI ĐOẠN 4 — CHUNG KẾT (đến 10/11)

Mỗi đội có tối đa 10 phút trình bày + 8 phút hỏi đáp. Cấu trúc pitch 10 phút đã đề xuất trước đó (vấn đề → giải pháp → kiến trúc → demo → kết quả → mô hình kinh doanh → kết luận) vẫn phù hợp.

- Dùng **ChatGPT Plus** luyện tập trả lời phản biện nhanh, đặc biệt về: rủi ro đạo đức/pháp lý của AI, khả năng thương mại hóa, và **lưu ý quan trọng về SHTT (Điều 16)** — nếu đạt giải, sản phẩm có thể thuộc quyền sở hữu của Học viện nếu được chọn phát triển tiếp, nên chuẩn bị câu trả lời rõ ràng nếu BGK hỏi về hướng thương mại hóa sau này.
- Chuẩn bị khu vực demo trực tiếp tại HT 700, có phương án dự phòng nếu mất kết nối mạng.

---

## 7. RỦI RO CẦN THEO DÕI XUYÊN SUỐT

1. **Thời gian gấp cho Vòng 1** — chỉ 24 ngày, không nên trì hoãn tuần đầu.
2. **Khai báo AI đầy đủ** — duy trì `AI_usage_log.md` suốt dự án, không chỉ lúc nộp hồ sơ.
3. **Không để AI bịa căn cứ pháp lý** — mọi câu trả lời của TaxGPT phải truy vết được về văn bản luật thật; đây vừa là yêu cầu đạo đức vừa là tiêu chí chấm điểm.
4. **Không làm quá rộng** — thể lệ nêu rõ mô hình đơn giản nhưng chạy ổn định được đánh giá cao hơn mô hình phức tạp không triển khai được.
5. **Điều khoản SHTT** — cân nhắc kỹ trước khi đầu tư sâu vào hướng thương mại hóa nếu có ý định giữ quyền sở hữu sản phẩm về sau.

---

*File này nên được cập nhật hàng tuần khi có tiến độ mới hoặc khi BTC điều chỉnh lịch (thể lệ ghi rõ BTC có quyền điều chỉnh thời gian).*
