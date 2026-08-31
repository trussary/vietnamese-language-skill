<!-- vlc-disable: CAL001, DIA001 -->

# Glossary — school, academic, and EdTech terms

Two tables. The first is machine-readable: `validate_copy.py` parses it, so every row is a
lint rule and adding a row needs no code change. The second is guidance the linter cannot
enforce, because the correct term depends on context the linter cannot see.

An optional `Severity` column overrides the default. Use `error` for a calque no Vietnamese
teacher, registrar, or EdTech practitioner would ever write, `warn` for one that is merely unnatural
or that a native reader would notice but not consider broken.

## Calques that mark machine translation

<!-- machine-readable: glossary -->

| EN | ❌ Calque | ✅ Native usage | Severity |
|---|---|---|---|
| report card | `thẻ báo cáo` | `học bạ / sổ liên lạc` | error |
| homeroom teacher | `giáo viên phòng nhà` | `giáo viên chủ nhiệm` | error |
| parents (collective, formal) | `các bậc cha mẹ` | `quý phụ huynh` | warn |
| dear parents | `thân gửi các cha mẹ` | `kính gửi quý phụ huynh` | warn |
| plagiarism | `ăn cắp ý tưởng` | `đạo văn` | error |
| reissue a lost original diploma | `cấp lại bằng gốc` | `cấp bản sao từ sổ gốc` | error |
| reissue a lost original diploma (alt.) | `cấp lại bản chính` | `cấp bản sao từ sổ gốc` | error |
| academic credit | `tín dụng học tập` | `tín chỉ` | error |
| learning outcomes (syllabus) | `kết quả học tập mong muốn` | `chuẩn đầu ra` | warn |
| submit (an assignment) | `đệ trình bài tập` | `nộp bài` | error |
| submit (an assignment, alt.) | `trình nộp bài` | `nộp bài` | error |
| learning dashboard | `bảng táp-lô` | `bảng tổng quan / tổng quan` | error |
| track progress | `theo dấu sự tiến bộ` | `xem tiến độ học tập` | error |
| leaderboard | `bảng lãnh đạo` | `bảng xếp hạng` | error |
| leaderboard (alt.) | `bảng người dẫn đầu` | `bảng xếp hạng` | error |
| mastery learning | `học tập làm chủ` | `học tập thông hiểu / học tới mức tinh thông` | error |
| formative assessment | `đánh giá định hình` | `đánh giá quá trình` | error |
| formative assessment (alt.) | `đánh giá hình thành` | `đánh giá quá trình` | warn |
| summative assessment | `đánh giá tổng quát` | `đánh giá tổng kết` | error |
| summative assessment (alt.) | `đánh giá đúc kết` | `đánh giá tổng kết` | warn |
| gamification | `trò chơi hóa` | `game hóa / ứng dụng cơ chế game` | warn |
| learning streak | `vệt học tập` | `chuỗi học tập / chuỗi ngày học` | error |
| comprehensible input | `đầu vào có thể hiểu được` | `dữ liệu đầu vào vừa sức` | warn |
| scaffolding (pedagogy) | `giàn giáo học tập` | `hỗ trợ từng bước / hệ thống gợi ý` | warn |
| dropout rate | `tỷ lệ rớt ra ngoài` | `tỷ lệ bỏ học / tỷ lệ hao hụt` | error |
| adaptive testing | `thử nghiệm thích nghi` | `bài thi thích ứng / bài kiểm tra tùy biến` | error |

## Terms where context decides — do not blocklist

These are legitimate Vietnamese words with a genuine second meaning, so they are deliberately
**not** in the machine-readable table above; a blanket rule would fire on correct usage as
often as on the calque.

