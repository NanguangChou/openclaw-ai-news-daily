#!/usr/bin/env python3
"""
OpenClaw 项目智能优化器
每小时自动分析并改进项目，提升 Star 数量
"""

import os
import json
import subprocess
import hashlib
from datetime import datetime

PROJECT_DIR = "/root/.openclaw/workspace/openclaw-ai-news-daily"
os.chdir(PROJECT_DIR)

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def get_github_stats():
    """获取 GitHub 统计数据"""
    code, out, err = run_cmd('curl -s "https://api.github.com/repos/NanguangChou/openclaw-ai-news-daily"')
    try:
        import json
        data = json.loads(out)
        return {
            "stars": data.get("stargazers_count", 0),
            "forks": data.get("forks_count", 0),
            "issues": data.get("open_issues_count", 0),
            "subscribers": data.get("subscribers_count", 0)
        }
    except:
        return {"stars": 0, "forks": 0, "issues": 0, "subscribers": 0}

def check_and_improve():
    """检查并改进项目"""
    improvements = []
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 1. 检查 README 完整性
    with open("README.md", "r") as f:
        readme = f.read()
    
    # 检查是否有徽章
    if "![" not in readme:
        improvements.append("添加 GitHub 徽章")
        # 添加徽章
        badge_section = '''<p align="center">
  <img src="https://img.shields.io/github/stars/NanguangChou/openclaw-ai-news-daily" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanguangChou/openclaw-ai-news-daily" alt="Forks">
</p>

'''
        if "# 🤖 OpenClaw AI News Daily" in readme:
            readme = readme.replace("# 🤖 OpenClaw AI News Daily", "# 🤖 OpenClaw AI News Daily\n" + badge_section)
            with open("README.md", "w") as f:
                f.write(readme)
    
    # 2. 检查是否支持更多数据源
    with open("config.json", "r") as f:
        config = json.load(f)
    
    sources = config.get("sources", {})
    if len(sources) < 5:
        improvements.append("增加更多数据源")
        # 添加更多数据源配置
        new_sources = {
            "twitter-ai": {
                "enabled": True,
                "keywords": ["AI", "LLM", "GPT", "OpenAI"]
            },
            "hackernews": {
                "enabled": True,
                "keywords": ["AI", "LLM", "OpenAI", "Claude", "OpenClaw", "machine learning"]
            }
        }
        config["sources"] = new_sources
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    # 3. 检查是否有更多功能
    with open("news_fetcher.py", "r") as f:
        code = f.read()
    
    if "telegram" not in code.lower() and "discord" not in code.lower():
        improvements.append("添加 Telegram/Discord 推送支持")
        # 添加推送功能
        push_code = '''

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

'''
        # 添加到文件末尾
        with open("news_fetcher.py", "a") as f:
            f.write(push_code)
    
    # 4. 添加更多代码示例
    if not os.path.exists("example.py"):
        improvements.append("添加使用示例文件")
        example_code = '''#!/usr/bin/env python3
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
'''
        with open("example.py", "w") as f:
            f.write(example_code)
    
    # 5. 检查是否有 requirements.txt
    if not os.path.exists("requirements.txt"):
        improvements.append("添加依赖文件")
        with open("requirements.txt", "w") as f:
            f.write("""httpx>=2.28.0
asyncio
""")
    
    return improvements

def main():
    print(f"=== 项目优化检查 - {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
    
    # 获取当前状态
    stats = get_github_stats()
    print(f"当前 Stars: {stats['stars']}")
    
    # 执行改进
    improvements = check_and_improve()
    
    if improvements:
        print(f"发现 {len(improvements)} 项改进:")
        for imp in improvements:
            print(f"  - {imp}")
        
        # 提交更改
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        run_cmd('git add .')
        code, out, err = run_cmd(f'git commit -m "优化: 改进项目 - {date}"')
        
        if code == 0:
            # 推送
            code, out, err = run_cmd('git push origin master')
            if code == 0:
                print("✅ 已推送改进")
            else:
                print(f"推送失败: {err}")
        else:
            print(f"提交失败: {err}")
    else:
        print("暂无改进")

if __name__ == "__main__":
    main()
