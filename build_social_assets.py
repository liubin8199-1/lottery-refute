# -*- coding: utf-8 -*-
"""生成社交平台专用素材：OG 横图、抖音 9:16 竖版海报。"""
import segno
from PIL import Image, ImageDraw, ImageFont

BASE = r"C:/Users/binliu8199/Desktop/refute-site/assets"
SRC_HERO = r"C:/Users/binliu8199/Downloads/金色实拍合成世界法律日公益宣传节日祝福微信公众号封面.png"
URL = "https://liubin8199-1.github.io/lottery-refute/"
FD = "C:/Windows/Fonts/"

def font(name, size, idx=0):
    return ImageFont.truetype(FD + name, size, index=idx)

yb = lambda s: font("msyhbd.ttc", s, 0)
yr = lambda s: font("msyh.ttc", s, 0)

# 品牌色
BRAND = (31, 111, 235)
INK = (28, 39, 51)
SUB = (91, 107, 123)
GREEN = (26, 157, 90)
RED = (214, 51, 51)
GOLD = (180, 130, 60)

def load_src_scaled(W, H):
    src = Image.open(SRC_HERO).convert("RGB")
    # cover 模式：等比缩放后居中裁剪
    scale = max(W / src.width, H / src.height)
    nw, nh = int(src.width * scale), int(src.height * scale)
    src = src.resize((nw, nh), Image.LANCZOS)
    x, y = (W - nw) // 2, (H - nh) // 2
    canvas = Image.new("RGB", (W, H), (245, 240, 230))
    canvas.paste(src, (x, y))
    return canvas

def add_gradient(base, width, alpha_max=130):
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for i in range(width):
        alpha = int(alpha_max * (1 - i / width))
        d.line([(i, 0), (i, base.height)], fill=(16, 14, 12, alpha), width=1)
    return Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")

def add_text_shadow(d, xy, text, fnt, fill, shadow=(30, 24, 18), offsets=None, anchor=None):
    offsets = offsets or [(-2, -2), (2, -2), (-2, 2), (2, 2)]
    x, y = xy
    kw = {"anchor": anchor} if anchor else {}
    for dx, dy in offsets:
        d.text((x+dx, y+dy), text, font=fnt, fill=shadow, **kw)
    d.text((x, y), text, font=fnt, fill=fill, **kw)

# ========== 1) OG 横图 1200x630 ==========
W, H = 1200, 630
img = load_src_scaled(W, H)
img = add_gradient(img, 560)
d = ImageDraw.Draw(img)
add_text_shadow(d, (50, 135), "开奖即随机", yb(86), (255, 255, 255))
d.text((54, 245), "彩票伪证档案库", font=yb(44), fill=(255, 230, 190))
lines = ["用官方全量开奖数据，", "证伪每一个「稳赚不赔」"]
y = 320
for line in lines:
    d.text((54, y), line, font=yr(28), fill=(255, 255, 255))
    y += 46
# 数据条
bar_y = y + 18
d.rounded_rectangle([54, bar_y, 500, bar_y + 50], radius=10, fill=(60, 52, 44))
d.text((74, bar_y + 25), "213 + 27 + 686 条方法 · 0 条跑赢随机", font=yr(22), fill=(255, 255, 255), anchor="lm")
img.save(f"{BASE}/og.png", "PNG", optimize=True)
print("og.png", img.size)

# ========== 2) 抖音 9:16 竖版海报 1080x1920 ==========
W, H = 1080, 1920
img = Image.new("RGB", (W, H), (246, 248, 251))
d = ImageDraw.Draw(img)

