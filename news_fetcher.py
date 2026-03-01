#!/usr/bin/env python3
"""
AI News Daily - 每日 AI 资讯获取
"""

import json
import httpx
from datetime import datetime
from typing import List, Dict

class AINewsFetcher:
    def __init__(self, config: dict):
        self.config = config
        self.news = []
    
    async def fetch_hackernews(self) -> List[Dict]:
        """获取 Hacker News AI 相关内容"""
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            story_ids = response.json()[:50]
            
            stories = []
            for story_id in story_ids[:20]:
                story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                story = await client.get(story_url)
                story_data = story.json()
                
                if story_data and self._is_ai_related(story_data.get("title", "")):
                    stories.append({
                        "title": story_data.get("title"),
                        "url": story_data.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                        "score": story_data.get("score", 0),
                        "source": "Hacker News"
                    })
            
            return stories[:5]
    
    def _is_ai_related(self, title: str) -> bool:
        keywords = self.config.get("sources", {}).get("hackernews", {}).get("keywords", [])
        title_lower = title.lower()
        return any(kw.lower() in title_lower for kw in keywords)
    
    async def fetch_github_trending(self) -> List[Dict]:
        """获取 GitHub Trending AI 项目"""
        url = "https://api.github.com/search/repositories"
        params = {
            "q": "AI OR llm OR machine-learning created:>2026-01-01",
            "sort": "stars",
            "order": "desc",
            "per_page": 10
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            data = response.json()
            
            repos = []
            for item in data.get("items", [])[:5]:
                repos.append({
                    "title": item.get("name"),
                    "description": item.get("description", ""),
                    "url": item.get("html_url"),
                    "stars": item.get("stargazers_count", 0),
                    "source": "GitHub Trending"
                })
            
            return repos
    
    async def fetch_all(self) -> List[Dict]:
        """获取所有来源的新闻"""
        all_news = []
        
        if self.config.get("sources", {}).get("hackernews", {}).get("enabled", True):
            try:
                hn_news = await self.fetch_hackernews()
                all_news.extend(hn_news)
            except Exception as e:
                print(f"Error fetching Hacker News: {e}")
        
        if self.config.get("sources", {}).get("github-trending", {}).get("enabled", True):
            try:
                gh_news = await self.fetch_github_trending()
                all_news.extend(gh_news)
            except Exception as e:
                print(f"Error fetching GitHub: {e}")
        
        # 按热度排序
        all_news.sort(key=lambda x: x.get("score", x.get("stars", 0)), reverse=True)
        
        return all_news[:self.config.get("max_items", 10)]
    
    def format_news(self, news: List[Dict]) -> str:
        """格式化新闻为可读文本"""
        if not news:
            return "今日暂无 AI 资讯 📭"
        
        date = datetime.now().strftime("%Y-%m-%d")
        output = [f"📰 今日 AI 要闻 ({date})\n"]
        
        for i, item in enumerate(news, 1):
            title = item.get("title", "无标题")
            source = item.get("source", "Unknown")
            score = item.get("score", item.get("stars", 0))
            url = item.get("url", "")
            desc = item.get("description", "")
            
            output.append(f"{i}. 🔥 {title}")
            output.append(f"   来源: {source} | 热度: {score}")
            if desc:
                output.append(f"   📝 {desc[:80]}...")
            output.append(f"   🔗 {url}\n")
        
        return "\n".join(output)


async def main():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    fetcher = AINewsFetcher(config)
    news = await fetcher.fetch_all()
    print(fetcher.format_news(news))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
