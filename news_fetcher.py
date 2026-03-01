#!/usr/bin/env python3
"""
OpenClaw AI News Daily - 每日 AI 资讯获取
支持多数据源、异步获取、缓存优化
"""

import json
import asyncio
import httpx
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib

@dataclass
class NewsItem:
    """新闻条目"""
    title: str
    url: str
    source: str
    score: int
    description: str = ""
    timestamp: str = ""
    
    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "score": self.score,
            "description": self.description,
            "timestamp": self.timestamp
        }

class AINewsFetcher:
    """AI 资讯获取器"""
    
    def __init__(self, config_path: str = "config.json"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.news_cache: List[NewsItem] = []
        self.cache_time: Optional[datetime] = None
    
    async def fetch_hackernews(self) -> List[NewsItem]:
        """获取 Hacker News AI 相关内容"""
        keywords = self.config.get("sources", {}).get("hackernews", {}).get("keywords", 
            ["AI", "LLM", "OpenAI", "Claude", "OpenClaw", "machine learning"])
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                # 获取 Top Stories
                response = await client.get(
                    "https://hacker-news.firebaseio.com/v0/topstories.json"
                )
                story_ids = response.json()[:50]
                
                stories = []
                tasks = [
                    client.get(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
                    for sid in story_ids[:20]
                ]
                
                responses = await asyncio.gather(*tasks, return_exceptions=True)
                
                for resp in responses:
                    if isinstance(resp, httpx.Response):
                        story = resp.json()
                        if story and self._is_ai_related(story.get("title", ""), keywords):
                            stories.append(NewsItem(
                                title=story.get("title", ""),
                                url=story.get("url", f"https://news.ycombinator.com/item?id={story.get('id')}"),
                                source="Hacker News",
                                score=story.get("score", 0),
                                timestamp=datetime.fromtimestamp(story.get("time", 0)).strftime("%Y-%m-%d %H:%M") if story.get("time") else ""
                            ))
                
                return stories[:5]
            except Exception as e:
                print(f"获取 Hacker News 失败: {e}")
                return []
    
    async def fetch_github_trending(self) -> List[NewsItem]:
        """获取 GitHub Trending AI 项目"""
        async with httpx.AsyncClient(timeout=15.0) as client:
            try:
                # 搜索 AI 相关的高星项目
                response = await client.get(
                    "https://api.github.com/search/repositories",
                    params={
                        "q": "AI OR LLM OR machine-learning OR gpt",
                        "sort": "stars",
                        "order": "desc",
                        "per_page": 10
                    },
                    headers={"Accept": "application/vnd.github.v3+json"}
                )
                
                data = response.json()
                repos = []
                
                for item in data.get("items", [])[:5]:
                    # 过滤 AI 相关项目
                    desc = item.get("description", "").lower()
                    name = item.get("name", "").lower()
                    if any(kw in desc or kw in name for kw in ["ai", "llm", "gpt", "chatbot", "model"]):
                        repos.append(NewsItem(
                            title=item.get("name", ""),
                            url=item.get("html_url", ""),
                            source="GitHub Trending",
                            score=item.get("stargazers_count", 0),
                            description=item.get("description", "")[:100]
                        ))
                
                return repos
            except Exception as e:
                print(f"获取 GitHub 失败: {e}")
                return []
    
    async def fetch_reddit_ai(self) -> List[NewsItem]:
        """获取 Reddit AI 热门讨论"""
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.get(
                    "https://www.reddit.com/r/ArtificialIntelligence/hot.json",
                    params={"limit": 15},
                    headers={"User-Agent": "OpenClaw-News/1.0"}
                )
                
                data = response.json()
                posts = []
                
                for post in data.get("data", {}).get("children", [])[:5]:
                    post_data = post.get("data", {})
                    posts.append(NewsItem(
                        title=post_data.get("title", ""),
                        url=f"https://reddit.com{post_data.get('permalink', '')}",
                        source="Reddit AI",
                        score=post_data.get("score", 0),
                        description=post_data.get("selftext", "")[:100]
                    ))
                
                return posts
            except Exception as e:
                print(f"获取 Reddit 失败: {e}")
                return []
    
    def _is_ai_related(self, title: str, keywords: List[str]) -> bool:
        """检查标题是否与 AI 相关"""
        title_lower = title.lower()
        return any(kw.lower() in title_lower for kw in keywords)
    
    async def fetch_all(self) -> List[NewsItem]:
        """获取所有来源的新闻"""
        all_news = []
        
        # 并发获取所有数据源
        tasks = []
        
        if self.config.get("sources", {}).get("hackernews", {}).get("enabled", True):
            tasks.append(self.fetch_hackernews())
        
        if self.config.get("sources", {}).get("github-trending", {}).get("enabled", True):
            tasks.append(self.fetch_github_trending())
        
        if self.config.get("sources", {}).get("reddit-ai", {}).get("enabled", True):
            tasks.append(self.fetch_reddit_ai())
        
        # 并发执行
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, list):
                all_news.extend(result)
        
        # 按热度排序
        all_news.sort(key=lambda x: x.score, reverse=True)
        
        # 更新缓存
        self.news_cache = all_news
        self.cache_time = datetime.now()
        
        return all_news[:self.config.get("max_items", 10)]
    
    def format_news(self, news: List[NewsItem], format_type: str = "default") -> str:
        """格式化新闻为可读文本"""
        if not news:
            return "📭 今日暂无 AI 资讯"
        
        date = datetime.now().strftime("%Y-%m-%d")
        
        if format_type == "simple":
            # 简洁模式
            output = [f"📰 AI 要闻 ({date})\n"]
            for i, item in enumerate(news[:5], 1):
                output.append(f"{i}. {item.title[:50]}")
                output.append(f"   🔗 {item.url}\n")
            return "\n".join(output)
        
        # 默认详细模式
        output = [f"📰 今日 AI 要闻 ({date})\n"]
        
        for i, item in enumerate(news, 1):
            # 根据来源选择图标
            icon = {
                "Hacker News": "🟠",
                "GitHub Trending": "🐙",
                "Reddit AI": "📺",
                "Twitter/X": "🐦"
            }.get(item.source, "📌")
            
            output.append(f"{i}. {icon} **{item.title}**")
            output.append(f"   📊 热度: {item.score} | 📍 {item.source}")
            
            if item.description:
                output.append(f"   📝 {item.description[:60]}...")
            
            output.append(f"   🔗 [查看原文]({item.url})\n")
        
        output.append("\n💡 资讯来源: Hacker News, GitHub, Reddit AI")
        
        return "\n".join(output)
    
    def get_cache_hash(self) -> str:
        """获取缓存哈希"""
        if not self.news_cache:
            return ""
        content = json.dumps([n.to_dict() for n in self.news_cache])
        return hashlib.md5(content.encode()).hexdigest()


async def main():
    """测试运行"""
    fetcher = AINewsFetcher()
    
    print("🔄 正在获取 AI 资讯...")
    news = await fetcher.fetch_all()
    
    print(f"✅ 获取到 {len(news)} 条资讯\n")
    print(fetcher.format_news(news))
    
    # 输出 JSON 格式（供其他程序使用）
    print("\n--- JSON 输出 ---")
    print(json.dumps({
        "date": datetime.now().isoformat(),
        "count": len(news),
        "news": [n.to_dict() for n in news]
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())


# ============ 推送功能 ============
class PushNotifier:
    """推送通知器"""
    
    def __init__(self, config: dict):
        self.config = config
    
    async def send_telegram(self, message: str, token: str = None, chat_id: str = None):
        """发送到 Telegram"""
        if not token:
            token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not chat_id:
            chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
        if not token or not chat_id:
            return False
        
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        async with httpx.AsyncClient() as client:
            await client.post(url, json=data)
        return True
    
    async def notify(self, news: list):
        """发送通知"""
        message = self.format_message(news)
        await self.send_telegram(message)

