# 🤖 OpenClaw AI News Daily

每天自动收集并推送 AI / OpenClaw 领域的最新资讯，让你的 AI 助手每天早上为你播报。

## 📺 演示

![Demo](https://via.placeholder.com/800x400?text=AI+News+Daily+Demo)

## ✨ 特性

- 📰 **多源聚合** - 自动获取 Hacker News、GitHub Trending、AI Twitter 等热门资讯
- 🌐 **多语言支持** - 中文/英文双语播报
- 🎯 **智能筛选** - 基于热度、相关性过滤优质内容
- 📱 **多平台推送** - 支持 Telegram、Discord、邮件等推送方式
- 🔄 **每日自动更新** - 定时获取最新资讯

## 🚀 快速开始

### 安装

```bash
# 安装技能
px clawhub@latest install ai-news-daily

# 或手动安装
git clone https://github.com/YOUR_USERNAME/openclaw-ai-news-daily.git
cp -r openclaw-ai-news-daily ~/.openclaw/skills/ai-news-daily
```

### 配置

在 `~/.openclaw/skills/ai-news-daily/config.json` 中配置：

```json
{
  "sources": ["hackernews", "github-trending", "twitter-ai"],
  "language": "zh-CN",
  "push_targets": ["telegram"],
  "schedule": "0 8 * * *"
}
```

## 📊 数据源

| 来源 | 更新频率 | 内容类型 |
|------|---------|---------|
| Hacker News | 实时 | 技术/AI 新闻 |
| GitHub Trending | 每日 | 开源项目 |
| AI Twitter | 实时 | 行业动态 |
| Reddit AI | 实时 | 社区讨论 |

## 📝 使用示例

```
用户: 今天的 AI 新闻有哪些？
AI:  今日 AI 要闻 (2026-03-01):

1. 🔥 OpenClaw 获得 200k+ Stars
   OpenClaw 成为 GitHub 增长最快的 AI 助手项目...
   
2. 🐍 PyTorch 2.0 发布
   带来更好的性能和新功能...
   
3. 📱 iOS 18 AI 功能曝光
   Apple 正在测试新的 AI 助手...
```

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 许可证

MIT License

---

⭐ 如果这个项目对你有帮助，请点个 Star 支持一下！
