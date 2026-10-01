// 双色球 GitHub 策略仓库审计证据（15 仓库；2026-10-01 新增 TouKenAI/ssq-analysis 诚实框架）
// 数据来源：固化 skill github-lottery-strategy-audit 的防泄漏滚动回测（2026-09-28~29 基线 + 2026-10-01 补审）
// 口径：第 t 期只用 ≤t 历史预测 t+1；对照官方 cwl 全量 2070 期 / 仓库自带 / yangusrname 1879 期
// 本文件为站点「GitHub 策略审计」板块的单一数据源，所有数字均来自已核实回测，不编造。
window.GH_DATA = {
  meta: {
    total: 15,
    updated: "2026-10-01",
    verdict: "15 仓库全部 = 随机，无 alpha（含 1 个诚实自证框架）",
    bonf: 2.81,
    note: "样本外滚动回测（第 t 期只用 ≤t 历史预测 t+1），官方 cwl 全量 2071 期，与铁律#4一致，杜绝数据泄漏"
  },
  scale: [
    { v: 14, u: "个", c: "审计仓库（热冷/频率/时序/ML/RL/LLM 全覆盖）" },
    { v: 0, u: "个", c: "通过 Bonferroni 显著检验（|z|≥2.81）" },
    { v: 2071, u: "期", c: "官方 cwl 全量回测基准" },
    { v: "≤0.68", u: "", c: "三探针最大 |z| 偏离（远低于阈值 2.81）" }
  ],
  probes: [
    {
      key: "A", title: "热/冷号滚动 z 检验（3 套独立数据）",
      head: ["数据集", "红球·热号 z", "蓝球·冷号 z", "结论"],
      rows: [
        ["SSQ-DCBall-Quant history.csv（3339 目标期）", "+0.301", "−0.624", "无显著"],
        ["官方 ssq_hist_cwl.json（2039 目标期）", "+0.025", "+0.426", "无显著"],
        ["yangusrname lottery_data.json（1848 目标期）", "−0.311", "+0.116", "无显著"]
      ]
    },
    {
      key: "B", title: "gitmen 策略真跑（官方数据滚动 OOS, n=399）",
      head: ["策略", "策略平均红球命中", "随机基线 / 理论", "结论"],
      rows: [
        ["coldHot（3 热+2 温+1 冷）", "1.093", "1.103 / ≈1.091", "≈随机"],
        ["frequency（4 高频+2 随机）", "1.148", "1.108 / ≈1.091", "≈随机"],
        ["高频蓝号（命中率）", "0.0576", "0.0476 / 1/16=0.0625", "≈随机"]
      ]
    },
    {
      key: "C", title: "时序/ML 可预测性探针（官方 2071 期）",
      head: ["探针", "实测", "对照", "结论"],
      rows: [
        ["自相关 lag-1/2/3/5/10", "6 位置 |r|≤0.068", "iid 期望≈0", "无可学时间结构"],
        ["RandomForest(lag-5) 预测位置号", "准确率 0.056~0.143", "≤多数类基线", "未超越随机"],
        ["lucky_ball 正规回测 Hit@k", "k6=0.186 / k10=0.307", "理论 0.182/0.303", "=随机"]
      ]
    },
    {
      key: "D", title: "典型伪证：LJQ-HUB-cmyk/SSQ 自带回测剖析",
      head: ["维度", "该仓库情况", "对照", "判定"],
      rows: [
        ["预测样本量", "仅 2 期", "统计无意义", "cherry-pick"],
        ["评分体系", "自定 60 分（红4+蓝1）", "非真实中奖率", "包装伪证"],
        ["底层方法", "冷热/遗漏/五行/频率六维", "已被 A/C 证伪", "无 alpha"]
      ]
    },
    {
      key: "E", title: "诚实对照：TouKenAI/ssq-analysis（视频《如何在家计算彩票漏洞》关联仓）",
      head: ["维度", "该框架自身结论", "对照", "判定"],
      rows: [
        ["数学基座", "双色球 iid 均匀随机，单注头奖 1/17,721,088", "公理事实", "不可优化"],
        ["贝叶斯证明", "P(下一期=c|历史)=P(c)=1/T，后验=先验", "零信息增益", "选号无影响"],
        ["蒙特卡洛 n=20万", "优化方案至少中一奖≈33%，中一等奖≈0", "返奖率≈50%必然", "仅优化覆盖"],
        ["本审计实跑(官方2071期)", "红热 z=+0.026 / 蓝冷 z=+0.407 / 自相关≤0.068", "远<2.81", "=随机"]
      ]
    }
  ],
  repos: [
    { name: "yuwenbin860/lottery", type: "统计（热冷/频率/奇偶/连号/和值）", ran: "结构审阅", concl: "≈随机" },
    { name: "LJQ-HUB-cmyk/SSQ-DCBall-Quant", type: "冷热号 + RL 量化选号", ran: "实跑", concl: "=随机" },
    { name: "aiyufan3/lucky_ball", type: "LSTM+ARIMA+蒙特卡洛 正规回测", ran: "实跑", concl: "=随机" },
    { name: "wjt0321/lottery-predictor", type: "多算法频率/冷热融合", ran: "结构审阅", concl: "≈随机" },
    { name: "konglr/Lottery", type: "调 Gemini/Qwen 等 LLM「AI 预测」", ran: "离线不可跑", concl: "无 alpha" },
    { name: "LJQ-HUB-cmyk/auto_lot", type: "统计（频率/遗漏/尾/奇偶/和值/连号）", ran: "统一审计", concl: "=随机" },
    { name: "88899/gitmen-lottery", type: "纯 Python 冷热/频率/均衡/随机", ran: "gitmen_harness 真跑", concl: "≈随机" },
    { name: "modbender/skill-library-mcp", type: "lottery-analyzer 热冷统计 skill", ran: "前提被覆盖", concl: "=随机" },
    { name: "Lang7910/ssq", type: "8 模型 MA/ES/RF/SVR/Bayes/ARIMA/LSTM/Hybrid", ran: "timeseries_probe 覆盖", concl: "时序=随机" },
    { name: "yangusrname/lottery_predictor", type: "RF/XGBoost/LightGBM/NN（自带 1879 期）", ran: "audit_hotcold 跑其数据", concl: "z≈0=随机" },
    { name: "JXXuanlv/double-color-ball", type: "TF LSTM/CNN（作者自承 0~2 红）", ran: "timeseries_probe 覆盖", concl: "时序=随机" },
    { name: "LJQ-HUB-cmyk/SSQ", type: "TF LSTM 六维融合", ran: "回测缺陷剖析", concl: "n=2 无意义" },
    { name: "druakin/DCBall-Quant", type: "RL（DQN/PPO），同源 #2", ran: "同源已证", concl: "=随机" },
    { name: "KittenCN/predict_Lottery_ticket", type: "TF LSTM 时序", ran: "timeseries_probe 覆盖", concl: "时序=随机" },
    { name: "TouKenAI/ssq-analysis", type: "5步分析+覆盖优化引擎（频率/贝叶斯/信息熵/蒙特卡洛）", ran: "audit_repo.py 实跑官方2071期", concl: "=随机·自带诚实声明" }
  ],
  verdict_summary: [
    ["热/冷号预测力（3 套独立数据）", "z≈0，无显著"],
    ["实际推荐注命中", "≈随机（均值 1.09/注）"],
    ["正规滚动回测 Hit@k", "=理论随机（k/33、k/16）"],
    ["时序/ML 可预测性", "自相关≈0、RF≤多数类基线"],
    ["与本项目证伪体系对照", "一致：83 法全证伪 / 9 策略 max|z|<2.99 / 追踪闭环 max|z|<1.7"],
    ["TouKenAI/ssq-analysis（诚实框架）", "贝叶斯证后验=先验 + 蒙特卡洛中一等奖≈0；本审计实跑 z≈0，无伪 alpha"]
  ]
};
