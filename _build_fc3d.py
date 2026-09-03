# -*- coding: utf-8 -*-
"""生成 data/fc3d.js —— 福彩3D 证伪详表
口径与 SSQ 完全一致：
  lift = 基线漏杀率 / 实测漏杀率   (杀号类)
       = 实测命中率 / 基线命中率   (取胆/选号类)
  两者均 >1 表示"优于随机"
  z : 正号 = 劣于随机；负号 = 看似优于随机（与 SSQ 表格约定一致）
全部数字来自 outputs/ 下已核实的回测报告，不编造。
"""
import json, math, io, os

def z_of(miss, miss0, n):
    se = math.sqrt(miss0 * (1 - miss0) / n)
    return (miss - miss0) / se

rows = []

def kill(cat, formula, note, hit_rate, base_hit, n):
    """杀号类：hit_rate=实测杀对率, base_hit=基线杀对率"""
    miss = 1 - hit_rate
    miss0 = 1 - base_hit
    lift = miss0 / miss
    z = z_of(miss, miss0, n)
    rows.append(dict(cat=cat, formula=formula, note=note,
                     lift=round(lift, 4), z=round(-z if False else z, 3),
                     n=n, hit=round(hit_rate * 100, 2),
                     base=round(base_hit * 100, 2)))

def hit(cat, formula, note, hit_rate, base_hit, n):
    """取胆/选号类：hit_rate=实测命中率, base_hit=基线命中率"""
    lift = hit_rate / base_hit
    # 命中率低 = 劣于随机 -> z 取正
    z = -(hit_rate - base_hit) / math.sqrt(base_hit * (1 - base_hit) / n)
    rows.append(dict(cat=cat, formula=formula, note=note,
                     lift=round(lift, 4), z=round(z, 3),
                     n=n, hit=round(hit_rate * 100, 2),
                     base=round(base_hit * 100, 2)))

# ── 1. 秘籍·《杀号公式准确率大比拼》代表公式（n=4698，全量 2013002~2026194）──
K = "秘籍·杀号公式大比拼"
kill(K, "A 和值尾+跨度个位数 绝杀十位", "文章声明 98%", 0.9008, 0.90, 4698)
kill(K, "B 和尾−3 绝杀百位",            "文章声明 97%", 0.9008, 0.90, 4698)
kill(K, "C 期尾+4 绝杀十位",            "文章声明 95%", 0.8976, 0.90, 4698)
kill(K, "D 上期十位 杀本期十位",         "文章声明 91%", 0.8972, 0.90, 4698)
kill(K, "E 上期个位 杀本期百位",         "文章声明 94%", 0.9057, 0.90, 4698)
kill(K, "F 开奖号×123 第一位 杀百位",    "文章声明 94%", 0.9000, 0.90, 4698)
hit (K, "G 和值尾左右号 取胆3码",        "文章声明 57%", 0.6543, 0.657, 4698)

# ── 2. 秘籍·《合值分位杀号铁律》（n=4698，有精确计数）──
K2 = "秘籍·合值分位杀号铁律"
kill(K2, "上期合值尾→杀百位", "4234/4698", 4234 / 4698, 0.90, 4698)
kill(K2, "上期合值尾→杀十位", "4268/4698", 4268 / 4698, 0.90, 4698)
kill(K2, "上期合值尾→杀个位", "4258/4698", 4258 / 4698, 0.90, 4698)
kill(K2, "三位全杀对",        "3476/4698", 3476 / 4698, 0.729, 4698)

# ── 3. 冷号杀号法 · walk-forward 样本外（n=4695，基线取随机对照实测）──
K3 = "冷号杀号法·样本外"
kill(K3, "全样本最冷3号 杀百位", "wf；随机对照 70.00%", 0.6947, 0.7000, 4695)
kill(K3, "全样本最冷3号 杀十位", "wf；随机对照 70.02%", 0.6898, 0.7002, 4695)
kill(K3, "全样本最冷3号 杀个位", "wf；随机对照 69.99%", 0.7020, 0.6999, 4695)
kill(K3, "三位全杀对",           "wf；随机对照 34.28%", 0.3353, 0.3428, 4695)

# ── 4. 两待测变体 · 全量 OOS（真跑，含 p 值）──
K4 = "两变体·全量OOS"
kill(K4, "A 和值×百位+1 取模3 → 杀数字R",  "p=0.457", 0.7328, 0.7290, 4705)
kill(K4, "A 同上 → 杀和值尾R",             "p=0.490", 0.9014, 0.8991, 4705)
kill(K4, "B 相邻号差的各位和 → 杀数字R",    "p=1.268", 0.7283, 0.7290, 4704)
kill(K4, "B 同上 → 单位置(百位)",          "p=1.645", 0.8965, 0.9000, 4704)

