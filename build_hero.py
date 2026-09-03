# -*- coding: utf-8 -*-
"""用用户提供的金色天平图生成站点 hero 横幅（带文字叠加）。"""
from PIL import Image, ImageDraw, ImageFont

SRC = r"C:/Users/binliu8199/Downloads/金色实拍合成世界法律日公益宣传节日祝福微信公众号封面.png"
OUT = r"C:/Users/binliu8199/Desktop/refute-site/assets/hero.png"
FD = "C:/Windows/Fonts/"

def font(name, size, idx=0):
    return ImageFont.truetype(FD + name, size, index=idx)

src = Image.open(SRC).convert("RGB")
W, H = 1200, 480

# 等比缩放至高度 480
scale = H / src.height
nw = int(src.width * scale)
src = src.resize((nw, H), Image.LANCZOS)

# 拼成 1200x480：原图右对齐，左侧不足部分用原图最左列像素平铺
base = Image.new("RGB", (W, H))
left_col = src.crop((0, 0, 1, H))
for x in range(W - nw):
    base.paste(left_col, (x, 0))
base.paste(src, (W - nw, 0))

# 左侧暗角遮罩（RGBA 渐变，再合成）
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
for i in range(460):
    alpha = int(132 * (1 - i / 460))
    draw.line([(i, 0), (i, H)], fill=(18, 16, 14, alpha), width=1)
base = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")

# 文字层（带轻微投影）
d = ImageDraw.Draw(base)
yb = lambda s: font("msyhbd.ttc", s, 0)
yr = lambda s: font("msyh.ttc", s, 0)

# 主标题投影
for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
    d.text((44+dx, 114+dy), "开奖即随机", font=yb(82), fill=(30, 24, 18))
d.text((44, 114), "开奖即随机", font=yb(82), fill=(255, 255, 255))

# 副标题
d.text((48, 220), "彩票伪证档案库", font=yb(42), fill=(255, 230, 190))

# 说明行
lines = ["用官方全量开奖数据，", "证伪每一个「稳赚不赔」"]
y = 290
for line in lines:
    d.text((48, y), line, font=yr(26), fill=(255, 255, 255))
    y += 42

# 底部数据条
bar_y = y + 20
d.rounded_rectangle([48, bar_y, 432, bar_y + 44], radius=8, fill=(60, 52, 44))
d.text((68, bar_y + 22), "213 + 27 + 686 条方法 · 全部 = 随机", font=yr(20), fill=(255, 255, 255), anchor="lm")

base.save(OUT, "PNG", optimize=True)
print("hero.png 生成成功", base.size)
