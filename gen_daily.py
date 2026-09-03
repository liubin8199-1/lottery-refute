# -*- coding: utf-8 -*-
"""
gen_daily.py — 彩票伪证档案库「每日观测」数据生成器（stdlib-only，无第三方依赖）

产出：
  data/daily.js  ->  window.SSQ_DAILY  (双色球 金胆/三胆/杀号/复式 + 一期前瞻命中率对照)
                    window.FC3D_DAILY (福彩3D v42 预测候选 + observation-only 观测层画像)

数据源（读取即路径，点开即用）：
  璇玑V2/xuanji/ssq/data/history.csv                      双色球官方历史开奖
  璇玑V2/xuanji/outputs/FC3D_预测与观测_*.md              福彩3D 每日预测+观测

设计原则（合规）：
  1. 双色球「金胆/三胆/杀号/复式」用系统既定方法 综合分 = 0.4×频率 + 0.6×遗漏 得出，
     与站点 #ssq 证伪档案的方法论一致；而非凭空捏造。
  2. 一并对金胆/三胆做全量一期前瞻回测，给出命中率 vs 随机基线，
     让访客当场看到「这套输出 ≈ 蒙眼随机」——这正是全站主题。
  3. 福彩3D 仅搬运系统既有的 observation-only 观测层（不投票、不改期望），并附 iid 随机诚实说明。
  4. 所有内容为纯观测 / 科普，不构成任何投注建议。

重跑：python gen_daily.py  （建议在每次开奖后、下期开奖前执行，再 git 提交刷新站点）
"""
import csv, json, os, re, math, glob, datetime

BASE = "C:/Users/binliu8199/WorkBuddy/璇玑V2/xuanji"
HIST = BASE + "/ssq/data/history.csv"
FC3D_DIR = BASE + "/outputs"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "daily.js")


# ============================================================
# 双色球 SSQ
# ============================================================
def qnum(q):
    d = re.sub(r"\D", "", q)
    return int(d) if d else 0


def load_ssq():
    rows = []
    with open(HIST, encoding="utf-8") as f:
        for x in csv.DictReader(f):
            try:
                reds = [int(x["红球%d" % k]) for k in range(1, 7)]
                blue = int(x["蓝球"])
                if all(1 <= v <= 33 for v in reds) and 1 <= blue <= 16:
                    rows.append({"reds": reds, "blue": blue, "qh": x["期号"].strip()})
            except Exception:
                pass
    rows.sort(key=lambda r: qnum(r["qh"]))
    return rows


def combo_score(freq, lastseen, idx):
    """综合分 = 0.4×频率 + 0.6×遗漏（均归一化）。idx = 可用期数（rows[0..idx-1]）。"""
    maxf = max(freq) or 1
    omis = {}
    mx = 1
    for v in range(1, 34):
        m = (idx - 1) - lastseen[v] if lastseen[v] >= 0 else idx
        omis[v] = m
        if m > mx:
            mx = m
    return {v: 0.4 * (freq[v] / maxf) + 0.6 * (omis[v] / mx) for v in range(1, 34)}


def ssq_eval(rows):
    """增量一期前瞻回测 + 生成下期(当天)预测。"""
    freq = [0] * 34
    lastseen = [-10 ** 9] * 34
    gold_hits = 0
    three_hits = 0
    n = 0
    for i in range(len(rows)):
        if i >= 1:
            comp = combo_score(freq, lastseen, i)  # 用 rows[0..i-1] 预测第 i 期
            ranked = sorted(range(1, 34), key=lambda v: -comp[v])
            gold = ranked[0]
            three = ranked[:3]
            nxt = rows[i]["reds"]
            if gold in nxt:
                gold_hits += 1
            if any(t in nxt for t in three):
                three_hits += 1
            n += 1
        for v in rows[i]["reds"]:
            freq[v] += 1
            lastseen[v] = i
    # 当下(用全量)预测下一期
    comp = combo_score(freq, lastseen, len(rows))
    ranked = sorted(range(1, 34), key=lambda v: -comp[v])

    # 蓝球综合分（1..16）
    bfreq = [0] * 17
    blast = [-10 ** 9] * 17
    for i, r in enumerate(rows):
        bfreq[r["blue"]] += 1
        blast[r["blue"]] = i
    bmaxf = max(bfreq) or 1
    bmx = 1
    bomis = {}
    for v in range(1, 17):
        m = (len(rows) - 1) - blast[v] if blast[v] >= 0 else len(rows)
        bomis[v] = m
        if m > bmx:
            bmx = m
    bcomp = {v: 0.4 * (bfreq[v] / bmaxf) + 0.6 * (bomis[v] / bmx) for v in range(1, 17)}
    blue_ranked = sorted(range(1, 17), key=lambda v: -bcomp[v])

    # 随机基线
    gold_base = 6 / 33
    three_base = 1 - math.comb(30, 6) / math.comb(33, 6)
    kill_base = math.comb(27, 6) / math.comb(33, 6)  # 杀 6 个全不中(正确)的概率

    gold_rate = gold_hits / n if n else 0
    three_rate = three_hits / n if n else 0

    return {
        "source_qh": rows[-1]["qh"],
        "next_qh": str(qnum(rows[-1]["qh"]) + 1),
        "n_periods": len(rows),
        "gold": ranked[0],
        "three": ranked[:3],
        "kill": ranked[-6:][::-1],          # 综合分最低 6 个 = 系统认为最不可能出现
        "combo_reds": ranked[:15],          # 复式口径：前 15 红
        "blue_top5": blue_ranked[:5],
        "honest": {
            "gold_rate": round(gold_rate, 4),
            "gold_base": round(gold_base, 4),
            "three_rate": round(three_rate, 4),
            "three_base": round(three_base, 4),
            "kill_base": round(kill_base, 4),
            "n_oos": n,
            "note": ("一期前瞻回测：用第 i 期及之前数据算金胆/三胆，核对第 i+1 期是否命中。"
                     "金胆命中率≈随机基线 6/33，三胆命中率≈随机基线 1−C(30,6)/C(33,6)；"
                     "说明这套输出与蒙眼随机无差异，请勿据此下注。"),
        },
    }


