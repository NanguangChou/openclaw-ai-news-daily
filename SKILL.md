---
name: ai-news-daily
description: 每日 AI / OpenClaw 资讯播报技能。自动收集并推送 AI 领域的最新资讯，让你的 AI 助手每天早上为你播报最新动态。
---

# 🤖 AI News Daily - 每日 AI 资讯播报

## 用途

自动收集并播报 AI、OpenClaw、技术领域的最新资讯。

## 触发方式

- 今天有什么 AI 新闻？
- 给我播报 AI 资讯
- 今日要闻
- /ai-news
- AI news

## 功能

### 1. 多源资讯聚合
- Hacker News AI 相关内容
- GitHub Trending AI 项目
- AI Twitter/Reddit 热门讨论
- 各大 AI 公司动态

### 2. 智能筛选
- 基于热度排序
- 去重和过滤低质量内容
- 提取关键信息

### 3. 播报格式
```
📰 今日 AI 要闻 (2026-03-01)

🔥 [标题]
   来源: Hacker News
   热度: 500+ points
   摘要: ...
   链接: ...

🔗 [链接2]
   ...
```

## 配置

首次使用会询问：
1. 关注的资讯来源
2. 播报语言（中文/英文）
3. 推送方式（仅展示/推送到指定平台）

## 示例对话

```
用户: 今天有啥 AI 新闻？

AI: 📰 今日 AI 要闻 (2026-03-01)

🔥 OpenClaw 突破 200K Stars
   来源: GitHub
   摘要: 开源 AI 助手 OpenClaw 成为历史上增长最快的项目...
   🔗 github.com/openclaw/openclaw

🔧 Claude Code 发布新版本
   来源: Hacker News
   摘要: Anthropic 发布 Claude Code 2.0，带来...
   🔗 news.ycombinator.com/item?id=...

📱 Apple AI 战略曝光
   来源: Twitter
   摘要: 知名分析师预测 iOS 18 将集成...
   🔗 twitter.com/...
```

## 注意事项

- 首次获取可能需要 10-30 秒
- 部分内容可能需要 VPN
- 资讯仅供学习参考
