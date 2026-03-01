#!/usr/bin/env python3
"""
OpenClaw AI News Daily - 使用示例
"""
import asyncio
from news_fetcher import AINewsFetcher

async def main():
    # 创建获取器
    fetcher = AINewsFetcher("config.json")
    
    # 获取新闻
    news = await fetcher.fetch_all()
    
    # 打印格式化结果
    print(fetcher.format_news(news))
    
    # 推送到 Telegram
    # notifier = PushNotifier(config)
    # await notifier.notify(news)

if __name__ == "__main__":
    asyncio.run(main())
