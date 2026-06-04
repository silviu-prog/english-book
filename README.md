# Yeshua: Jesus Without Christianity — English Edition

English translation of *Yeshua: Iisus fără creștinism* by **Silviu Rotariu**,
prepared for publication on Amazon Kindle (KDP).

- **Length:** ~133,700 words · 14 chapters + front matter · 232 sections
- **Validation:** EPUB passes EPUBCheck (EPUB 3.2) with **0 errors / 0 warnings**

## Ready-to-publish files (`manuscript/`)

| File | Use |
|------|-----|
| `Yeshua-Jesus-Without-Christianity.epub` | **Primary** upload to KDP (reflowable eBook) |
| `Yeshua-Jesus-Without-Christianity.pdf` | Print-ready interior (6 × 9″, 399 pp.) for a KDP paperback |
| `Yeshua-Jesus-Without-Christianity.docx` | Alternative manuscript format KDP also accepts |
| `cover.jpg` | eBook cover (1600 × 2560 px, KDP-compliant) |

## Repository layout

- `book/` — the English manuscript, one Markdown file per chapter (the editable source)
- `src_ro/` — the Romanian source text extracted per chapter (provenance)
- `manuscript/` — build outputs, cover, metadata, stylesheet
- `TRANSLATION_BRIEF.md` — translation rules / glossary used for consistency
- `build_epub.sh` — rebuilds the EPUB from `book/*.md`
- `make_cover.py` — regenerates the cover

## Rebuilding

```bash
python3 make_cover.py      # regenerate cover
./build_epub.sh            # rebuild the EPUB
```

## Publishing on Kindle (KDP) — step by step

1. Go to **https://kdp.amazon.com** and sign in (create a free account if needed).
2. Complete your **Account info** (tax + bank details) under the account menu —
   required before a book can go live.
3. On the Bookshelf, click **Create** → **Kindle eBook**.
4. **Language:** English. **Title:** `Yeshua` · **Subtitle:** `Jesus Without Christianity`.
5. **Author:** Silviu Rotariu.
6. **Description:** paste the back-cover text below.
7. **Keywords & categories:** suggestions below.
8. **Manuscript:** upload `Yeshua-Jesus-Without-Christianity.epub`.
9. **Cover:** upload `cover.jpg` (or use the Cover Creator).
10. Use **Kindle Previewer** (the online preview) to check the look, then **Publish**.

### Suggested book description (back-cover copy)

> What if we could meet Yeshua — the man from Galilee — before his message
> became a system, a doctrine, and an institution?
>
> This book is not written against Christianity, nor to replace it. It is a
> patient, honest attempt to listen to Yeshua's living voice beneath the
> centuries of interpretation, fear, and control that settled over it. Drawing
> on a lifetime of biblical study and a background in psychology, Silviu Rotariu
> reads the Gospels existentially rather than dogmatically — asking not *what
> must we believe about Yeshua?* but *how did he live, how did he see, and how
> did he relate to people, to truth, to failure, and to God?*
>
> A bold, compassionate, and deeply human reading for believers, doubters, and
> seekers alike.

### Suggested categories
- Religion & Spirituality → Christianity → Christian Living
- Religion & Spirituality → Religious Studies

### Suggested keywords
`historical Jesus`, `Yeshua`, `Christianity without religion`, `Gospels`,
`spiritual but not religious`, `deconstruction faith`, `Jesus teachings`

> Note: ISBN 978-973-0-44188-8 is the Romanian-edition ISBN. KDP provides a free
> ASIN automatically; you do not need a new ISBN for the Kindle eBook.