| EN | Wrong here | Right here | Why it is not a lint rule |
|---|---|---|---|
| syllabus / course outline | `giáo trình` (this is *textbook*, not *syllabus*) — write `đề cương môn học` / `đề cương chi tiết học phần` | — | `giáo trình` is correct whenever the writer actually means "textbook"; the linter cannot tell the two apart |
| university course registration | `đăng ký khóa học` reads as an EdTech phrase, not a registrar one — write `đăng ký học phần` | — | `khóa học` is the right word for an e-learning or short course; only university-registrar prose wants `học phần` |
| academic vs. financial credit | `tín dụng` in a higher-ed document | `tín chỉ` (academic) — but `tín dụng sinh viên` (student credit/loan) is a real, correct phrase | gated behind `--doctype higher-ed`/`transcript` instead of blocklisted — see `scripts/rules_education.py` (`EDU005`) |
| badges (gamification) | `huy hiệu` (when it reads as physical metal badges) | `danh hiệu` / `kỷ niệm chương` | `huy hiệu` is standard in general software badges; in academic milestones `danh hiệu` conveys earned achievement better |

## Specialized EdTech Lexicon (Groups A–F)

Bảng đối chiếu 60 thuật ngữ chuyên ngành chuẩn hóa phục vụ xây dựng và bản địa hóa sản phẩm EdTech:

### Nhóm A: Khoa học Nhận thức & Sư phạm Ứng dụng (Learning Science & Pedagogy)
| Thuật ngữ EN | Dịch / Giữ nguyên vi-VN | Định nghĩa cốt lõi |
|---|---|---|
| Spaced Repetition | Lặp lại ngắt quãng | Kỹ thuật ôn tập tăng dần khoảng cách thời gian để chống quên (Leitner). |
| Retrieval Practice | Thực hành gợi nhớ | Chủ động truy xuất kiến thức qua bài tập trắc nghiệm ngắn/flashcard. |
| Interleaving | Học xen kẽ | Trộn lẫn các dạng bài tập/chủ đề trong một buổi học để tăng phản xạ phân biệt. |
| Scaffolding | Hỗ trợ từng bước / Hệ thống gợi ý | Cung cấp giàn giáo gợi ý tạm thời giúp học sinh vượt qua thử thách khó. |
| Zone of Proximal Development (ZPD) | Vùng phát triển gần | Khoảng cách giữa năng lực tự làm và năng lực khi có người hướng dẫn. |
| Formative Assessment | Đánh giá quá trình | Đánh giá liên tục trong lúc học để phản hồi và điều chỉnh ngay lập tức. |
| Summative Assessment | Đánh giá tổng kết | Bài thi cuối kỳ/cuối học phần để cấp chứng chỉ hoặc chuẩn đầu ra. |
| Mastery Learning | Học tập thông hiểu / Tinh thông | Yêu cầu đạt chuẩn vững chắc trước khi mở khóa bài học tiếp theo. |
| Comprehensible Input | Dữ liệu đầu vào vừa sức | Lượng kiến thức tiếp nhận ở mức $i+1$ (nhỉnh hơn năng lực hiện tại một chút). |
| Cognitive Evaluation Theory | Thuyết đánh giá nhận thức | Lý thuyết giải thích tác động của phần thưởng ngoại tại lên động lực nội tại. |

