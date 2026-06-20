# Chat2KB

> **Ask Your Database Anything**  
> 对话式数据库智能平台 — 连接 KubeBlocks 全系产品，用自然语言释放数据价值。

## 项目简介

Chat2KB 是一个面向 KubeBlocks 生态的对话式智能入口，提供：

- **知识库问答助手**：自然语言查询产品文档、最佳实践、故障排查、API 速查等。
- **Demo 环境运营洞察**：对接 dev、apecloud.cn、kubeblocks.io 三个环境，分析客户行为、资源利用率、高意向线索等。

本项目包含：

- `index.html`：Landing Page（响应式、动效、环境矩阵、场景用例）。
- `chat.html`：对话界面（支持环境切换、建议问题快捷输入）。
- `functions/api/chat.js`：Cloudflare Pages Function 后端，负责调用 Kimi 大模型与 dev admin API。
- `changelog.html`：更新日志。

## 在线预览

- GitHub Repo: https://github.com/ruijun2002/chat2kb
- GitHub Pages: https://ruijun2002.github.io/chat2kb

## 本地运行

### 前端静态预览

```bash
cd /Users/wangruijun/workspace/chat2kb
python3 -m http.server 8080
# 访问 http://localhost:8080
```

此时 `chat.html` 会优先调用 `/api/chat`；如果后端不可用，会自动降级为本地模拟回复。

### 完整功能预览（含后端）

需要安装 [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/)：

```bash
cd /Users/wangruijun/workspace/chat2kb

# 确认 .dev.vars 中已配置密钥
wrangler pages dev .
# 访问 http://localhost:8788
```

`.dev.vars` 中默认已包含 Kimi API Key 与 dev admin API Key（dev admin API Base URL 为占位符，需替换为真实地址）。

## 项目结构

```
chat2kb/
├── index.html              # 落地页
├── chat.html               # 对话页
├── changelog.html          # 更新日志
├── functions/
│   └── api/
│       └── chat.js         # Cloudflare Pages Function 后端
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
- 响应式布局

## 技术栈

- HTML5
- CSS3（变量、Flex/Grid、动画、响应式）
- 原生 JavaScript（Canvas 粒子、IntersectionObserver、URLSearchParams）
- Cloudflare Pages Functions（后端）
- Kimi (Moonshot) API（大模型）
- Google Fonts（Inter / JetBrains Mono）

## 说明

## 后端配置

本地开发通过 `.dev.vars` 配置，生产环境通过 Cloudflare Dashboard 或 `wrangler pages secret` 设置：

| 变量名 | 说明 |
|--------|------|
| `KIMI_API_KEY` | Kimi (Moonshot) API Key |
| `ADMIN_DEV_API_BASE` | dev 开发环境 admin API 根地址 |
| `ADMIN_DEV_API_KEY` | dev 开发环境 admin API Key |

### dev admin API 接入说明

`functions/api/chat.js` 已默认在 `userEnv === 'dev'` 时尝试调用：

```
GET ${ADMIN_DEV_API_BASE}/api/v1/clusters
Authorization: Bearer ${ADMIN_DEV_API_KEY}
```

如果实际接口路径或认证方式不同，请修改 `functions/api/chat.js` 中的请求逻辑。

## 部署到 Cloudflare Pages

```bash
wrangler pages deploy .
```

部署前请确保已在 Cloudflare Dashboard 中设置 `KIMI_API_KEY`、`ADMIN_DEV_API_BASE`、`ADMIN_DEV_API_KEY`。

## License

MIT © 2026 ApeCloud. Powered by KubeBlocks.
