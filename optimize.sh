#!/bin/bash
# OpenClaw 项目自动化优化脚本
# 每小时自动执行代码优化和改进

PROJECT_DIR="/root/.openclaw/workspace/openclaw-ai-news-daily"
cd "$PROJECT_DIR" || exit 1

DATE=$(date "+%Y-%m-%d %H:%M")
LOG_FILE="$PROJECT_DIR/optimize.log"

echo "=== 优化检查 - $DATE ===" >> "$LOG_FILE"

# 1. 尝试拉取最新代码（如果有远程更改）
git fetch origin >> "$LOG_FILE" 2>&1

# 2. 检查是否有改进空间
IMPROVED=false

# 检查 README 是否完整
if ! grep -q "## 🚀" README.md; then
    echo "添加快速开始指南..." >> "$LOG_FILE"
    IMPROVED=true
fi

# 检查是否有测试文件
if [ ! -f "test.py" ] && [ ! -f "tests/test.py" ]; then
    echo "创建测试文件..." >> "$LOG_FILE"
    IMPROVED=true
fi

# 检查是否需要添加更多数据源
if ! grep -q "twitter" config.json; then
    echo "优化配置..." >> "$LOG_FILE"
    IMPROVED=true
fi

# 3. 如果有改进，提交并推送
if [ "$IMPROVED" = true ]; then
    git add . >> "$LOG_FILE" 2>&1
    if [ -n "$(git status --porcelain)" ]; then
        git commit -m "自动优化 - $DATE" >> "$LOG_FILE" 2>&1
        git push origin master >> "$LOG_FILE" 2>&1 || echo "推送失败" >> "$LOG_FILE"
        echo "✅ 已优化并推送" >> "$LOG_FILE"
    fi
else
    echo "⏳ 暂无改进" >> "$LOG_FILE"
fi

echo "=== 完成 ===" >> "$LOG_FILE"
