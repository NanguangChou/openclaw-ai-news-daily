# 🤖 OpenClaw AI News Daily
<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>


<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>



<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
  <img src="https://img.shields.io/github/issues/NanguangChou/openclaw-ai-news-daily" alt="Issues">
  <img src="https://img.shields.io/github/license/NanguangChou/openclaw-ai-news-daily" alt="License">
  <img src="https://img.shields.io/badge/OpenClaw-Skill-blue" alt="OpenClaw Skill">
</p>

> 🦞 让你的 AI 助手每天早上为你播报 AI / OpenClaw 领域的最新资讯！

## ✨ 特性

- 📰 **多源聚合** - 自动获取 8+ 热门资讯源
- 🌐 **双语支持** - 中文/英文双语播报
- 🎯 **智能筛选** - 基于热度、相关性过滤优质内容
- 🔄 **定时任务** - 支持每日自动更新
- 📱 **多平台** - 支持 Telegram、Discord 等推送
- ⚡ **快速响应** - 异步获取，高效稳定

## 📊 支持的数据源

| 来源 | 更新频率 | 描述 |
|------|---------|------|
| 🟠 Hacker News | 实时 | 技术/AI 新闻 |
| 🐙 GitHub Trending | 每日 | 开源项目趋势 |
| 🐦 Twitter/X AI | 实时 | 行业动态讨论 |
| 📺 Reddit AI | 实时 | 社区热门话题 |
| 📰 36Kr | 实时 | 科技媒体资讯 |
| 💬 V2EX | 实时 | 程序员社区 |

## 🚀 快速开始

### 安装

```bash
# 方式一：使用 ClawHub CLI
px clawhub@latest install ai-news-daily

# 方式二：手动安装
git clone https://github.com/NanguangChou/openclaw-ai-news-daily.git
cp -r openclaw-ai-news-daily ~/.openclaw/skills/ai-news-daily
```

### 配置

在 `config.json` 中配置：

```json
{
  "sources": {
    "hackernews": {
      "enabled": true,
      "keywords": ["AI", "LLM", "OpenAI", "Claude", "OpenClaw"]
    },
    "github-trending": {
      "enabled": true,
      "language": "all"
    }
  },
  "language": "zh-CN",
  "max_items": 10,
  "schedule": "0 8 * * *"
}
```

## 📖 使用示例

```
用户: 今天有什么 AI 新闻？

AI: 📰 今日 AI 要闻 (2026-03-01)

🔥 OpenClaw 突破 200K Stars
   来源: GitHub Trending
   热度: 5000+ ⭐
   摘要: 开源 AI 助手 OpenClaw 成为历史上增长最快的项目...
   🔗 github.com/openclaw/openclaw

🔧 Claude Code 2.0 发布
   来源: Hacker News
   热度: 890 points
   摘要: Anthropic 发布 Claude Code 2.0，带来全新功能...
   🔗 news.ycombinator.com/item?id=...

📱 Apple AI 战略更新
   来源: Twitter/X
   热度: 520 likes
   摘要: 知名分析师曝光 iOS 18 AI 功能...
   🔗 twitter.com/...
```

## 📁 项目结构

```
openclaw-ai-news-daily/
├── SKILLClaw 技能.md              # Open定义
├── config.json           # 配置文件
├── news_fetcher.py       # 资讯获取核心代码
├── daily-review.sh       # 每日 review 脚本
├── examples/             # 使用示例
│   └── demo.png
└── README.md
```

## 🤝 贡献

欢迎提交 Issue 和 PR！

```bash
# 1. Fork 本项目
# 2. 创建特性分支
git checkout -b feature/your-feature

# 3. 提交更改
git commit -m "Add your feature"

# 4. 推送分支
git push origin feature/your-feature

# 5. 创建 Pull Request
```

## 📝 更新日志

### v1.0.0 (2026-03-01)
- 🎉 初始版本发布
- ✅ 支持 Hacker News 数据源
- ✅ 支持 GitHub Trending
- ✅ 中英文双语支持

## 📄 许可证

MIT License - 请随意使用！

---

<p align="center">
  ⭐ 如果这个项目对你有帮助，请点个 Star 支持一下！
</p>

<p align="center">
  🦞 Built with ❤️ for OpenClaw Community
</p>
