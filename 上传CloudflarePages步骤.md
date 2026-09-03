# 上传到 Cloudflare Pages · 步骤（当前站点结构版）

你的网站是一个**纯静态站点**（无后端、无编译步骤），已包含推广物料（hero / OG 图 / 抖音·小红书海报 / 二维码）与 SEO 三件套（robots.txt / sitemap.xml / JSON-LD）。本文件已更新到当前真实结构。

---

## 当前站点结构（refute-site/）

```
refute-site/
├── index.html            ← 主页面（导航 / KPI / 双色球·福彩3D·六合彩 可检索表格 / 答疑 / 免责 / 分享）
├── style.css             ← 排版样式（浅色主题，手机电脑自适应）
├── robots.txt            ← SEO：允许抓取 + 指向 sitemap
├── sitemap.xml           ← SEO：站点地图
├── wrangler.toml         ← Cloudflare Pages 配置（名称 lottery-refute，输出目录 .）
├── .cfignore             ← 上传时排除开发产物（构建脚本 / 校验脚本 / 文档）
├── data/                 ← 全部内嵌，无跨域问题
│   ├── ssq.js            ← 双色球 213 条证伪数据（官方全量 2059 期回测）
│   ├── fc3d.js           ← 福彩3D 27 条证伪数据
│   ├── lhc.js            ← 六合彩 686 条证伪数据
│   └── draws.js          ← 开奖号码检索底表
└── assets/               ← 13 个文件
    ├── hero.png          ← 首页金色天平横幅（1200×480）
    ├── og.png            ← OG 分享图（1200×630，微信/Discord/Twitter 大图卡）
    ├── poster.png        ← 通用竖版海报（1080×1350）
    ├── poster-douyin.png ← 抖音 9:16 竖版（1080×1920）
    ├── poster-xhs.png    ← 小红书 3:4 竖版（1080×1440）
    ├── qr.png / qr.svg   ← 站点二维码
    ├── qr-douyin.png     ← 抖音海报内嵌二维码
    ├── hero.svg / pipeline.svg / icon-ssq.svg / icon-3d.svg / icon-lhc.svg
    └── （构建脚本生成的其余图）
```

> 本地预览已通过 `node _verify.js` 完整校验：213 条 SSQ 回测、24 分类条形、4 个 KPI、秘籍粉碎机 15 条、幸存者偏差模拟器均正常。

---

## 方式一：Dashboard 拖拽上传（最简单，推荐先用这个）

不需要装任何软件、不需要命令行、不需要令牌。

1. 打开你已注册的 **https://dash.cloudflare.com/**
2. 左侧菜单点 **Workers 和 Pages**（Workers & Pages）
3. 右上角点 **创建**（Create）→ 选 **Pages**
4. 选择 **上传资产**（Upload assets / Direct Upload，不是连 Git 那个）
5. 把整个 `refute-site` 文件夹拖进去（或点「上传文件夹」选 `refute-site`）
   - `.cfignore` 会自动排除构建脚本/文档，只上传运行所需静态文件
6. 项目名称建议：`lottery-refute`
   - 自动生成公网地址：`https://lottery-refute.pages.dev`
7. 点 **部署**（Deploy）

等十几秒，页面显示「成功」，`xxx.pages.dev` 链接就是**全网可访问**的网站了。🌊
（国内访问通常比 github.io 更稳，且**免 ICP 备案**，因为服务器在境外。）

---

## 方式二：Wrangler 命令行（以后改内容一键更新用）

适合你经常改数据/文案、想一条命令重新发布时。

### 准备（一次性）
已在本机隔离环境装好 wrangler，并写好 `wrangler.toml`。首次需要**登录授权**（这步必须你本人做，沙箱无法代做浏览器 OAuth）：

```bash
# 方式 A：浏览器 OAuth 登录（会弹窗授权，用你的 Cloudflare 账号）
npx wrangler login

# 方式 B：用 API Token（无头/服务器环境，推荐）
# 在 Cloudflare → My Profile → API Tokens → Create Token
# 选 "Cloudflare Pages: Edit" 权限，得到 token 后：
export CLOUDFLARE_API_TOKEN="你的token"
```

### 发布（在 refute-site 目录执行）
```bash
# 首次创建项目并部署
npx wrangler pages project create lottery-refute --production-branch=main
npx wrangler pages deploy .
```
之后每次改完内容，重新跑 `npx wrangler pages deploy .` 即可，旧版本自动保留可回滚。

---

## 以后怎么更新内容

- **改文字/排版**：直接编辑 `index.html` 或 `style.css`，重新上传（方式一重选文件夹 / 方式二重跑命令）。
- **改彩票数据**：编辑 `data/*.js`（由 `SSQ/ssq_refutation_index.json` 等生成，别手改原始结构），重新部署。
- **改推广物料**：重跑 `build_*.py` 生成新图，重新部署。**绝不编造数字**。
- Cloudflare Pages 每次部署都保留历史版本，可随时回滚。

---

## 自定义域名（可选，以后再说）

- 想要 `你的名字.com`：在 Cloudflare **Registrar** 用成本价注册（约 ¥60~80/年），再到 Pages 项目 **设置 → 自定义域** 绑定。
- 不买域名也完全没问题，`xxx.pages.dev` 是**免费且永久有效**的公网地址。
- ⚠️ 若绑 `.cn` 域名，国内注册局要求先 ICP 备案才能解析；绑 `.com`/`.pages.dev` 则免备案（服务器仍在境外）。

---

## ⚠️ 上线前须知（如实标注）

- **双色球 / 福彩3D / 六合彩板块**：证伪数据均为真实（官方全量开奖回测）。
- 站点所有内容仅做历史数据回测与统计科普，**不含任何投注建议**，符合反误导 / 理性购彩定位。
- 继续保持「证伪 / 不荐号 / 不代购 / 显著免责声明」的口径，避免任何"预测 / 稳赚 / 包中 / 带单"表述。

---

## 文件归档位置

- 桌面归档：`C:\Users\binliu8199\Desktop\refute-site\`
- GitHub Pages（现用）：`https://liubin8199-1.github.io/lottery-refute/`
- Cloudflare Pages（待部署）：`https://lottery-refute.pages.dev`（部署后生效）
