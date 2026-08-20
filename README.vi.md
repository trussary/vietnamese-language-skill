# vietnamese-language-skill

*[English](README.md)*

Agent Skills giúp Claude viết tiếng Việt đúng chuẩn mà một người làm nghề tại Việt Nam sẽ thực
sự dùng được.

Tiếng Việt là ngôn ngữ ít dữ liệu huấn luyện đối với LLM. Nếu không có hướng dẫn, kết quả sẽ là
thứ tiếng Việt nghe trôi chảy nhưng thực chất là dịch máy: trật tự câu tiếng Anh lồng trong từ
tiếng Việt, sai đại từ xưng hô so với đối tượng đọc, CTA dịch sát nghĩa, các từ ngữ quảng cáo
so sánh nhất **vi phạm pháp luật Việt Nam**, và tiền tệ trình bày theo kiểu Mỹ.

Cột bên trái không phải ví dụ bịa ra cho có — đó là những gì bạn nhận được nếu không dùng
skill này. Dưới đây là một ví dụ cho mỗi skill:

`vietnamese-landing-copy`

```diff
- Học thêm về dự án của chúng tôi
+ Tìm hiểu thêm về dự án

- Chúng tôi cung cấp những căn hộ tốt nhất số 1 thị trường
+ Không gian sống đẳng cấp giữa lòng thành phố

- Giá: 2,500,000,000 VND
+ Giá chỉ từ 2,5 tỷ đồng
```

`vietnamese-tech-writing`

```diff
- cam kết các thay đổi
+ commit các thay đổi

- triển khai đến sản xuất
+ deploy lên production

- Bạn sẽ thử lại request khi gặp lỗi.
+ Hệ thống sẽ tự động retry request khi gặp lỗi.
```

`vietnamese-business-comms`

```diff
- Cà phê số 1 Việt Nam
+ Cà phê được hơn 10.000 khách hàng lựa chọn mỗi ngày

- Học thêm
+ Xem ngay

- Đơn hàng đã xác nhận. Ưu đãi giảm 50% hôm nay, đặt ngay!
+ Đơn hàng của Quý khách đã được xác nhận. Dự kiến giao trước 20/08.
```

`vietnamese-finance-copy`

```diff
- Cam kết lợi nhuận 12%/năm cho nhà đầu tư
+ Lợi nhuận kỳ vọng 12%/năm. Đầu tư có rủi ro; kết quả trong quá khứ không đảm bảo kết quả trong tương lai.

- Trả góp lãi suất 0% cho mọi đơn hàng
+ Trả góp lãi suất 0% — phí chuyển đổi 3%/khoản. Tổng chi phí phải trả: 10.300.000 ₫.

- Bảng cân đối kế toán tại ngày 31/12/2026
+ Báo cáo tình hình tài chính tại ngày 31/12/2026
```

## Repo này có gì

| Skill | Chức năng |
|---|---|
| [`vietnamese-landing-copy`](skills/vietnamese-landing-copy/) | Nội dung landing page — văn phong cho bất động sản, SaaS và thương mại điện tử. Có glossary thuật ngữ, CTA theo đúng quy ước, nhãn section, phần pháp lý cho form thu lead. |
| [`vietnamese-tech-writing`](skills/vietnamese-tech-writing/) | Tài liệu kỹ thuật và sản phẩm — commit, PR, RFC, postmortem, runbook, README, API docs, UI microcopy, file i18n, PRD, release notes, khảo sát. Có quy tắc code-switching và các rủi ro i18n riêng của tiếng Việt (vi-VN). |
| [`vietnamese-business-comms`](skills/vietnamese-business-comms/) | Marketing và sales — email campaign, Zalo ZNS/ZBS, quảng cáo, tin đăng marketplace, thông cáo báo chí, cold outreach, báo giá, nhắc nợ, lời chúc Tết. Có quy tắc xưng hô B2B và luật quảng cáo. |
| [`vietnamese-finance-copy`](skills/vietnamese-finance-copy/) | Tài chính — lĩnh vực chịu quản lý chặt: hóa đơn điện tử, báo cáo tài chính, bản tin nhà đầu tư, nội dung fintech và bảo hiểm, thông báo tín dụng. Có thuật ngữ theo Thông tư 99/2025 và giới hạn khi quảng cáo tài chính. |

