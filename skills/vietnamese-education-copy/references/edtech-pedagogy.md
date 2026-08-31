<!-- vlc-disable: TONE001, DIA001 -->

# EdTech & Pedagogical Intelligence Guide

Hướng dẫn toàn diện về Khoa học Học tập (Learning Science), Đo lường Đánh giá, Trải nghiệm Động lực và Vi-tương tác Sư phạm trong các ứng dụng Công nghệ Giáo dục (EdTech) tiếng Việt.

---

## 1. Bản đồ Năng lực Sư phạm (5 Core Capabilities)

Hệ thống AI đóng vai trò như một **gia sư sư phạm thông minh (Pedagogical Intelligence)**, đảm nhận 5 module năng lực cốt lõi:

| Module Năng lực | Điều kiện kích hoạt (Trigger) | Đầu vào mẫu (Platform Telemetry) | Phản hồi AI mẫu (vi-VN Native Copy) |
|---|---|---|---|
| **1. Pedagogical Nudge Generator** (Lời nhắc sư phạm) | Học sinh vắng mặt $\ge 48$h hoặc đến chu kỳ Spaced Repetition | `{"user_age": 8, "last_topic": "Phân biệt Tr/Ch", "streak_lost": true}` | *"Chào bé! Chú Voi con thấy em vắng mặt 2 ngày rồi. Các chữ Tr và Ch đang chơi trốn tìm chờ em đến ghép lại đấy. Mình vào ôn tập 5 phút để lấy lại Chuỗi ngày học nhé!"* |
| **2. Diagnostic Pronunciation Feedback** (Phản hồi phát âm chẩn đoán) | Thuật toán GOP/ASR báo điểm xác suất thấp ở âm vị/thanh điệu cụ thể | `{"target": "suy nghĩ", "uttered": "suy nghí", "error": "ngã -> sắc", "confidence": 0.92}` | *"Em phát âm từ 'suy' rất hay! Tuy nhiên, ở chữ 'nghĩ', âm thanh của em bị vút lên hơi nhanh giống dấu sắc (nghí). Em thử làm lại, kéo dài giọng ở giữa một chút và hạ giọng xuống trước khi lên cao nhé: ngh-ĩ-ĩ."* |
| **3. IRT Adaptive Router** (Điều hướng nội dung thích ứng) | Học sinh trả lời đúng liên tiếp 3 câu hỏi đánh giá quá trình | `{"student_theta": 1.2, "item_b": 0.5, "consecutive_correct": 3}` | *"Em làm rất tuyệt! Chúng ta thử sức với một câu hỏi thử thách hơn nhé!"* (Kích hoạt ZPD, giảm giàn giáo hỗ trợ, duy trì trạng thái Flow). |
| **4. Parental Analytics Translation** (Diễn dịch báo cáo phụ huynh) | Cuối tuần hoặc khi học sinh đạt Mastery Learning ở một học phần | `{"parent": "Anh Hoàng", "student": "Bé Tuấn", "mastery": ["Câu đơn"], "struggling": ["Âm tr/ch"]}` | *"Kính gửi Quý phụ huynh, tuần này bé Tuấn đã xuất sắc nắm vững cấu trúc câu đơn tiếng Việt. Dù bé còn đôi chút nhầm lẫn giữa âm 'tr' và 'ch', hệ thống đã tự động điều chỉnh lộ trình để bé thực hành thêm vào tuần tới. Anh/Chị có thể giúp bé ôn tập bằng cách cùng đọc truyện tranh buổi tối nhé."* |
| **5. Overjustification Preventer** (Kiểm soát dư thừa động lực) | Học sinh cày bài tập quá dễ lặp đi lặp lại để farm điểm XP/huy hiệu | `{"task_difficulty": "very_low", "competence": "high", "repetition": 10}` | *"Em đã hoàn toàn tinh thông bài học này rồi! Phần thưởng lớn nhất đang chờ em ở Thử thách Vượt cấp phía trước. Hãy bấm vào đây để khám phá bài mới nhé!"* (Chuyển từ động lực ngoại tại sang nội tại). |

---

## 2. Khoa học Nhận thức & Sư phạm Ứng dụng

### 2.1. Tối ưu hóa Trí nhớ
- **Lặp lại ngắt quãng (Spaced Repetition):** Ứng dụng hệ thống Leitner giãn cách chu kỳ ôn tập (1 ngày $\rightarrow$ 3 ngày $\rightarrow$ 7 ngày $\rightarrow$ 14 ngày) để làm phẳng Đường cong quên lãng Ebbinghaus.
- **Thực hành gợi nhớ (Retrieval Practice):** Sử dụng các câu hỏi trắc nghiệm ngắn (low-stakes quiz) hoặc điền khuyết để kích hoạt cơ chế truy xuất chủ động từ bộ nhớ dài hạn.
- **Học xen kẽ (Interleaving):** Đan xen các chủ đề ngữ pháp, từ vựng và thanh điệu khác nhau trong cùng một bài luyện tập để rèn luyện phản xạ phân biệt.

### 2.2. Khung Hỗ trợ Sư phạm
- **Vùng phát triển gần (ZPD) & Scaffolding:** Không cung cấp đáp án ngay lập tức. Gợi ý theo 3 tầng mỏng dần:
  1. Tầng 1: Nhắc lại quy tắc ngữ pháp / phát âm chung.
  2. Tầng 2: Làm nổi bật từ khóa hoặc âm vị bị sai.
  3. Tầng 3: Giải thích chi tiết và hướng dẫn sửa.
