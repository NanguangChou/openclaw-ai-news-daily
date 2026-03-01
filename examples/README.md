# 📸 使用示例

## 🎯 功能演示

### 1. 播报效果示例

```
用户: 今天有什么 AI 新闻？

AI: 📰 今日 AI 要闻 (2026-03-01)

1. 🟠 OpenClaw 突破 200K Stars
   📊 热度: 5200 | 📍 GitHub Trending
   📝 开源 AI 助手 OpenClaw 成为历史上增长最快的项目...
   🔗 [查看原文](https://github.com/openclaw/openclaw)

2. 🟠 Claude Code 2.0 发布
   📊 热度: 890 | 📍 Hacker News
   📝 Anthropic 发布 Claude Code 2.0，带来全新功能...
   🔗 [查看原文](https://news.ycombinator.com/item?id=...)

3. 📺 Apple AI 战略更新
   📊 热度: 650 | 📍 Reddit AI
   📝 知名分析师曝光 iOS 18 AI 功能...
   🔗 [查看原文](https://reddit.com/r/ArtificialIntelligence/...)

💡 资讯来源: Hacker News, GitHub, Reddit AI
```

### 2. 配置文件示例

```json
{
  "sources": {
    "hackernews": {
      "enabled": true,
      "keywords": ["AI", "LLM", "OpenAI", "Claude"]
    },
    "github-trending": {
      "enabled": true,
      "language": "python"
    },
    "reddit-ai": {
      "enabled": true,
      "subreddits": ["ArtificialIntelligence"]
    }
  },
  "language": "zh-CN",
  "max_items": 10
}
```

### 3. 命令行使用

```bash
# 获取资讯
python news_fetcher.py

# 输出示例:
# 🔄 正在获取 AI 资讯...
# ✅ 获取到 10 条资讯
#
# 📰 今日 AI 要闻 (2026-03-01)
#
# 1. 🟠 OpenClaw 突破 200K Stars
#    📊 热度: 5200 | 📍 GitHub Trending
#    ...
```

### 4. 输出格式

支持多种输出格式：

- **默认**: 带 Emoji 的 Markdown 格式
- **简洁**: 纯文本列表
- **JSON**: 供程序调用的结构化数据

```bash
# JSON 输出
python news_fetcher.py --json
```

---

💡 想添加更多示例？请提交 PR！
