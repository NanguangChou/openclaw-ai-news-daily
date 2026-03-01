# 🤝 贡献指南

感谢你对 OpenClaw AI News Daily 项目的兴趣！我们欢迎任何形式的贡献。

## 📋 贡献方式

### 🐛 报告问题

如果你发现任何 bug 或有新功能建议：

1. 搜索现有 [Issues](https://github.com/NanguangChou/openclaw-ai-news-daily/issues) 是否已存在
2. 如果没有，创建新的 Issue 并提供：
   - 清晰的标题和描述
   - 复现步骤
   - 环境信息

### 💡 提出功能建议

1. 使用 [Feature Request](https://github.com/NanguangChou/openclaw-ai-news-daily/issues/new?labels=enhancement) 模板
2. 描述你想要的功能
3. 解释为什么这会有用

### 🔧 提交代码

#### 步骤

1. **Fork** 本仓库
2. **克隆** 你的 Fork：
   ```bash
   git clone https://github.com/YOUR_USERNAME/openclaw-ai-news-daily.git
   ```

3. **创建** 分支：
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/bug-description
   ```

4. **开发** 你的功能：
   - 遵循现有代码风格
   - 添加注释
   - 确保代码可运行

5. **测试** 你的更改：
   ```bash
   python news_fetcher.py
   ```

6. **提交** 更改：
   ```bash
   git add .
   git commit -m "Add: 你的功能描述"
   ```

7. **推送** 到你的 Fork：
   ```bash
   git push origin feature/your-feature-name
   ```

8. **创建 Pull Request**

## 📝 提交规范

### 提交信息格式

```
<类型>: <简短描述>

[可选的详细描述]

[可选的关联 Issue]
```

**类型：**
- `Add`: 添加新功能
- `Fix`: 修复 bug
- `Update`: 更新现有功能
- `Refactor`: 代码重构
- `Docs`: 文档更新
- `Chore`: 维护性更改

**示例：**
```
Add: 添加 Reddit AI 数据源

- 支持获取 Reddit r/ArtificialIntelligence 热门帖子
- 添加异步获取优化

Closes #12
```

## 🎯 需要帮助？

- 📚 查看 [Wiki](https://github.com/NanguangChou/openclaw-ai-news-daily/wiki)
- 💬 加入 [Discord](https://discord.gg/openclaw) (如果有)
- 📧 邮箱联系: jack@openclaw.ai

## 📜 行为准则

请保持友好和包容。我们希望建立一个 welcoming 的社区。

---

⭐ 感谢你的贡献！
