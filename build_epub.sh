#!/usr/bin/env bash
# Build the Kindle-ready EPUB for "Yeshua: Jesus Without Christianity".
set -euo pipefail
cd "$(dirname "$0")"

OUT="manuscript/Yeshua-Jesus-Without-Christianity.epub"

pandoc \
  --from=markdown+smart \
  --to=epub3 \
  --output="$OUT" \
  --metadata-file=manuscript/metadata.yaml \
  --epub-cover-image=manuscript/cover.jpg \
  --css=manuscript/style.css \
  --toc \
  --toc-depth=2 \
  --split-level=1 \
  manuscript/copyright.md \
  book/00_frontmatter.md \
  book/ch01.md book/ch02.md book/ch03.md book/ch04.md book/ch05.md \
  book/ch06.md book/ch07.md book/ch08.md book/ch09.md book/ch10.md \
  book/ch11.md book/ch12.md book/ch13.md book/ch14.md

echo "Built: $OUT"
ls -la "$OUT"
