# -*- coding: utf-8 -*-
import segno
from PIL import Image, ImageDraw, ImageFont

BASE = r"C:/Users/binliu8199/Desktop/refute-site/assets"
URL = "https://liubin8199-1.github.io/lottery-refute/"

# 1) 二维码 PNG（segno 原生写 PNG，无中文、无乱码）
q = segno.make(URL, error='q')
q.save(f"{BASE}/qr.png", scale=10, border=2, dark="#1f6feb", light="#ffffff")

# 2) 推广海报 PNG（Pillow 手绘 + 微软雅黑，中文正常）
W, H = 1080, 1350
img = Image.new("RGB", (W, H), (246, 248, 251))
d = ImageDraw.Draw(img)
FD = "C:/Windows/Fonts/"

def font(name, size, idx=0):
    return ImageFont.truetype(FD + name, size, index=idx)

yb = lambda s: font("msyhbd.ttc", s, 0)   # 雅黑粗
yr = lambda s: font("msyh.ttc", s, 0)     # 雅黑常规

BRAND = (31, 111, 235)
INK = (28, 39, 51)
SUB = (91, 107, 123)
GREEN = (26, 157, 90)
RED = (214, 51, 51)
LBLUE = (232, 240, 254)

# 顶部品牌带
d.rectangle([0, 0, W, 260], fill=BRAND)
d.text((W / 2, 102), "开奖即随机", font=yb(84), fill=(255, 255, 255), anchor="mm")
d.text((W / 2, 196), "彩票伪证档案库 · 用全量数据证伪每一个「稳赚不赔」",
       font=yr(27), fill=(223, 232, 255), anchor="mm")

# 导语
d.text((W / 2, 332), "流传甚广的彩票秘籍，我们用官方全量开奖数据逐一回测",
       font=yr(30), fill=SUB, anchor="mm")

# 三张数据卡
cards = [("213", "双色球秘籍", "0 条通过检验"),
         ("27", "福彩 3D 方法", "0 条通过检验"),
         ("686", "六合杀肖公式", "全 部 死 亡")]
cw, ch, gap, y0 = 320, 212, 30, 418
x0 = 30
for i, (num, lab, sub) in enumerate(cards):
    x = x0 + i * (cw + gap)
    d.rounded_rectangle([x, y0, x + cw, y0 + ch], radius=22,
                        fill=(255, 255, 255), outline=(223, 233, 247), width=2)
    d.text((x + cw / 2, y0 + 72), num, font=yb(92), fill=BRAND, anchor="mm")
    d.text((x + cw / 2, y0 + 142), lab, font=yr(30), fill=INK, anchor="mm")
    d.text((x + cw / 2, y0 + 182), sub, font=yr(26), fill=RED, anchor="mm")

# 中央结论印章
sx, sy, sw, sh = 280, 700, 520, 92
d.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=46, fill=GREEN)
d.text((sx + sw / 2, sy + sh / 2), "全部 = 闭眼随机", font=yb(48),
       fill=(255, 255, 255), anchor="mm")

# 说明
d.text((W / 2, 858), "数学证明：只要摇奖机独立，杀号公式一条都不可能跑赢随机",
       font=yr(26), fill=SUB, anchor="mm")

# 底部分享带
d.rectangle([0, 1052, W, H], fill=LBLUE)
qr = Image.open(f"{BASE}/qr.png").convert("RGB").resize((250, 250))
img.paste(qr, (70, 1092))
d.text((372, 1124), "扫码查看完整证伪档案", font=yb(40), fill=INK, anchor="lm")
d.text((372, 1182), "liubin8199-1.github.io/lottery-refute",
       font=yr(28), fill=BRAND, anchor="lm")
d.text((372, 1240), "理性购彩 · 量力而行", font=yr(26), fill=SUB, anchor="lm")
d.text((W / 2, 1312), "本站仅为统计验证与科普，不构成任何投注建议",
       font=yr(20), fill=SUB, anchor="mm")

img.save(f"{BASE}/poster.png")
print("poster.png 生成成功", img.size)
