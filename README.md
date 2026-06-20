# Chat2KB

> **Ask Your Database Anything**  
> 对话式数据库智能平台 — 连接 KubeBlocks 全系产品，用自然语言释放数据价值。

## 项目简介

Chat2KB 是一个面向 KubeBlocks 生态的对话式智能入口，提供：

- **知识库问答助手**：自然语言查询产品文档、最佳实践、故障排查、API 速查等。
- **Demo 环境运营洞察**：对接 dev、apecloud.cn、kubeblocks.io 三个环境，分析客户行为、资源利用率、高意向线索等。

本项目包含：

- `index.html`：Landing Page（响应式、动效、环境矩阵、场景用例）。
- `chat.html`：对话界面（支持环境切换、建议问题快捷输入、设置入口）。
- `settings.html`：设置页面，可在浏览器中配置环境 API 与大模型 API Key。
- `server.py`：本地 Python 开发服务器，托管静态文件并处理 `/api/chat`。
- `functions/api/chat.js`：Cloudflare Pages Function 后端，负责调用 Kimi 大模型与 dev admin API。
- `changelog.html`：更新日志。

## 在线预览

- GitHub Repo: https://github.com/ruijun2002/chat2kb
- GitHub Pages: https://ruijun2002.github.io/chat2kb

## 本地运行

### 方式一：Python 本地服务器（推荐，含后端 API）

`server.py` 同时提供静态文件服务和 `POST /api/chat`，无需 Wrangler：

```bash
cd /Users/wangruijun/workspace/chat2kb
python3 server.py 8080
# 访问 http://localhost:8080/chat.html?env=dev
```

启动时会自动创建 SQLite 数据库 `chat2kb.db`，并默认写入 `.dev.vars` 中的 dev 环境信息以及 `kimi-k2.6` 大模型配置。也可以在 `chat.html` 右上角进入「设置」页面进行修改：

- 环境 Admin API Base URL / Access Key / Secret Key
- 大模型模型（如 `kimi-k2.6`）/ API ID / API Key

设置保存在服务端 SQLite 中，刷新页面或重启浏览器后仍然有效；留空则回退到 `.dev.vars` 的默认值。`chat2kb.db` 已加入 `.gitignore`，不会提交。

### 方式二：纯静态预览

```bash
cd /Users/wangruijun/workspace/chat2kb
python3 -m http.server 8080
# 访问 http://localhost:8080
```

此时 `chat.html` 会优先调用 `/api/chat`；由于纯静态服务器不支持 POST，后端不可用时自动降级为本地模拟回复。

### 方式三：Wrangler（Cloudflare Pages Functions）

需要安装 [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/)：

```bash
cd /Users/wangruijun/workspace/chat2kb

# 确认 .dev.vars 中已配置密钥
wrangler pages dev .
# 访问 http://localhost:8788
```

`.dev.vars` 中默认已包含 Kimi API Key 与 dev admin API Key。

## 项目结构

```
chat2kb/
├── index.html              # 落地页
├── chat.html               # 对话页
├── settings.html           # 设置页面
├── changelog.html          # 更新日志
├── server.py               # Python 本地开发服务器
├── functions/
│   └── api/
│       └── chat.js         # Cloudflare Pages Function 后端
├── lib/
│   └── md5.js              # 纯 JS MD5 实现（用于 Digest 认证）
├── wrangler.toml           # Wrangler / Pages 配置
├── .dev.vars               # 本地密钥（不提交到 git）
├── prd_chat2kb_landing.md  # 产品需求文档
├── README.md
└── .gitignore
```

## 核心功能

### Landing Page

- 动态粒子背景（Canvas 2D）
- 更新日志入口，链接至 `changelog.html`
- 固定导航栏滚动高斯模糊效果
- 双引擎功能卡片 + 中间数据流动线
- 三个 Demo 环境卡片（dev / apecloud.cn / kubeblocks.io）
- 角色 × 场景标签切换
- AI Native 技术亮点
- CTA + Footer

### Changelog Page

- 时间线式版本记录
- 与落地页一致的视觉风格与导航

### Chat Page

- 环境选择器（URL 参数 `?env=` 预填充）
- 用户 / AI 消息气泡
- 模拟运营数据卡片（高意向客户、资源利用率等）
- 模拟知识库回答（Redis/MySQL/备份/报错等）
- 建议问题快捷输入
- 右上角设置入口，跳转 `settings.html`
- 响应式布局

## 技术栈

- HTML5
- CSS3（变量、Flex/Grid、动画、响应式）
- 原生 JavaScript（Canvas 粒子、IntersectionObserver、URLSearchParams）
- Cloudflare Pages Functions（后端）
- Kimi (Moonshot) / DeepSeek API（大模型，OpenAI-compatible）
- Digest 认证调用 dev admin API
- Google Fonts（Inter / JetBrains Mono）

## 说明

## 后端配置

本地开发通过 `.dev.vars` 配置，生产环境通过 Cloudflare Dashboard 或 `wrangler pages secret` 设置：

| 变量名 | 说明 |
|--------|------|
| `KIMI_API_KEY` | Kimi (Moonshot) API Key |
| `ADMIN_DEV_API_BASE` | dev 开发环境 admin API 根地址，例如 `https://api-dev.apecloud.cn/admin/v1/` |
| `ADMIN_DEV_ACCESS_KEY` | dev admin API Key 的 `accessKey`（Digest 用户名） |
| `ADMIN_DEV_SECRET_KEY` | dev admin API Key 的 `secretKey`（Digest 密码） |

### dev admin API 接入说明

根据官方文档，dev admin API 使用 **Digest 认证**，格式为：

```bash
curl --digest -u "accessKey:secretKey" https://api-dev.apecloud.cn/admin/v1/organizations
```

`functions/api/chat.js` 会在 `userEnv === 'dev'` 时：

1. 根据用户问题智能选择相关 endpoint（默认拉取 `/organizations`、`/clusters`，并按关键词匹配 `/environments`、`/users`、`/tasks`、`/events`、`/bills` 等）。
2. 使用 `ADMIN_DEV_ACCESS_KEY` / `ADMIN_DEV_SECRET_KEY` 并行请求这些 endpoint。
3. 将返回的实时数据注入 Kimi system prompt，由 Kimi 生成回答。

如果 endpoint 路径或返回结构与预期不同，请修改 `functions/api/chat.js` 中的 `ADMIN_ENDPOINTS` 映射。

## 部署到 Cloudflare Pages

```bash
wrangler pages deploy .
```

部署前请确保已在 Cloudflare Dashboard 中设置 `KIMI_API_KEY`、`ADMIN_DEV_API_BASE`、`ADMIN_DEV_ACCESS_KEY`、`ADMIN_DEV_SECRET_KEY`。

## License

MIT © 2026 ApeCloud. Powered by KubeBlocks.
