#!/usr/bin/env python3
"""Generate a clean typographic cover for the Kindle edition."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
# Palette: deep ink-blue background, warm off-white type, muted gold accent
BG      = (20, 28, 44)
PANEL   = (27, 37, 58)
CREAM   = (238, 232, 219)
GOLD    = (197, 162, 94)
MUTED   = (150, 162, 184)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

SERIF      = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS       = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def center_text(text, y, fnt, fill, tracking=0):
    if tracking == 0:
        w = d.textlength(text, font=fnt)
        d.text(((W - w) / 2, y), text, font=fnt, fill=fill)
        bbox = d.textbbox((0, 0), text, font=fnt)
        return y + (bbox[3] - bbox[1])
    # letter-spaced
    widths = [d.textlength(ch, font=fnt) + tracking for ch in text]
    total = sum(widths) - tracking
    x = (W - total) / 2
    for ch, wch in zip(text, widths):
        d.text((x, y), ch, font=fnt, fill=fill)
        x += wch
    bbox = d.textbbox((0, 0), "Ag", font=fnt)
    return y + (bbox[3] - bbox[1])

# Top thin rule + author
center_text("SILVIU ROTARIU", 235, font(SANS, 58), MUTED, tracking=14)
d.line([(W/2 - 170, 340), (W/2 + 170, 340)], fill=GOLD, width=3)

# Title block: YESHUA (large)
center_text("YESHUA", 560, font(SERIF_BOLD, 300), CREAM)

# Subtitle
center_text("JESUS", 1010, font(SERIF, 96), GOLD, tracking=8)
center_text("WITHOUT", 1130, font(SERIF, 96), GOLD, tracking=8)
center_text("CHRISTIANITY", 1250, font(SERIF, 96), GOLD, tracking=8)

# Lower descriptive line
d.line([(W/2 - 320, 2090), (W/2 + 320, 2090)], fill=(70, 84, 110), width=2)
center_text("Encountering the Galilean before the religion", 2160,
            font(SERIF, 50), MUTED)

img.save("manuscript/cover.jpg", "JPEG", quality=92)
img.save("manuscript/cover.png", "PNG")
print("cover written:", img.size)