### Nhóm B: Đo lường, Đánh giá & Xử lý Tiếng nói (Assessment, Analytics & Speech)
| Thuật ngữ EN | Dịch / Giữ nguyên vi-VN | Định nghĩa cốt lõi |
|---|---|---|
| Item Response Theory (IRT) | Lý thuyết ứng đáp câu hỏi | Mô hình toán học 3PL ($b$: độ khó, $a$: độ phân biệt, $c$: đoán mò). |
| Computer Adaptive Testing (CAT) | Kiểm tra thích ứng | Bài thi tự động điều chỉnh độ khó theo thời gian thực dựa trên năng lực học sinh. |
| Rubric | Khung chấm điểm (Rubric) | Bảng tiêu chí chi tiết mô tả mức độ đạt được cho bài tập tự luận/nói. |
| Learning Analytics | Phân tích dữ liệu học tập | Thu thập và phân tích dữ liệu hành vi học sinh trên Dashboard. |
| Goodness of Pronunciation (GOP) | Độ chính xác phát âm | Thuật toán đánh giá phát âm âm vị dựa trên log-likelihood từ mô hình âm học. |
| Posterior Probabilities | Xác suất hậu nghiệm | Xác suất âm vị được tính sau khi đã quan sát đặc trưng âm học. |
| Senones | Trạng thái Triphone (Senones) | Trạng thái HMM ràng buộc ngữ cảnh dùng để mô hình hóa âm học trong DNN. |
| Word Error Rate (WER) | Tỷ lệ lỗi từ | Chỉ số đo lỗi ASR trên cấp độ từ (chèn, xóa, thay thế). |
| Character Error Rate (CER) | Tỷ lệ lỗi ký tự | Thước đo ưu việt hơn cho tiếng Việt ở cấp độ ký tự và thanh điệu. |
| Phoneme-level feedback | Phản hồi cấp độ âm vị | Đánh giá chỉ ra chính xác sai sót ở từng nguyên âm, phụ âm hay dấu thanh. |

### Nhóm C: Trải nghiệm Người dùng, Động lực & Game hóa (UX & Motivation)
| Thuật ngữ EN | Dịch / Giữ nguyên vi-VN | Định nghĩa cốt lõi |
|---|---|---|
| Self-Determination Theory (SDT) | Thuyết tự quyết | Khung lý thuyết động lực tập trung vào Tự chủ, Năng lực và Gắn kết. |
| Overjustification Effect | Hiệu ứng dư thừa động lực | Hiện tượng suy giảm động lực nội tại khi nhận quá nhiều phần thưởng ngoại tại. |
| Gamification | Game hóa / Ứng dụng cơ chế game | Áp dụng cơ chế game (điểm, cấp độ, huy hiệu) vào học tập. |
| Habit Loop | Vòng lặp thói quen | Chu trình Gợi ý (Cue) $\rightarrow$ Hành động (Routine) $\rightarrow$ Phần thưởng (Reward). |
| Nudge | Cú hích | Thiết kế thông báo/giao diện dẫn dắt hành vi tích cực mà không ép buộc. |
| Onboarding | Hướng dẫn nhập môn | Luồng làm quen ban đầu giúp học sinh/phụ huynh hiểu cách sử dụng ứng dụng. |
| Empty State | Giao diện rỗng | Màn hình khi chưa có dữ liệu, luôn đi kèm Call to Action (CTA) hành động. |

### Nhóm D: Chuẩn Kỹ thuật & Tương tác Hệ thống (Technical Standards)
| Thuật ngữ EN | Dịch / Giữ nguyên vi-VN | Định nghĩa cốt lõi |
|---|---|---|
| Curriculum Mapping | Ánh xạ chương trình | Đối chiếu nội dung học với chuẩn quốc gia (GDPT 2018) hoặc CEFR. |
| Learning Path | Lộ trình học tập | Cấu trúc bài học được thiết kế tuần tự hoặc rẽ nhánh theo năng lực. |
| SCORM | SCORM (Chuẩn cũ) | Chuẩn đóng gói cũ, phụ thuộc iframe, không tối ưu cho di động/offline. |
| xAPI (Experience API) | xAPI | Chuẩn ghi nhận dữ liệu dạng "Actor - Verb - Object" gửi về LRS. |
| cmi5 | cmi5 | Hồ sơ xAPI chuẩn hóa khởi chạy, quản lý Đơn vị Giao việc (AU) an toàn. |
| Assignable Unit (AU) | Đơn vị Giao việc | Module nội dung học tập độc lập có thể khởi chạy và theo dõi trong cmi5. |
| Learning Record Store (LRS) | Kho bản ghi học tập | Cơ sở dữ liệu chuyên dụng lưu trữ các câu lệnh trải nghiệm xAPI. |
| LTI Advantage | LTI Advantage | Chuẩn kết nối công cụ học tập với LMS (Canvas, Moodle) qua LTI 1.3. |
| Names and Role Provisioning (NRPS) | Dịch vụ Tên và Vai trò | Tính năng LTI 1.3 lấy danh sách lớp học và quyền hạn an toàn. |
| Assignment and Grade Services (AGS) | Dịch vụ Điểm số và Bài tập | Tính năng LTI 1.3 đồng bộ điểm trực tiếp về sổ điểm của LMS. |
| Deep Linking | Liên kết sâu | Dịch vụ LTI 1.3 cho phép giáo viên chọn chính xác bài học nhúng vào khóa học. |
| QTI 3.0 | QTI 3.0 | Chuẩn định dạng ngân hàng câu hỏi, hỗ trợ thi thích ứng và trợ năng WCAG. |
| LRMI / Schema.org | Siêu dữ liệu Tài nguyên Học tập | Định dạng JSON-LD mô tả bài học phục vụ SEO và tìm kiếm bài giảng. |

