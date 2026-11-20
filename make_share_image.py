# Run once inside the my-website folder (the one that contains the images folder):
#   python make_share_image.py
# Creates images/share.jpg = the link-preview card shown on WhatsApp/Google.
# It uses YOUR logo (images/logo.png). If there is no logo it uses images/photo.jpg.
# The design is centred so it still looks right when WhatsApp crops it to a square.
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

NAVY, AMBER, WHITE, SOFT = (13, 27, 42), (245, 166, 35), (255, 255, 255), (205, 214, 226)
W, H = 1200, 630

def font(size, bold=True):
    names = (["arialbd.ttf", "segoeuib.ttf", "DejaVuSans-Bold.ttf"] if bold
             else ["arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"])
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            pass
    return ImageFont.load_default()

def centered(d, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)

src = "images/logo.png" if os.path.exists("images/logo.png") else "images/photo.jpg"
print("Using", src)

card = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(card)
for x in range(0, W, 48):                      # blueprint grid
    d.line([(x, 0), (x, H)], fill=(24, 40, 60), width=1)
for y in range(0, H, 48):
    d.line([(0, y), (W, y)], fill=(24, 40, 60), width=1)
d.rectangle([0, 0, W, 10], fill=AMBER)
d.rectangle([0, H - 10, W, H], fill=AMBER)

# logo in a circle, centred at the top
S = 290
logo = Image.open(src).convert("RGBA")
logo = ImageOps.fit(logo, (S, S), Image.LANCZOS, centering=(0.5, 0.3))
mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).ellipse([0, 0, S - 1, S - 1], fill=255)
lx, ly = (W - S) // 2, 45
d.ellipse([lx - 10, ly - 10, lx + S + 10, ly + S + 10], fill=AMBER)
card.paste(logo.convert("RGB"), (lx, ly), mask)

centered(d, 365, "Gabriel Mukamba", font(68), WHITE)
centered(d, 455, "Civil Engineering Student", font(34, False), AMBER)
centered(d, 505, "& Web Developer  |  Kampala, Uganda", font(30, False), SOFT)

for q in (88, 82, 76, 70, 64, 58, 52):         # WhatsApp ignores images over ~300 KB
    card.save("images/share.jpg", "JPEG", quality=q, optimize=True)
    if os.path.getsize("images/share.jpg") < 250 * 1024:
        break
print("Created images/share.jpg", round(os.path.getsize("images/share.jpg") / 1024), "KB")