# ============================================================
# 福彩3D FC3D
# ============================================================
def load_fc3d_latest():
    files = glob.glob(os.path.join(FC3D_DIR, "FC3D_预测与观测_*.md"))
    if not files:
        return None
    def num(p):
        m = re.search(r"(\d{7})", os.path.basename(p))
        return int(m.group(1)) if m else 0
    files.sort(key=num)
    path = files[-1]
    txt = open(path, encoding="utf-8").read()

    def block(label):
        m = re.search(label + r"[:：]\s*([0-9 ]+)", txt)
        return re.findall(r"\d{3}", m.group(1)) if m else []

    single = block("单选 Top10")
    z3 = block("组三 Top10")
    z6 = block("组六 Top10")
    mprev = re.search(r"上期 `(\d{3})`", txt)
    prev = mprev.group(1) if mprev else ""
    mt = re.search(r"生成时间[:：]\s*([0-9:\-\s]+?)(?:\s*模式|$)", txt)
    gen = mt.group(1).strip() if mt else ""

    # 解析三张观测表（断组/冷热/盲区）
    tables = []
    for b in re.split(r"\n## ", txt):
        lines = [l for l in b.split("\n") if l.strip().startswith("|")]
        if len(lines) >= 3:
            hdr = [c.strip() for c in lines[0].strip("|").split("|")]
            rows_t = []
            for l in lines[2:]:
                cells = [c.strip() for c in l.strip("|").split("|")]
                rows_t.append(cells)
            tables.append({"hdr": hdr, "rows": rows_t})

    duan = hot = blind = None
    for t in tables:
        if len(t["hdr"]) == 3 and t["hdr"][0] == "候选":
            duan = t
        elif len(t["hdr"]) == 4 and t["hdr"][0] == "候选":
            hot = t
        elif len(t["hdr"]) == 2 and t["hdr"][0] == "候选":
            blind = t

    mqh = re.search(r"预测期 (\d{7})", txt)
    next_qh = str(int(mqh.group(1)) + 1) if mqh else ""

    return {
        "file": os.path.basename(path),
        "generated": gen,
        "prev_draw": prev,
        "next_qh": next_qh,
        "single_top10": single,
        "z3_top10": z3,
        "z6_top10": z6,
        "tables": {"duan": duan, "hot": hot, "blind": blind},
        "note": ("FC3D 开奖为 iid 随机（系统前后 3 次独立回测已证：独胆公式≈随机、"
                 "WT家园杀号 ROI −42.7%、万能四码 ROI −27.9%）。观测层仅作复盘画像，"
                 "对命中率无正向增益，不构成投注信号。"),
    }


def main():
    rows = load_ssq()
    ssq = ssq_eval(rows)
    fc3d = load_fc3d_latest()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    out = "// 自动生成 by gen_daily.py · %s · 纯观测/科普，不构成投注建议\n" % now
    out += "window.SSQ_DAILY = " + json.dumps(ssq, ensure_ascii=False, indent=2) + ";\n"
    out += "window.FC3D_DAILY = " + json.dumps(fc3d, ensure_ascii=False, indent=2) + ";\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print("写入:", OUT)
    print("SSQ 下一期预测:", ssq["next_qh"], "| 金胆:", ssq["gold"], "| 三胆:", ssq["three"],
          "| 杀号:", ssq["kill"], "| 蓝球Top5:", ssq["blue_top5"])
    print("SSQ 诚实回测: 金胆命中率=%.4f (基线%.4f) / 三胆命中率=%.4f (基线%.4f) / 样本=%d"
          % (ssq["honest"]["gold_rate"], ssq["honest"]["gold_base"],
             ssq["honest"]["three_rate"], ssq["honest"]["three_base"], ssq["honest"]["n_oos"]))
    if fc3d:
        print("FC3D 文件:", fc3d["file"], "| 上期:", fc3d["prev_draw"], "| 预测期:", fc3d["next_qh"])


if __name__ == "__main__":
    main()
