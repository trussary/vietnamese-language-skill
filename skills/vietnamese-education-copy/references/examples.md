<!-- vlc-disable: all -->
<!-- GENERATED FILE — do not edit by hand.
     Source: evals/vietnamese-education-copy/pairs.jsonl. Regenerate with: python tools/build_examples.py -->

# Examples — bad to good

The highest-value file in this skill. Each pair names the failure mode it fixes; the
diagnosis generalizes further than the string does. Read this before writing anything
long in Vietnamese.

Every ❌ string here is a deliberate defect, so this file is exempt from its own linter.

**28 pairs.** Contributions welcome — see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

## K-12 school communications

### The student got an overall Excellent grade this semester.

❌ **Học sinh đạt loại Giỏi trong học kỳ này.**

✅ **Học sinh đạt mức Tốt trong học kỳ này.**

Uses the overall classification 'Giỏi', abolished by Thông tư 22/2021/TT-BGDĐT for THCS/THPT students; the current scale is Tốt/Khá/Đạt/Chưa đạt.

<sub>id: `edu-k12-001` · caught by: `EDU001`</sub>

### She is an Advanced student in her class.

❌ **Em là học sinh tiên tiến của lớp.**

✅ **Em đạt danh hiệu học sinh khá của lớp.**

'Học sinh tiên tiến' no longer exists as an overall title under Thông tư 22/2021/TT-BGDĐT.

<sub>id: `edu-k12-002` · caught by: `EDU001`</sub>

### You need to finish your homework before class tomorrow.

❌ **Bạn cần hoàn thành bài tập trước giờ học ngày mai.**

✅ **Em cần hoàn thành bài tập trước giờ học ngày mai.**

A teacher addressing a student as 'bạn' strips the hierarchical respect the relationship requires; secondary students are addressed as 'em'.

<sub>id: `edu-k12-003` · caught by: `EDU002`</sub>

### He needs to improve in Vietnamese language.

❌ **Con cần cải thiện ở môn Tiếng Việt.**

✅ **Con cần cố gắng hơn ở môn Tiếng Việt.**

'Cần cải thiện' is the calque for 'needs improvement'; Thông tư 27/2020/TT-BGDĐT mandates 'cần cố gắng' for primary routine assessment.

<sub>id: `edu-k12-004` · caught by: `EDU003`</sub>

### Dear Parents, please remember to sign the school notebook.

❌ **Thân gửi các cha mẹ, xin nhớ ký vào sổ liên lạc.**

✅ **Kính gửi Quý phụ huynh, xin vui lòng ký xác nhận vào sổ liên lạc.**

'Thân gửi các cha mẹ' is a literal, distant-sounding translation; Vietnamese school-to-home communication opens with 'Kính gửi Quý phụ huynh'.

<sub>id: `edu-k12-005` · caught by: `CAL001`</sub>

### Please keep this report card for your records.

❌ **Xin lưu giữ thẻ báo cáo này.**

✅ **Xin lưu giữ học bạ này.**

'Thẻ báo cáo' is not a Vietnamese school artifact; the correct term is 'học bạ' (or 'sổ liên lạc' for the home-communication book).

<sub>id: `edu-k12-006` · caught by: `CAL001`</sub>

### The homeroom teacher will contact you soon.

❌ **Giáo viên phòng nhà sẽ liên hệ sớm.**

✅ **Giáo viên chủ nhiệm sẽ liên hệ sớm.**

'Giáo viên phòng nhà' is a literal calque of 'homeroom teacher'; the standard term is 'giáo viên chủ nhiệm' (GVCN).

<sub>id: `edu-k12-007` · caught by: `CAL001`</sub>

### Parents must consent before the app shares a child's grade data.

❌ **Ứng dụng sẽ chia sẻ dữ liệu điểm số của con.**

✅ **Quý phụ huynh vui lòng xác nhận đồng ý để ứng dụng chia sẻ dữ liệu điểm số của con nhằm mục đích theo dõi học tập.**

A K-12 portal sharing a specific child's grades is processing a minor's data and needs the parent's informed consent naming a purpose (Nghị định 13/2023/NĐ-CP); whether consent language is present is a human review item, not machine-detectable.

<sub>id: `edu-k12-008` · caught by: _not machine-detectable_</sub>

### Tuition this month is 2,500,000 VND.

❌ **Học phí tháng này là 2,500,000 VND.**