Các skill dùng chung một validator engine và bốn tài liệu tham chiếu (register matrix, dấu
thanh và Unicode, định dạng theo locale, tuân thủ pháp luật), nằm trong [`shared/`](shared/) và
được copy vào từng skill qua một bước build — nhờ vậy mỗi thư mục skill vẫn cài đặt độc lập được.

## Cài đặt

### `npx skills` (dùng cho mọi agent)

CLI [`skills`](https://www.npmjs.com/package/skills) cài vào Claude Code, Cursor và các agent
khác chỉ bằng một lệnh — không cần hệ thống plugin:

```bash
npx skills add trussary/vietnamese-language-skill
```

Các flag hữu ích:

```bash
npx skills add trussary/vietnamese-language-skill --list       # xem trước repo có gì
npx skills add trussary/vietnamese-language-skill -g           # cài global, không theo từng project
npx skills add trussary/vietnamese-language-skill -a '*' --all # cài cho mọi agent, không hỏi lại
```

Sau đó dùng `npx skills list` để kiểm tra, `npx skills update` để cập nhật bản mới, và
`npx skills remove vietnamese-landing-copy` để gỡ cài đặt.

Muốn dùng thử một skill trong một session mà không cần cài gì:

```bash
npx skills use trussary/vietnamese-language-skill@vietnamese-landing-copy
npx skills use trussary/vietnamese-language-skill@vietnamese-tech-writing
npx skills use trussary/vietnamese-language-skill@vietnamese-business-comms
npx skills use trussary/vietnamese-language-skill@vietnamese-finance-copy
```

### Plugin cho Claude Code

```bash
/plugin marketplace add trussary/vietnamese-language-skill
```

Sau đó cài plugin `vietnamese-language-skill` từ marketplace. Mỗi skill sẽ có tiền tố tên
plugin đứng trước — `vietnamese-language-skill:vietnamese-landing-copy`, và tương tự cho các
skill còn lại.

### Thư mục skill thuần

Copy các skill bạn cần vào thư mục skills cá nhân hoặc của project. Mỗi thư mục là độc lập —
không cần copy thêm gì kèm theo:

```bash
cp -r skills/vietnamese-landing-copy ~/.claude/skills/
cp -r skills/vietnamese-tech-writing ~/.claude/skills/
```

Nếu muốn giới hạn trong một project, dùng `.claude/skills/` ngay trong repo đó thay vì thư mục
cá nhân.

### Claude.ai / Claude Cowork

Nén một thư mục skill và upload trong phần cài đặt skill:

```bash
cd skills && zip -r vietnamese-landing-copy.zip vietnamese-landing-copy
```

## Cách dùng

Sau khi cài đặt, các skill tự kích hoạt khi cần. Bạn chỉ cần yêu cầu viết nội dung tiếng Việt
như bình thường, các từ khóa sẽ tự điều hướng đến đúng skill:

> Viết landing page cho dự án căn hộ cao cấp tại Quận 7

> Our Vietnamese README reads like Google Translate — should we translate "deploy"?

> Viết email chào hàng gửi khách doanh nghiệp, kèm báo giá có VAT

> Can we advertise a guaranteed 12% annual return in Vietnam?

Linter của từng skill cũng chạy độc lập được, không cần Claude:

```bash
python skills/vietnamese-landing-copy/scripts/validate_copy.py copy.md --register re
python skills/vietnamese-tech-writing/scripts/validate_copy.py CHANGELOG.md --doctype commit
python skills/vietnamese-business-comms/scripts/validate_copy.py email.md --doctype cold-outreach
python skills/vietnamese-finance-copy/scripts/validate_copy.py bctc.md --doctype statement
```

```text
copy.md:3:1: error CAL001  calque "Học thêm"
      → use "Tìm hiểu thêm / Xem thêm" (glossary.md)
copy.md:7:12: warn  LAW001  regulated superlative "số 1"
      → needs a licensed market survey or award certificate; annotate with
        <!-- proof: ... --> or rewrite as a countable fact
copy.md:11:8: error NUM001  comma-grouped number "2,500,000"
      → write "2.500.000"
```

Yêu cầu Python 3.9+, chỉ dùng standard library. Không cần bước cài đặt riêng.

## Linter kiểm tra những gì

| Rule | Bắt lỗi gì |
|---|---|
| `NFC001` | Unicode dạng decomposed làm vỡ hiển thị web-font |
| `CAL001` | Calque tiếng Anh, dựa theo blocklist trong glossary |
| `LAW001` | Từ so sánh nhất bị quản lý (Luật Quảng cáo Điều 8 khoản 11) — chỉ cảnh báo, không bao giờ chặn |
| `DIA001` | Tiếng Việt viết không dấu |
| `TONE001` | Trộn lẫn hai kiểu đánh dấu thanh trong cùng một tài liệu |
| `NUM001`–`NUM004` | Dấu phẩy ngăn cách hàng nghìn, số không nhóm chữ số, dấu chấm thập phân, `m2` viết bằng ASCII |
| `DATE001` | Định dạng `MM/dd/yyyy` trong khi tiếng Việt dùng `dd/MM/yyyy` |
| `PHONE001` | Còn giữ số 0 đầu khi đã có `+84` |
| `ICU001` | Bất kỳ nhánh số nhiều ICU nào khác `other` — tiếng Việt chỉ có `other` |
| `PRO001`/`PRO002` | Trộn lẫn register, hoặc dùng đại từ không đúng với register đã khai báo |

Mỗi skill còn bổ sung thêm rule riêng. Chạy `--list-rules` với validator của một skill để xem
đầy đủ các rule skill đó có thể phát hiện:

| Skill | Rule bổ sung |
|---|---|
| `vietnamese-tech-writing` | `ENG001` commit subject, branch hoặc identifier không phải ASCII · `ENG003` xưng hô trực tiếp trong RFC hoặc postmortem · `ENG007` bước runbook viết theo kiểu hedging · `PROD002` thang khảo sát đồng ý/không đồng ý · `PROD003` metadata app-store vượt giới hạn nền tảng · `PROD004` nội dung xin consent mà không nêu mục đích |
| `vietnamese-business-comms` | `ZNS001` nội dung marketing trong template Zalo transactional · `ZNS002` template dài quá 400 ký tự · `MKT001` tiêu đề marketplace viết hoa toàn bộ hoặc chèn emoji · `MKT002` giảm giá vượt trần 50% · `SALES001` xưng hô suồng sã trong giao tiếp B2B · `SALES003` outreach không có lời chào · `SALES004` báo giá thiếu VAT hoặc thời hạn hiệu lực · `SPAM001` tin nhắn hàng loạt không có tùy chọn từ chối nhận |
| `vietnamese-finance-copy` | `FIN001` ngôn từ cam kết lợi nhuận <!-- vlc-disable-line CAL001 --> · `FIN002` lãi suất khuyến mãi không công bố tổng chi phí · `FIN005` bảng trong báo cáo tài chính thiếu `Đơn vị tính` · `FIN006` số âm viết bằng dấu trừ · `FIN007` hóa đơn thiếu `MST` hoặc `thuế GTGT` |

**Các rule chỉ hợp lý với một loại tài liệu cụ thể được gate bằng `--doctype` và sẽ im lặng nếu
không có flag này.** Giới hạn 400 ký tự đúng cho một template Zalo nhưng vô nghĩa với một design
doc. Ngoại lệ duy nhất là `FIN001`: ngôn từ cam kết lợi nhuận bị cấm ở bất kỳ đâu xuất hiện, nên rule này không bao giờ bị gate. <!-- vlc-disable-line LAW001, CAL001 -->

Tắt một rule khi nó thực sự sai trong ngữ cảnh cụ thể:

```markdown
<!-- vlc-disable: TONE001 -->            áp dụng cho toàn file
Text here <!-- vlc-disable-line NUM001 -->
Thương hiệu số 1 <!-- proof: Khảo sát Nielsen VN 2026 -->
Giảm đến 90% <!-- khuyen-mai-tap-trung: QĐ 123/SCT ngày 01/06/2026 -->
```

Directive hoạt động trong HTML, `//`, `/* */`, `#`, và giá trị string trong JSON. Annotation
`proof` và `khuyen-mai-tap-trung` chỉ ghi nhận rằng giấy tờ đã tồn tại — chúng không tạo ra
giấy tờ đó, và người review vẫn cần kiểm tra thực tế.

## Ghi chú thiết kế

Năm quyết định nên biết trước khi đóng góp:

1. **Dữ liệu rule nằm trong Markdown, không nằm trong Python.** `validate_copy.py` parse các
   bảng trong `references/glossary.md`, `references/banned-phrases.md` và
   `references/register-matrix.md` khi chạy. Thêm một lint rule, hay thêm cả một register mới,
   chỉ là thêm một dòng bảng — không cần sửa code, không cần sửa test. Rule nào thực sự cần
   logic thì đặt trong `scripts/rules_*.py` riêng của skill, engine sẽ tự import.
2. **Từ so sánh nhất chỉ cảnh báo, không bao giờ chặn.** Luật không cấm `số 1`; luật cấm `số 1`
   *khi không có chứng cứ*. Một linter chặn cứng cả một tuyên bố đã có chứng cứ hợp lệ sẽ bị tắt
   hoàn toàn, và điều đó không giúp được ai. `FIN001` cảnh báo vì lý do khác: quy định cấm cam
   kết lợi nhuận được ghép từ ba văn bản pháp luật khác nhau chứ không nằm gọn trong một văn
   bản, nên một cảnh báo đưa vấn đề đến luật sư mới là cách xử lý trung thực.
3. **Kiểu đánh dấu thanh không phải câu hỏi đúng/sai.** `hòa` (kiểu cũ) và `hoà` (kiểu mới) đều
   đúng. Các skill mặc định dùng kiểu mới và chỉ báo lỗi khi *trộn lẫn* hai kiểu trong cùng tài
   liệu.
4. **Gate theo doctype là thứ giữ cho linter luôn hữu dụng.** Một rule áp cho cả tài liệu không
   liên quan sẽ khiến cả công cụ bị tắt, nên các rule mang tính cấu trúc chỉ bật lên khi người
   gọi khai báo rõ tài liệu là loại gì.
5. **File dùng chung được generate ra, không symlink.** `npx skills use`, upload zip trên
   Claude.ai, và `cp -r` thuần đều chỉ cài đúng một thư mục, nên mỗi skill cần giữ bản copy thật
   của các tài liệu tham chiếu và engine dùng chung. `tools/sync_shared.py` ghi các bản copy đó,
   và CI sẽ fail nếu một bản copy bị lệch — sửa ở `shared/`, không sửa trực tiếp bản copy.

## Đóng góp

Đóng góp giá trị nhất ở đây là **về ngôn ngữ, không phải về code**: một dòng glossary, một cặp
ví dụ sai→đúng, một register profile cho một lĩnh vực repo chưa có. Xem
[CONTRIBUTING.md](CONTRIBUTING.md).

Mọi thay đổi trong glossary hoặc kho ví dụ đều cần một người bản ngữ tiếng Việt duyệt.

```bash
python -m pytest tests/ -q                # 500+ assertion, chủ yếu từ các eval corpus
python tools/build_examples.py            # tạo lại examples.md từ evals/<skill>/pairs.jsonl
python tools/sync_shared.py               # copy shared/ vào từng skill
```

Skill tài chính có tiêu chuẩn cao hơn: thuật ngữ báo cáo tài chính cần kế toán viên duyệt, và
bất kỳ nội dung nào mời chào đầu tư, mô tả bảo hiểm, hoặc trình bày lãi suất tín dụng đều cần
luật sư duyệt.

## Bối cảnh

[`research/research.md`](research/research.md) là tài liệu lý giải thiết kế ban đầu: các lỗi
đã ghi nhận, các quy ước bản ngữ dùng để sửa lỗi đó, các trích dẫn pháp lý, và spec Agent Skill
mà repo này được xây dựng theo.

[`research/exnpansion-research.md`](research/exnpansion-research.md) là phần nghiên cứu đứng
sau ba skill mới hơn — danh mục thể loại văn bản, chênh lệch register, bảng ngôn từ bị quản lý,
và danh sách rõ ràng những gì chưa xác minh được.
[`research/expansion-plan.md`](research/expansion-plan.md) mô tả cách nghiên cứu đó được chuyển
thành cấu trúc hiện tại, kể cả lý do vì sao thứ tự build bị đảo ngược.

## Giấy phép

MIT — xem [LICENSE](LICENSE). Các trích dẫn pháp lý chỉ mang tính tham khảo khi viết nội dung,
không phải tư vấn pháp lý.
