# 上传到 Cloudflare Pages · 傻瓜步骤

你的网站文件已经做好了，是一个**纯静态站点**（不需要任何后端、不需要编译），一共 3 个文件：

```
refute-site/
├── index.html      ← 主页面（导航/KPI/双色球可检索表格/3D/六合/答疑/免责）
├── style.css       ← 排版样式（浅色主题，手机电脑都能看）
└── data/
    └── ssq.js      ← 双色球 213 条证伪数据（已内嵌，无跨域问题）
```

> 本地预览已通过运行时校验：213 条全部渲染、24 个分类条形、4 个 KPI 全部正常。

---

## 方式一：Dashboard 拖拽上传（最简单，推荐先用这个）

不需要装任何软件、不需要命令行。

1. 打开你已注册的 **https://dash.cloudflare.com/**
2. 左侧菜单点 **Workers 和 Pages**（或 `Workers & Pages`）
3. 右上角点 **创建**（Create）→ 选 **Pages**
4. 选择 **上传资产**（Upload assets / Direct Upload，不是连 Git 那个）
5. 把整个 `refute-site` 文件夹拖进去（或点「上传文件夹」选 `refute-site`）
6. 项目名称随便起，建议：`lottery-refute`
   - 它会自动生成公网地址：`https://lottery-refute.pages.dev`
7. 点 **部署**（Deploy）

等十几秒，页面显示「成功」，给你的 `xxx.pages.dev` 链接就是**全网可访问**的网站了。🌊

---

## 方式二：Wrangler 命令行（以后改内容更新用，可选）

适合你以后经常改数据、想一键重新发布时。

```bash
# 第一次：装 wrangler 并登录
npm install -g wrangler
wrangler login          # 会弹浏览器授权

# 发布（在 refute-site 目录外执行，路径指到文件夹）
wrangler pages deploy refute-site
```

每次更新了数据或文案，重新跑一次 `wrangler pages deploy refute-site` 即可，旧版本会自动保留可回滚。

---

## 以后怎么更新内容

- **改文字/排版**：直接编辑 `index.html` 或 `style.css`，然后重新上传（方式一重选文件夹 / 方式二重跑命令）。
- **改双色球数据**：编辑 `data/ssq.js`（由 `SSQ/ssq_refutation_index.json` 生成，别手改原始结构），重新上传。
- Cloudflare Pages 每次部署都会保留历史版本，可随时回滚。

---

## 自定义域名（可选，以后再说）

- 想要 `你的名字.com` 这种独立域名：在 Cloudflare 里点 **Registrar** 用成本价注册（约 ¥60~80/年），再到 Pages 项目 **设置 → 自定义域** 绑定即可。
- 不买域名也完全没问题，`xxx.pages.dev` 是**免费且永久有效**的公网地址。

---

## ⚠️ 上线前须知（如实标注）

- **双色球板块**：213 条证伪数据是真实的（官方 cwl 全量 2059 期回测）。
- **福彩3D / 六合彩板块**：目前页面里是「接入中」占位——原始证伪索引在另一套分析系统，尚未同步到本站。等真实数据接入后，替换 `data/` 下对应 js 文件再重新部署，**绝不编造数字**。
- 站点所有内容仅做历史数据回测与统计科普，不含任何投注建议，符合反误导/理性购彩定位。

---

## 文件归档位置（已同步）

- 项目目录：`C:\Users\binliu8199\WorkBuddy\2026-07-18-10-48-51\refute-site\`
- 桌面归档：`C:\Users\binliu8199\Desktop\refute-site\`
- OneDrive 刘斌：`C:\Users\binliu8199\OneDrive\图片\文档\刘斌\refute-site\`