✅ **Học phí tháng này là 2.500.000 đ.**

Comma-grouped, English-style currency formatting; Vietnamese groups with periods.

<sub>id: `edu-k12-009` · caught by: `NUM001`</sub>

### Dear customer, please check your child's report.

❌ **Kính gửi quý khách, mời quý khách xem báo cáo học tập của con.**

✅ **Kính gửi Quý phụ huynh, mời quý phụ huynh xem báo cáo học tập của con.**

'Quý khách' is a commercial, e-commerce register; a school addressing a parent is not addressing a customer.

<sub>id: `edu-k12-010` · caught by: `PRO002`</sub>

## Higher education and academic writing

### The student completed 120 credits.

❌ **Sinh viên đã hoàn thành 120 tín dụng.**

✅ **Sinh viên đã tích lũy đủ 120 tín chỉ.**

'Tín dụng' is financial credit; Vietnamese academic credit under Thông tư 08/2021/TT-BGDĐT is 'tín chỉ'.

<sub>id: `edu-hed-001` · caught by: `EDU005`</sub>

### His GPA is 3.6 out of 4.0.

❌ **GPA của sinh viên là 3.6/4.0.**

✅ **Điểm trung bình tích lũy của sinh viên là 3,6/4,0.**

GPA written with a dot decimal is a locale bug; Vietnamese transcripts use a decimal comma.

<sub>id: `edu-hed-002` · caught by: `EDU006`</sub>

### If the diploma is lost, a replacement original can be issued.

❌ **Nếu mất bằng, sinh viên có thể được cấp lại bằng gốc.**

✅ **Nếu mất văn bằng, sinh viên có thể được cấp bản sao từ sổ gốc.**

Vietnamese law has no mechanism to reissue a second original diploma (Thông tư 21/2019/TT-BGDĐT); a lost diploma is replaced with a copy from the master register.

<sub>id: `edu-hed-003` · caught by: `CAL001`</sub>

### Plagiarism will result in disciplinary action.

❌ **Ăn cắp ý tưởng sẽ bị xử lý kỷ luật.**

✅ **Đạo văn sẽ bị xử lý kỷ luật.**

'Ăn cắp ý tưởng' is a colloquial calque; formal academic-integrity writing uses 'đạo văn'.

<sub>id: `edu-hed-004` · caught by: `CAL001`</sub>

### You must complete course registration by the 15th.

❌ **Bạn phải hoàn tất đăng ký học phần trước ngày 15.**

✅ **Sinh viên cần hoàn tất đăng ký học phần trước ngày 15.**

University administrative prose addresses no one directly; the student is third-person 'sinh viên', not 'bạn'.

<sub>id: `edu-hed-005` · caught by: `PRO002`</sub>

### The syllabus outlines the learning outcomes.

❌ **Giáo trình phác thảo các kết quả học tập mong muốn.**

✅ **Đề cương chi tiết học phần nêu rõ các chuẩn đầu ra.**

Calques both 'syllabus' (giáo trình is textbook, not syllabus) and 'learning outcomes' (the settled term is chuẩn đầu ra); only the second is machine-checkable, since giáo trình is also correct when the writer means textbook.

<sub>id: `edu-hed-006` · caught by: `CAL001`</sub>

### Undergraduate students must pay tuition by the 15th.

❌ **Học sinh đại học phải nộp học phí trước ngày 15.**

✅ **Sinh viên phải hoàn thành nghĩa vụ học phí trước ngày 15.**

'Học sinh' is a K-12 student; a university student is 'sinh viên'. Not machine-checkable, since 'học sinh' is correct throughout this skill's own K-12 content.

<sub>id: `edu-hed-007` · caught by: _not machine-detectable_</sub>

### The registration deadline is 12/25/2026.

❌ **Hạn đăng ký học phần là 12/25/2026.**

✅ **Hạn đăng ký học phần là 25/12/2026.**

MM/dd/yyyy date format; Vietnamese uses dd/MM/yyyy.

<sub>id: `edu-hed-008` · caught by: `DATE001`</sub>

## EdTech product and pedagogical intelligence

### Please submit your assignment before 10 PM.

❌ **Học sinh vui lòng đệ trình bài tập trước 22:00.**

✅ **Học sinh vui lòng nộp bài trước 22:00.**

'Đệ trình bài tập' is a bureaucratic calque for 'submit an assignment'; native Vietnamese education uses 'nộp bài'.

