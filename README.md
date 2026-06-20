# Chat2KB

> **Ask Your Database Anything**  
> 对话式数据库智能平台 — 连接 KubeBlocks 全系产品，用自然语言释放数据价值。

## 项目简介

Chat2KB 是一个面向 KubeBlocks 生态的对话式智能入口，提供：

- **知识库问答助手**：自然语言查询产品文档、最佳实践、故障排查、API 速查等。
- **Demo 环境运营洞察**：对接 dev、apecloud.cn、kubeblocks.io 三个环境，分析客户行为、资源利用率、高意向线索等。

本项目为前端演示版本，包含：

- `index.html`：Landing Page（响应式、动效、环境矩阵、场景用例）。
- `chat.html`：对话界面（支持环境切换、模拟 AI 回复、建议问题）。

## 在线预览

- GitHub Repo: https://github.com/ruijun2002/chat2kb
- GitHub Pages: https://ruijun2002.github.io/chat2kb

## 本地运行

本项目为纯静态页面，无需构建工具。任选一种方式：

### 方式 1：直接打开

用浏览器打开 `index.html` 即可。

### 方式 2：本地 HTTP 服务器

```bash
# Python 3
python3 -m http.server 8080

# 或 Node.js
npx serve .
```

然后访问 http://localhost:8080。

## 项目结构

```
chat2kb/
├── index.html              # 落地页
├── chat.html               # 对话页
├── changelog.html          # 更新日志
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
- Google Fonts（Inter / JetBrains Mono）

## 说明

当前 `chat.html` 为演示模式，所有 AI 回复均为本地模拟数据，未连接真实后端。后续可接入大模型 API 与 KubeBlocks 数据接口替换 `generateResponse` 函数。

## License

MIT © 2026 ApeCloud. Powered by KubeBlocks.
