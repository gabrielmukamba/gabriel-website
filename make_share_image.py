# Run once inside the my-website folder (the one that contains the images folder):
#   pip install pillow
#   python make_share_image.py
# Creates: images/share.jpg (link preview for WhatsApp/Google).
# Your own logo stays as images/logo.png - this script never changes it.
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

PHOTO = "images/photo.jpg"
NAVY, AMBER, WHITE = (13, 27, 42), (245, 166, 35), (255, 255, 255)

def font(size, bold=True):
    names = (["arialbd.ttf", "segoeuib.ttf", "DejaVuSans-Bold.ttf"] if bold
             else ["arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"])
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            pass
    return ImageFont.load_default()

photo = Image.open(PHOTO).convert("RGB")

# ---------- share.jpg (1200x630) ----------
W, H = 1200, 630
card = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(card)
for x in range(0, W, 48):                      # blueprint grid
    d.line([(x, 0), (x, H)], fill=(24, 40, 60), width=1)
for y in range(0, H, 48):
    d.line([(0, y), (W, y)], fill=(24, 40, 60), width=1)
d.rectangle([0, 0, 14, H], fill=AMBER)

pw, ph = 390, 500
pic = ImageOps.fit(photo, (pw, ph), Image.LANCZOS, centering=(0.5, 0.2))
mask = Image.new("L", (pw, ph), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, pw, ph], radius=28, fill=255)
px, py = 740, (H - ph) // 2
d.rounded_rectangle([px - 6, py - 6, px + pw + 6, py + ph + 6], radius=34, fill=AMBER)
card.paste(pic, (px, py), mask)

# put YOUR logo (images/logo.png) on the card if it exists
if os.path.exists("images/logo.png"):
    lg = Image.open("images/logo.png").convert("RGBA")
    lg.thumbnail((110, 110))
    card.paste(lg, (70, 40), lg)

d.text((70, 150), "CIVIL ENGINEERING  |  WEB DEVELOPMENT", font=font(24), fill=AMBER)
d.text((70, 205), "Gabriel", font=font(92), fill=WHITE)
d.text((70, 305), "Mukamba", font=font(92), fill=WHITE)
d.text((70, 430), "Civil Engineering Student", font=font(34, False), fill=(215, 222, 232))
d.text((70, 475), "& Web Developer  |  Kampala, Uganda", font=font(34, False), fill=(215, 222, 232))

for q in (85, 80, 75, 70, 65, 60, 55, 50):
    card.save("images/share.jpg", "JPEG", quality=q, optimize=True)
    if os.path.getsize("images/share.jpg") < 280 * 1024:
        break
print("Created images/share.jpg", round(os.path.getsize("images/share.jpg") / 1024), "KB")