<sub>id: `edu-edt-001` · caught by: `CAL001`</sub>

### Visit your learning dashboard to view your progress.

❌ **Mời bạn truy cập bảng táp-lô để xem tiến độ.**

✅ **Mời bạn truy cập bảng tổng quan để xem tiến độ.**

'Bảng táp-lô' is a literal automotive calque for 'dashboard'; in EdTech, learning analytics screens are 'bảng tổng quan' or 'tổng quan'.

<sub>id: `edu-edt-002` · caught by: `CAL001`</sub>

### The app helps you track your progress every day.

❌ **Hệ thống giúp bạn theo dấu sự tiến bộ mỗi ngày.**

✅ **Hệ thống giúp bạn xem tiến độ học tập mỗi ngày.**

'Theo dấu sự tiến bộ' is an unnatural literal calque of 'track your progress'; educational Vietnamese uses 'tiến độ học tập'.

<sub>id: `edu-edt-003` · caught by: `CAL001`</sub>

### She reached the top spot on the leaderboard.

❌ **Bé đã vươn lên vị trí dẫn đầu trên bảng lãnh đạo.**

✅ **Bé đã vươn lên vị trí dẫn đầu trên bảng xếp hạng.**

'Bảng lãnh đạo' is a machine-translation calque for 'leaderboard'; standard gamification uses 'bảng xếp hạng'.

<sub>id: `edu-edt-004` · caught by: `CAL001`</sub>

### Teachers perform formative assessment after each lecture.

❌ **Giáo viên tiến hành đánh giá định hình sau mỗi bài giảng.**

✅ **Giáo viên tiến hành đánh giá quá trình sau mỗi bài giảng.**

'Đánh giá định hình' is a calque; the statutory term codified by Bộ GD&ĐT is 'đánh giá quá trình' (Formative Assessment).

<sub>id: `edu-edt-005` · caught by: `CAL001`</sub>

### The curriculum is designed around mastery learning.

❌ **Khóa học áp dụng phương pháp học tập làm chủ.**

✅ **Khóa học áp dụng phương pháp học tập thông hiểu.**

'Học tập làm chủ' is a literal translation error for 'Mastery Learning'; pedagogical terminology uses 'học tập thông hiểu' or 'học tới mức tinh thông'.

<sub>id: `edu-edt-006` · caught by: `CAL001`</sub>

### You have maintained a 7-day learning streak.

❌ **Bạn đã duy trì vệt học tập 7 ngày liên tiếp.**

✅ **Bạn đã duy trì chuỗi học tập 7 ngày liên tiếp.**

'Vệt học tập' is a dictionary calque for 'streak'; Vietnamese learning apps use 'chuỗi học tập' or 'chuỗi ngày học'.

<sub>id: `edu-edt-007` · caught by: `CAL001`</sub>

### Empty state screen on student assignments tab.

❌ **Trạng thái trống**

✅ **Bạn chưa có bài tập nào hôm nay. Hãy bắt đầu với bài Ôn tập Thanh điệu nhé!**

Displaying raw 'Trạng thái trống' or 'Không có dữ liệu' without an actionable Call to Action leaves learners stranded.

<sub>id: `edu-edt-008` · caught by: `EDU007`</sub>

### Pronunciation feedback for incorrect tone.

❌ **Sai rồi! Bạn đã phát âm sai chữ này.**

✅ **Em phát âm âm đầu rất tốt! Ở chữ 'nghĩ', em thử kéo dài giọng ở giữa một chút và hạ giọng trước khi lên cao nhé.**

Blunt negative feedback ('Sai rồi') harms learner confidence; pedagogical systems apply the Sandwich Feedback model (praise effort, provide phoneme/tone guidance, encourage growth mindset).

<sub>id: `edu-edt-009` · caught by: `EDU009`</sub>

### Adaptive testing and scaffolding in learning analytics.

❌ **Ứng dụng giúp giảm tỷ lệ rớt ra ngoài của học viên.**

✅ **Ứng dụng giúp giảm tỷ lệ bỏ học của học viên.**

'Tỷ lệ rớt ra ngoài' is a literal calque for 'dropout rate'; Learning Analytics uses 'tỷ lệ bỏ học' or 'tỷ lệ hao hụt'.

<sub>id: `edu-edt-010` · caught by: `CAL001`</sub>