### Nhóm E: Pháp lý & Bảo vệ Dữ liệu Trẻ em (Compliance & Privacy)
| Thuật ngữ EN | Dịch / Giữ nguyên vi-VN | Định nghĩa cốt lõi |
|---|---|---|
| PDPL (Decree 13) | Nghị định 13/2023/NĐ-CP | Quy định bảo vệ dữ liệu cá nhân tại Việt Nam. |
| PII (Personally Identifiable Info) | Dữ liệu định danh cá nhân | Thông tin định danh bao gồm cả dữ liệu sinh trắc học giọng nói. |
| Double Consent | Sự đồng ý kép | Bắt buộc có sự đồng ý của cả trẻ ($\ge 7$ tuổi) và cha mẹ/người giám hộ. |
| Verifiable Parental Consent (VPC) | Chấp thuận xác minh từ phụ huynh | Quy trình xác minh phụ huynh thực sự cấp phép (email xác thực, giao dịch nhỏ). |
| COPPA | Đạo luật COPPA (Hoa Kỳ) | Khung tham chiếu quốc tế bảo vệ quyền riêng tư của trẻ em dưới 13 tuổi. |
| GDPR-K | GDPR-K (Châu Âu) | Quy định bảo vệ dữ liệu trẻ em theo chuẩn Châu Âu (dưới 16 tuổi). |
| Data Retention | Lưu giữ dữ liệu | Quy định tự động xóa file ghi âm giọng nói trẻ em sau khi xử lý GOP. |

### Nhóm F: Hạ tầng Công nghệ Tiếng nói & AI (Speech & AI Infrastructure)
| Thuật ngữ EN | Dịch / Giữ nguyên vi-VN | Định nghĩa cốt lõi |
|---|---|---|
| Automatic Speech Recognition (ASR) | Nhận dạng giọng nói tự động | Công nghệ chuyển đổi âm thanh giọng nói thành văn bản. |
| Text to Speech (TTS) | Tổng hợp giọng nói | Chuyển văn bản thành giọng đọc nhân tạo chuẩn phát âm. |
| Self-supervised learning | Học tự giám sát | Huấn luyện mô hình (Wav2Vec2) trên dữ liệu không gán nhãn cho giọng trẻ em. |
| Pitch / Formants | Tần số cơ bản / Dải cộng hưởng | Đặc trưng âm học đặc thù của giọng trẻ em (Pitch cao, Formants dịch chuyển). |
| Retrieval-Augmented Generation (RAG) | Sinh văn bản tăng cường truy xuất | AI tạo sinh kết hợp tìm kiếm quy chế điểm/tài liệu chuẩn xác. |
| Prompt Chaining | Chuỗi câu lệnh liên hoàn | Chuỗi prompt phân tầng giúp gia sư AI phản hồi sư phạm từng bước. |
