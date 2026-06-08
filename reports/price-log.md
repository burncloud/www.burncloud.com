# BurnCloud 价格更新日志

---

## 2026-06-08 09:01

**状态**: ✓ 执行成功

**结果**: 无价格变动

**说明**: 
- 脚本 `price_update.py` 正常执行
- `fetch_official_prices()` 函数目前返回空字典（TODO状态）
- 当前模型数据最后更新时间: 2026-06-07
- 共监控 18 个模型

**下次执行**: 2026-06-09 09:00

---

## 数据源说明

当前价格数据来自 `/data/models.json`，包含以下模型：

### Frontier Models (前沿模型)
- GPT-5.5, GPT-5.4 (OpenAI)
- Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 (Anthropic)
- Gemini 3.1 Pro, Gemini 3.5 Flash (Google)
- Grok 4.1 (xAI)

### Chinese Models (中国模型)
- DeepSeek V4 Pro, V4 Flash, V3.2, R1
- Kimi K2.6 (Moonshot)
- Qwen 3.5 (Alibaba)
- GLM-5.1 (Zhipu)
- Step 3.5 Flash (StepFun)
- Doubao Pro (ByteDance)
- MiniMax

---

## 待办事项

需要实现真实的价格抓取逻辑：
1. DeepSeek 官方 API 定价页面
2. Anthropic 官方定价页面
3. OpenAI 官方定价页面
4. Google AI 定价页面
5. 其他中国模型供应商定价页面

**注意**: 需要人工确认后才能实现真实抓取逻辑
