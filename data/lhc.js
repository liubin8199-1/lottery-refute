// 六合彩（澳门）证伪档案 —— 全部数字来自璇玑系统已核实 OOS 回测与《官方数据一致性核查报告》(2026-08-30 修复后重跑)，无编造
window.LHC_DATA = {
 "meta": {
  "total": 686,
  "window": "OOS P30~P241（212 期，2026 全量开奖）· 璇玑系统回放",
  "maxz": 1.06,
  "thresh": 3.11,
  "passing": 0,
  "updated": "2026-09-03",
  "reports": [
   {"title":"686 条杀肖公式 · 全部死亡","note":"OOS P30~P241 共 212 期，686/686 = 100%"},
   {"title":"首次触发即死率 90.2%","note":"619/686 首次触发即判定死亡，半衰期 T50=1"},
   {"title":"观测漏杀率 92.3% vs 随机基线 91.6%","note":"z=1.06, p=0.291，不显著"},
   {"title":"分层 9 组 p 值 0.365–0.836","note":"全部 >0.05，无分组优势"},
   {"title":"Logistic OR=1.001 (p=0.963)","note":"无条件模型 n=5988，与随机无差异"},
   {"title":"平肖 p=0.765 / 生肖盲区不成立 / 开奖≈iid","note":"主系统多项 OOS 证伪结论"}
  ]
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