# 顶部品牌带
d.rectangle([0, 0, W, 360], fill=BRAND)
add_text_shadow(d, (W//2, 132), "开奖即随机", yb(92), (255,255,255), offsets=[(-3,-3),(3,-3),(-3,3),(3,3)], anchor="mm")
d.text((W//2, 248), "彩票伪证档案库 · 用全量数据证伪「稳赚不赔」", font=yr(28), fill=(223,232,255), anchor="mm")

# 导语
d.text((W//2, 430), "流传甚广的彩票秘籍，我们用官方全量开奖数据逐一回测", font=yr(30), fill=SUB, anchor="mm")

# 三卡（竖排，更大）
cards = [("213", "双色球秘籍", "0 条通过检验"),
         ("27", "福彩 3D 方法", "0 条通过检验"),
         ("686", "六合杀肖公式", "全 部 死 亡")]
cw, ch, gap, y0 = 880, 260, 34, 510
x0 = (W - cw) // 2
for i, (num, lab, sub) in enumerate(cards):
    y = y0 + i * (ch + gap)
    d.rounded_rectangle([x0, y, x0+cw, y+ch], radius=26, fill=(255,255,255), outline=(223,233,247), width=2)
    d.text((x0+cw//2, y+82), num, font=yb(120), fill=BRAND, anchor="mm")
    d.text((x0+cw//2, y+168), lab, font=yr(40), fill=INK, anchor="mm")
    d.text((x0+cw//2, y+222), sub, font=yr(32), fill=RED, anchor="mm")

# 结论印章
sx, sy, sw, sh = 180, 1380, 720, 110
d.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=55, fill=GREEN)
d.text((sx+sw//2, sy+sh//2), "全部 = 闭眼随机", font=yb(58), fill=(255,255,255), anchor="mm")

# 说明
d.text((W//2, 1550), "数学证明：只要摇奖机独立，杀号公式不可能跑赢随机", font=yr(28), fill=SUB, anchor="mm")

# 底部分享带
share_y = 1620
d.rectangle([0, share_y, W, H], fill=(232, 240, 254))
# 二维码
q = segno.make(URL, error='q')
q.save(f"{BASE}/qr-douyin.png", scale=12, border=2, dark="#1f6feb", light="#ffffff")
qr = Image.open(f"{BASE}/qr-douyin.png").convert("RGB").resize((340, 340))
img.paste(qr, (90, share_y+70))
d.text((500, share_y+140), "扫码查看完整证伪档案", font=yb(46), fill=INK, anchor="lm")
d.text((500, share_y+216), "liubin8199-1.github.io/lottery-refute", font=yr(30), fill=BRAND, anchor="lm")
d.text((500, share_y+288), "理性购彩 · 量力而行", font=yr(28), fill=SUB, anchor="lm")
d.text((W//2, H-34), "本站仅为统计验证与科普，不构成任何投注建议", font=yr(22), fill=SUB, anchor="mm")

img.save(f"{BASE}/poster-douyin.png", "PNG", optimize=True)
print("poster-douyin.png", img.size)

# ========== 3) 小红书 3:4 竖版海报 1080x1440 ==========
W, H = 1080, 1440
img = Image.new("RGB", (W, H), (246, 248, 251))
d = ImageDraw.Draw(img)

d.rectangle([0, 0, W, 300], fill=BRAND)
add_text_shadow(d, (W//2, 115), "开奖即随机", yb(80), (255,255,255), offsets=[(-3,-3),(3,-3),(-3,3),(3,3)], anchor="mm")
d.text((W//2, 220), "彩票伪证档案库 · 用全量数据证伪「稳赚不赔」", font=yr(26), fill=(223,232,255), anchor="mm")

d.text((W//2, 350), "流传甚广的彩票秘籍，我们用官方全量开奖数据逐一回测", font=yr(26), fill=SUB, anchor="mm")

cw, ch, gap, y0 = 880, 190, 24, 400
x0 = (W - cw) // 2
for i, (num, lab, sub) in enumerate(cards):
    y = y0 + i * (ch + gap)
    d.rounded_rectangle([x0, y, x0+cw, y+ch], radius=22, fill=(255,255,255), outline=(223,233,247), width=2)
    d.text((x0+cw//2, y+62), num, font=yb(90), fill=BRAND, anchor="mm")
    d.text((x0+cw//2, y+124), lab, font=yr(30), fill=INK, anchor="mm")
    d.text((x0+cw//2, y+162), sub, font=yr(24), fill=RED, anchor="mm")

sx, sy, sw, sh = 180, 1020, 720, 96
d.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=48, fill=GREEN)
d.text((sx+sw//2, sy+sh//2), "全部 = 闭眼随机", font=yb(50), fill=(255,255,255), anchor="mm")

share_y = 1180
d.rectangle([0, share_y, W, H], fill=(232, 240, 254))
qr = Image.open(f"{BASE}/qr-douyin.png").convert("RGB").resize((250, 250))
img.paste(qr, (70, share_y+36))
d.text((372, share_y+90), "扫码查看完整证伪档案", font=yb(38), fill=INK, anchor="lm")
d.text((372, share_y+152), "liubin8199-1.github.io/lottery-refute", font=yr(26), fill=BRAND, anchor="lm")
d.text((372, share_y+206), "理性购彩 · 量力而行", font=yr(24), fill=SUB, anchor="lm")
d.text((W//2, H-30), "本站仅为统计验证与科普，不构成任何投注建议", font=yr(20), fill=SUB, anchor="mm")

img.save(f"{BASE}/poster-xhs.png", "PNG", optimize=True)
print("poster-xhs.png", img.size)