- **Comprehensible Input ($i+1$):** Đảm bảo độ khó của bài học luôn nhỉnh hơn năng lực hiện tại một nấc để tạo đà tiến bộ mà không gây nản chí.
- **Formative vs Summative Assessment:** Đánh giá quá trình (Formative) diễn ra liên tục để định hướng việc học; Đánh giá tổng kết (Summative) dùng để xếp loại và cấp chứng chỉ.
- **Học tập thông hiểu (Mastery Learning):** Yêu cầu học sinh đạt chuẩn thông hiểu ($\ge 80\%$) trước khi mở khóa nội dung mới.

---

## 3. Đo lường, Đánh giá & Phản hồi Phát âm

### 3.1. Lý thuyết Ứng đáp Câu hỏi (IRT) & CAT
- Mô hình 3PL: Độ khó $b$, Độ phân biệt $a$, Đoán mò $c$.
- Computer Adaptive Testing (CAT) sử dụng chuẩn ngân hàng câu hỏi QTI 3.0 để điều chỉnh độ khó bài thi theo thời gian thực dựa trên năng lực ước tính $\theta$.

### 3.2. Chấm điểm Phát âm Tiếng Việt (GOP & ASR)
- Giọng trẻ em có tần số cơ bản (pitch) cao và dải cộng hưởng (formants) đặc thù $\rightarrow$ Cần tinh chỉnh trên mô hình tự giám sát (Wav2Vec2).
- Thuật toán Goodness of Pronunciation (GOP) tính toán xác suất hậu nghiệm trên từng âm vị và trạng thái thanh điệu ($f_0$).
- Sử dụng chỉ số **CER (Character Error Rate)** thay vì WER để phản ánh chính xác lỗi dấu thanh và âm tiết tiếng Việt.

### 3.3. Quy tắc Phản hồi Sandwich (Bắt buộc cho Phát âm)
Tuyệt đối không dùng phản hồi tiêu cực thô bạo (*"Sai rồi"*, *"Điểm của bạn là 40%"*). Áp dụng cấu trúc 3 lớp:
1. **Lớp 1 (Khen ngợi nỗ lực):** Nêu âm vị đã phát âm đúng.
2. **Lớp 2 (Chỉ dẫn sửa âm vị/thanh điệu):** Hướng dẫn khẩu hình/luồng hơi trực quan.
3. **Lớp 3 (Động viên Growth Mindset):** Khích lệ thử lại.

---

## 4. Thuyết Tự quyết (SDT) & Trải nghiệm Người dùng

- **3 Nhu cầu tâm lý SDT:**
  - *Quyền tự chủ (Autonomy):* Cho phép chọn lộ trình, linh vật hoặc chủ đề bài học.
  - *Năng lực (Competence):* Duy trì trạng thái dòng chảy (Flow State) qua bài tập vừa sức ($i+1$).
  - *Sự gắn kết (Relatedness):* Kết nối bạn học, chia sẻ thành tích văn minh.
- **Phòng ngừa Overjustification Effect:** Khi học sinh đã đạt mức thông hiểu (Mastery), hệ thống cần giới hạn điểm thưởng ngoại tại và khích lệ động lực nội tại khám phá thử thách mới.
- **Empty State (Giao diện rỗng):** Không bao giờ hiển thị cụm từ trơ trụi `"Trạng thái trống"` hoặc `"Không có dữ liệu"`. Luôn viết kèm lời khuyên hành động (Actionable Call-to-Action).

---

## 5. Chuẩn Kỹ thuật & Tương tác Hệ thống

| Chuẩn Kỹ thuật | Trạng thái | Mục đích & Vai trò |
|---|---|---|
| **LTI 1.3 & LTI Advantage** | **Cốt lõi (Adopt)** | Kết nối an toàn (OAuth 2.0 / JWT), đồng bộ sổ điểm LMS (AGS), lấy danh sách lớp (NRPS), nhúng bài học (Deep Linking). |
| **xAPI & cmi5** | **Cốt lõi (Adopt)** | Ghi nhận hành vi học tập dạng "Actor-Verb-Object" về LRS; cmi5 quản lý Đơn vị Giao việc (AU) an toàn thay thế SCORM. |
| **QTI 3.0** | **Cốt lõi (Adopt)** | Chuẩn ngân hàng câu hỏi trắc nghiệm hỗ trợ CAT và chuẩn trợ năng WCAG. |
| **LRMI / Schema.org** | **Cốt lõi (Adopt)** | Siêu dữ liệu tài nguyên học tập dạng JSON-LD hỗ trợ SEO và tìm kiếm bài giảng. |
| **SCORM / IEEE LOM** | **Loại bỏ (Deprecate)** | Lỗi thời, phụ thuộc iframe trình duyệt, không tối ưu cho di động và học offline. |

---

## 6. Pháp lý Bảo vệ Dữ liệu Trẻ em (Nghị định 13/2023/NĐ-CP)

- **Điều 20 Nghị định 13/2023/NĐ-CP:** Trẻ em từ đủ 7 tuổi trở lên bắt buộc phải có **Sự đồng ý kép (Double Consent)**:
  - Sự đồng ý từ chính trẻ em; VÀ
  - Sự đồng ý từ cha, mẹ hoặc người giám hộ hợp pháp (Verifiable Parental Consent).
- **Dữ liệu Sinh trắc học Giọng nói:** Tệp ghi âm tiếng nói trẻ em là dữ liệu nhạy cảm. Phải áp dụng chính sách **Tự động xóa (Data Retention)** ngay sau khi hoàn thành tính điểm GOP, không lưu trữ vĩnh viễn trừ phi có thỏa thuận đồng ý bổ sung từ phụ huynh.