# ── 5. 1D 选号策略 · walk-forward（n=3693，warmup=1000，基线 27.10%）──
K5 = "1D选号策略·样本外"
hit(K5, "追冷号（选最久未出数字）", "1066/3693；置换检验 p=0.040", 1066 / 3693, 0.2710, 3693)
hit(K5, "奇偶轮动（欠方最小遗漏）", "1044/3693", 1044 / 3693, 0.2710, 3693)
hit(K5, "跨度法（上期跨度作胆）",   "1043/3693", 1043 / 3693, 0.2710, 3693)
hit(K5, "重号（取上期首位）",       "1029/3693", 1029 / 3693, 0.2710, 3693)
hit(K5, "追热号（近期高频）",       "1001/3693", 1001 / 3693, 0.2710, 3693)
hit(K5, "邻号（上期邻号最小遗漏）",  "992/3693",  992 / 3693, 0.2710, 3693)

# ── 6. 四维共振缩水（n=4695，基线=静态注数占比）──
K6 = "四维共振缩水"
hit(K6, "三维共振（46 注 / 4.6%）", "236/4695；+0.43pp", 236 / 4695, 0.046, 4695)
hit(K6, "四维共振（10 注 / 1.0%）", "50/4695；+0.06pp",   50 / 4695, 0.010, 4695)

# ── 汇总统计 ──
lifts = [r["lift"] for r in rows]
absz = [abs(r["z"]) for r in rows]
maxz = round(max(absz), 3)
# Bonferroni: alpha=0.05 / N
N = len(rows)
alpha = 0.05 / N
# 双侧 z 临界
def zcrit(alpha_two):
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        p = math.erfc(mid / math.sqrt(2))  # 双侧
        if p > alpha_two:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2, 2)
thr = zcrit(alpha)
passing = sum(1 for r in rows if abs(r["z"]) >= thr)

# 分类聚合
cats = {}
for r in rows:
    c = cats.setdefault(r["cat"], dict(cat=r["cat"], n=0, maxz=0.0))
    c["n"] += 1
    c["maxz"] = round(max(c["maxz"], abs(r["z"])), 2)
cats = sorted(cats.values(), key=lambda x: -x["n"])

data = dict(
    meta=dict(
        total=N,
        window="全量 4696 期（2013002~2026201，官方历史开奖库）",
        maxz=maxz,
        thresh=thr,
        passing=passing,
        updated="2026-09-03",
        reports=[
            dict(title="《杀号公式准确率大比拼》代表公式 全量回测",
                 note="4698 期 · 7 条代表公式全部回归基线"),
            dict(title="《合值分位杀号铁律》全量回测",
                 note="4698 期 · 含随机映射×1000 零分布对照"),
            dict(title="冷号杀号法 walk-forward 样本外回测",
                 note="4695 期 · 只用历史重算冷号，杜绝循环论证"),
            dict(title="两待测变体 全量 OOS 证伪",
                 note="4705/4704 期 · 逐期回放 + 二项 z 检验"),
            dict(title="1D 选号策略 walk-forward 回测",
                 note="3693 期 · 含 300 次置换检验（p=0.040 边缘）"),
            dict(title="「四维共振筛选器」全量回测",
                 note="4695 期 · 命中率 = 注数占比，筛选无效"),
        ],
    ),
    cats=cats,
    rows=rows,
)

out = io.StringIO()
out.write("// 福彩3D 证伪档案 —— 全部数字来自已核实的全量回测报告，无编造\n")
out.write("window.FC3D_DATA = ")
out.write(json.dumps(data, ensure_ascii=False, indent=1))
out.write(";\n")

os.makedirs("data", exist_ok=True)
with open("data/fc3d.js", "w", encoding="utf-8") as f:
    f.write(out.getvalue())

print("条目数 N =", N)
print("Bonferroni 阈值 |z| >=", thr, " (alpha=0.05/%d)" % N)
print("max|z| =", maxz, " 过阈值条数 =", passing)
print("lift 范围: %.4f ~ %.4f" % (min(lifts), max(lifts)))
print("分类数 =", len(cats))
print("\n分类分布:")
for c in cats:
    print("  %-28s %2d 条  max|z|=%.2f" % (c["cat"], c["n"], c["maxz"]))
print("\n|z| 最大的 5 条:")
for r in sorted(rows, key=lambda x: -abs(x["z"]))[:5]:
    print("  |z|=%.3f  lift=%.4f  %s / %s" % (abs(r["z"]), r["lift"], r["cat"], r["formula"]))
