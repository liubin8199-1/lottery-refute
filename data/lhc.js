// 六合彩（澳门）证伪档案 —— 全部数字来自璇玑系统已核实 OOS 回测与《官方数据一致性核查报告》(2026-08-30 修复后重跑)，无编造
window.LHC_DATA = {
 "meta": {
  "total": 686,
  "window": "OOS P30~P241（212 期，2026 全量开奖）· 璇玑系统回放",
  "maxz": 1.06,
  "thresh": 3.11,
  "passing": 0,
  "updated": "2026-11-02",
  "recheck": "2026-11 续测：纯观测窗口推进至 P301（数据至 P306），新增「杀 3 尾集成」「含平码杀区」两组独立观测，结论与 9 月一致——全部收敛回随机基线，无一显著。",
  "reports": [
   {"title":"686 条杀肖公式 · 全部死亡","note":"OOS P30~P241 共 212 期，686/686 = 100%"},
   {"title":"首次触发即死率 90.2%","note":"619/686 首次触发即判定死亡，半衰期 T50=1"},
   {"title":"观测漏杀率 92.3% vs 随机基线 91.6%","note":"z=1.06, p=0.291，不显著"},
   {"title":"分层 9 组 p 值 0.365–0.836","note":"全部 >0.05，无分组优势"},
   {"title":"Logistic OR=1.001 (p=0.963)","note":"无条件模型 n=5988，与随机无差异"},
   {"title":"平肖 p=0.765 / 生肖盲区不成立 / 开奖≈iid","note":"主系统多项 OOS 证伪结论"}
  ]
 },
 "observation": {
  "title": "一个「看起来有 30 个百分点优势」的信号，是怎么自己消失的",
  "what": "杀 3 尾（762 条公式集成投票选出覆盖最少的 3 个尾数）· 纯观测，从未用于任何投注",
  "baseline": 29.8,
  "window": "P292~P301（连续 10 期）",
  "series": [
   {"n":1,  "hits":0, "rate":0.0},
   {"n":2,  "hits":1, "rate":50.0},
   {"n":3,  "hits":2, "rate":66.7},
   {"n":4,  "hits":2, "rate":50.0},
   {"n":5,  "hits":3, "rate":60.0},
   {"n":6,  "hits":3, "rate":50.0},
   {"n":7,  "hits":3, "rate":42.9},
   {"n":8,  "hits":3, "rate":37.5},
   {"n":9,  "hits":3, "rate":33.3},
   {"n":10, "hits":3, "rate":30.0}
  ],
  "verdict": "第 3 期时命中率一度达到 66.7%，第 5 期仍有 60.0%——比随机基线高出 30.2 个百分点，足够做一张漂亮的海报。再观测 5 期，它自己掉回 30.0%，与基线 29.8% 只差 0.2 个百分点（z=0.01）。这里没有任何「后来失效」的变化，公式从第一期到第十期一个字没改，变的只有样本量。这就是为什么「连中 5 期」不构成证据：它不是被证伪的，是自己蒸发的。"
 },
 "cats":[
  {"cat":"杀肖公式(686)","n":5,"maxz":1.06},
  {"cat":"平肖信号","n":1,"maxz":0},
  {"cat":"生肖盲区","n":1,"maxz":0},
  {"cat":"开奖独立性","n":1,"maxz":0},
  {"cat":"数据一致性","n":2,"maxz":0}
 ],
 "rows":[
  {"cat":"杀肖公式(686)","formula":"686 条杀肖公式 · 总体死亡率","note":"OOS P30~P241 全量回放","hit":100,"base":null,"lift":null,"z":null,"verdict":"686/686 全死"},
  {"cat":"杀肖公式(686)","formula":"首次触发即死率","note":"619/686","hit":90.2,"base":null,"lift":null,"z":null,"verdict":"90.2% 首死"},
  {"cat":"杀肖公式(686)","formula":"观测漏杀率 vs 随机基线","note":"5528/5988 触发事件","hit":92.3,"base":91.6,"lift":1.008,"z":1.06,"verdict":"不显著 p=0.291"},
  {"cat":"杀肖公式(686)","formula":"分层 9 组 p 值范围","note":"波色91.6% / 尾数88.7% 最快/最慢","hit":null,"base":null,"lift":null,"z":null,"verdict":"全部 p>0.05"},
  {"cat":"杀肖公式(686)","formula":"Logistic 回归 OR(无条件)","note":"A1 n=5988","hit":null,"base":null,"lift":null,"z":null,"verdict":"OR=1.001 p=0.963"},
  {"cat":"平肖信号","formula":"平肖命中率 vs 随机基线","note":"主系统证伪","hit":null,"base":null,"lift":null,"z":null,"verdict":"p=0.765 永不下注"},
  {"cat":"生肖盲区","formula":"样本外生肖盲区补偿","note":"XGB+生肖补偿","hit":null,"base":null,"lift":null,"z":null,"verdict":"不成立 逼近随机"},
  {"cat":"开奖独立性","formula":"开奖 ≈ iid 随机","note":"EV≤0 越级外推已停","hit":null,"base":null,"lift":null,"z":null,"verdict":"无稳定 alpha"},
  {"cat":"数据一致性","formula":"生肖/五行错位修复(47期)","note":"农历/公历切换点","hit":null,"base":null,"lift":null,"z":null,"verdict":"修复后结论不变"},
  {"cat":"数据一致性","formula":"波色格式 + 头数修复","note":"72期格式 / 1期头数","hit":null,"base":null,"lift":null,"z":null,"verdict":"修复后结论不变"}
 ]
};
