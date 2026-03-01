#!/bin/bash
# OpenClaw 项目每日 Report 脚本
# 每天 12:00 执行并发送报告

PROJECT_DIR="/root/.openclaw/workspace/openclaw-ai-news-daily"
cd "$PROJECT_DIR" || exit 1

DATE=$(date "+%Y-%m-%d %H:%M")
LOG_FILE="$PROJECT_DIR/review.log"

echo "=== Daily Review - $DATE ===" >> "$LOG_FILE"

# 1. 获取 GitHub 统计数据
STATS=$(curl -s "https://api.github.com/repos/NanguangChou/openclaw-ai-news-daily" 2>/dev/null)
STARS=$(echo "$STATS" | python3 -c "import sys,json; print(json.load(sys.stdin).get('stargazers_count', 0))" 2>/dev/null || echo "0")
FORKS=$(echo "$STATS" | python3 -c "import sys,json; print(json.load(sys.stdin).get('forks_count', 0))" 2>/dev/null || echo "0")

# 2. 检查当日优化次数
OPTIMIZE_COUNT=$(grep -c "已优化并推送" "$LOG_FILE" 2>/dev/null || echo "0")

# 3. 读取最近日志
RECENT_LOG=$(tail -20 "$LOG_FILE" 2>/dev/null)

# 4. 生成报告
REPORT="📊 OpenClaw 项目 Daily Report

📅 日期: $DATE
📂 项目: openclaw-ai-news-daily
🔗 https://github.com/NanguangChou/openclaw-ai-news-daily

📈 GitHub 统计:
⭐ Stars: $STARS
🍴 Forks: $FORKS

🔄 今日优化:
⚡ 自动优化次数: $OPTIMIZE_COUNT

📝 最近活动:
$RECENT_LOG

---

🦞 OpenClaw 自动优化 Bot"

echo "$REPORT"
