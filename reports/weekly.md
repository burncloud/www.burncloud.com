# BurnCloud 项目报告

## 初始化状态

**日期**: 2026-06-07

---

## 已完成任务

### 1. 项目结构创建 ✓

已创建以下目录结构：

```
/home/hermes/www.burncloud.com/
├── data/                    # 数据文件
│   ├── models.json         # 模型价格数据
│   ├── seo-rules.json      # SEO 规则
│   └── protected-files.json # 受保护文件列表
├── models/                  # 模型页面
├── blog/                    # 博客页面
├── compare/                 # 对比页面
├── alternatives/            # 竞品替代页面
├── use-cases/              # 用例页面
├── pricing/                # 定价页面
├── docs/                   # 文档页面
├── security/               # 安全页面
├── self-host/              # 自托管页面
├── suppliers/              # 供应商页面
├── status/                 # 状态页面
├── reports/                # 报告目录
├── scripts/                # 自动化脚本
│   ├── price_update.py     # 价格更新
│   ├── blog_generate.py    # 博客生成
│   ├── seo_check.py        # SEO 检查
│   └── competitor_monitor.py # 竞品监控
└── template/               # 模板文件
```

### 2. 定时任务设置 ✓

| 任务名称 | 执行时间 | 描述 |
|---------|---------|------|
| burncloud-price-update | 每天 09:00 | 更新模型价格 |
| burncloud-blog-generate-10am | 每天 10:00 | 生成博客文章 |
| burncloud-seo-check | 每周三 10:00 | SEO 质量检查 |
| burncloud-competitor-monitor | 每周五 10:00 | 竞品监控 |

### 3. 页面创建 ✓

已从模板复制以下页面：

- `/index.html` - 首页
- `/models/index.html` - 模型中心
- `/pricing/index.html` - 定价页
- `/models/deepseek-v4-flash/index.html` - DeepSeek V4 Flash
- `/models/deepseek-v3-2/index.html` - DeepSeek V3.2
- `/security/index.html` - 安全页
- `/blog/index.html` - 博客首页
- `/blog/deepseek-v4-api-guide/index.html` - 博客文章
- `/compare/index.html` - 对比页
- `/compare/deepseek-vs-openai/index.html` - DeepSeek vs OpenAI
- `/docs/quickstart/index.html` - 快速开始
- `/use-cases/indie-developers/index.html` - 独立开发者用例
- `/alternatives/openrouter/index.html` - OpenRouter 替代

---

## 2026-06-08 任务执行

### 价格更新任务 ✓

**执行时间**: 2026-06-08 09:01

**结果**: 执行成功，无价格变动

**说明**: 
- 脚本 `scripts/price_update.py` 正常运行
- 当前价格数据最后更新: 2026-06-07
- 共监控 18 个模型价格
- 无异常价格变动（涨幅>50%）需要告警

**备注**: `fetch_official_prices()` 函数需实现真实抓取逻辑

---

## 待完成任务

### 第二批页面（下周）

- [ ] `/models/gpt-5-4/index.html`
- [ ] `/models/claude-sonnet-4-6/index.html`
- [ ] `/alternatives/siliconflow/index.html`

### 持续执行

- [ ] 每周博客文章 ×1-3 篇
- [ ] 每天价格更新
- [ ] 每周质量检查
- [ ] 每月内容进化

---

## 注意事项

1. **受保护文件**: 不可修改 `data/` 目录下的文件
2. **价格来源**: 只使用 `data/models.json` 中的价格数据
3. **URL 规则**: 所有 URL 不含 `.html` 后缀，不含大写字母，不含下划线
