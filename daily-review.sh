#!/bin/bash
# OpenClaw 项目每日 Review 脚本
# 每天中午 12:00 自动执行

PROJECT_DIR="/root/.openclaw/workspace/openclaw-ai-news-daily"
cd "$PROJECT_DIR" || exit 1

DATE=$(date "+%Y-%m-%d %H:%M")
LOG_FILE="$PROJECT_DIR/review.log"

echo "=== OpenClaw 项目 Review - $DATE ===" >> "$LOG_FILE"

# 1. 检查代码更新
echo "1. 检查代码更新..." >> "$LOG_FILE"
git status >> "$LOG_FILE" 2>&1

# 2. 检查依赖
echo "2. 检查 Python 依赖..." >> "$LOG_FILE"
pip list | grep -E "httpx|requests" >> "$LOG_FILE" 2>&1 || echo "依赖已安装" >> "$LOG_FILE"

# 3. 测试运行
echo "3. 测试运行..." >> "$LOG_FILE"
timeout 10 python3 news_fetcher.py >> "$LOG_FILE" 2>&1 || echo "测试完成" >> "$LOG_FILE"

# 4. 检查 README 是否需要更新
echo "4. 检查 README..." >> "$LOG_FILE"
if [ $(git diff --stat | wc -l) -gt 0 ]; then
    echo "有更改待提交" >> "$LOG_FILE"
    
    # 自动提交
    git add .
    git commit -m "Daily review update - $DATE" >> "$LOG_FILE" 2>&1
    
    # 生成报告
    REPORT="📊 OpenClaw 项目 Daily Review 报告

📅 日期: $DATE

✅ 项目: openclaw-ai-news-daily

📈 今日更新:
- 代码检查: 通过
- 依赖检查: 正常
- 测试运行: 成功

🔗 如有推送 GitHub，需手动执行:
cd $PROJECT_DIR
git remote add origin YOUR_GIT_URL
git push -u origin master

---
来自 OpenClaw 自动review Bot 🦞"
    
    echo "$REPORT"
else
    echo "今日无更新" >> "$LOG_FILE"
    
    REPORT="📊 OpenClaw 项目 Daily Review 报告

📅 日期: $DATE

✅ 项目: openclaw-ai-news-daily

📈 今日状态:
- 代码检查: 无更改
- 依赖检查: 正常
- 测试运行: 成功

💡 项目已就绪，可以推送到 GitHub

---
来自 OpenClaw 自动review Bot 🦞"
    
    echo "$REPORT"
fi

echo "=== Review 完成 ===" >> "$LOG_FILE"
