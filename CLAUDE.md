# BurnCloud SEO & Content Automation

# Hermes Agent 工作手册

# 最后更新：2026-06-05

-----

## 一、项目背景

产品： BurnCloud — 开源LLM API网关
网站： burncloud.com
核心Slogan： Don't trust us. Verify us.
目标受众： 海外独立开发者、AI Startup、企业技术负责人
竞争对手： OpenRouter、SiliconFlow、LiteLLM
网站风格： 白色系，对标OpenRouter，单HTML文件，零外部依赖

-----

## 二、数据源（只读，不可修改）
/data/models.json           所有模型最新价格
/data/seo-rules.json        SEO规范标准
/data/protected-files.json  受保护文件列表

所有价格数据必须来自 /data/models.json，不得自行编造。

-----

## 三、文件结构规范

### URL规则（最重要）
✅ 正确：文件夹结构，URL干净无后缀
/models/deepseek-v4/index.html     → 访问地址：/models/deepseek-v4
/blog/deepseek-api-guide/index.html → 访问地址：/blog/deepseek-api-guide
/pricing/index.html                 → 访问地址：/pricing

❌ 错误：带.html后缀
/models/deepseek-v4.html
/blog/deepseek-api-guide.html

### 完整文件目录
burncloud.com/
│
├── index.html                          ← 首页（受保护）
├── CLAUDE.md                           ← 本文件（受保护）
├── sitemap.xml                         ← 自动生成
├── robots.txt                          ← 自动生成
│
├── data/                               ← 只读数据源
│   ├── models.json                     ← 模型价格（受保护）
│   ├── seo-rules.json                  ← SEO规范
│   └── protected-files.json            ← 受保护文件列表
│
├── models/
│   ├── index.html                      ← 模型大厅
│   ├── deepseek-v4/index.html          → /models/deepseek-v4
│   ├── deepseek-v4-flash/index.html    → /models/deepseek-v4-flash
│   ├── deepseek-v3-2/index.html        → /models/deepseek-v3-2
│   ├── claude-sonnet-4-6/index.html    → /models/claude-sonnet-4-6
│   ├── claude-opus-4-7/index.html      → /models/claude-opus-4-7
│   ├── claude-haiku-4-5/index.html     → /models/claude-haiku-4-5
│   ├── gpt-5-4/index.html              → /models/gpt-5-4
│   ├── gpt-5-5/index.html              → /models/gpt-5-5
│   ├── gemini-3-1-pro/index.html       → /models/gemini-3-1-pro
│   ├── gemini-3-5-flash/index.html     → /models/gemini-3-5-flash
│   ├── qwen-3-5/index.html             → /models/qwen-3-5
│   ├── kimi-k2-6/index.html            → /models/kimi-k2-6
│   ├── step-3-5-flash/index.html       → /models/step-3-5-flash
│   ├── doubao-pro/index.html           → /models/doubao-pro
│   ├── minimax/index.html              → /models/minimax
│   └── glm-5-1/index.html             → /models/glm-5-1
│
├── compare/
│   ├── index.html                      ← 对比工具主页
│   ├── deepseek-vs-openai/index.html   → /compare/deepseek-vs-openai
│   ├── deepseek-v4-vs-claude/index.html→ /compare/deepseek-v4-vs-claude
│   ├── claude-vs-gpt/index.html        → /compare/claude-vs-gpt
│   ├── burncloud-vs-openrouter/index.html → /compare/burncloud-vs-openrouter
│   └── burncloud-vs-siliconflow/index.html → /compare/burncloud-vs-siliconflow
│
├── blog/
│   ├── index.html                      ← 博客列表
│   ├── deepseek-v4-api-guide/index.html → /blog/deepseek-v4-api-guide
│   ├── cheapest-llm-api-2026/index.html → /blog/cheapest-llm-api-2026
│   └── [后续文章]/index.html
│
├── alternatives/
│   ├── openrouter/index.html           → /alternatives/openrouter
│   └── siliconflow/index.html          → /alternatives/siliconflow
│
├── use-cases/
│   ├── indie-developers/index.html     → /use-cases/indie-developers
│   ├── startups/index.html             → /use-cases/startups
│   └── enterprise/index.html           → /use-cases/enterprise
│
├── pricing/
│   └── index.html                      → /pricing
│
├── security/
│   └── index.html                      → /security（受保护）
│
├── docs/
│   ├── quickstart/index.html           → /docs/quickstart
│   ├── models/index.html               → /docs/models
│   └── api-reference/index.html        → /docs/api-reference
│
├── self-host/
│   └── index.html                      → /self-host
│
├── suppliers/
│   └── index.html                      → /suppliers
│
├── status/
│   └── index.html                      → /status
│
├── privacy/
│   └── index.html                      → /privacy（受保护）
│
├── terms/
│   └── index.html                      → /terms（受保护）
│
├── .github/
│   └── workflows/
│       └── seo-automation.yml          ← 定时任务（受保护）
│
└── reports/                            ← Hermes工作报告
    ├── weekly.md
    ├── monthly.md
    ├── price-log.md
    ├── issues.md
    ├── competitive.md
    └── alert.md

-----

## 四、受保护文件（绝对不可修改）
index.html
CLAUDE.md
/data/models.json
/security/index.html
/privacy/index.html
/terms/index.html
.github/workflows/

任何任务涉及以上文件，立即停止并通知。

-----

## 五、SEO规范（每个页面必须遵守）

### Title格式
[主关键词] | [次关键词] | BurnCloud
字数限制：60字以内
例：DeepSeek V4 API — $0.14/1M Tokens | BurnCloud

### Meta Description格式
核心价值 + 行动号召
字数限制：120字以内
例：Access DeepSeek V4 at $0.14/1M tokens.
    Open source gateway. Start free.

### H标签规范
H1：只有一个，包含主关键词
H2：4-6个，覆盖次级关键词
H3：FAQ问题

### URL规范
全小写，连字符分隔，无.html后缀，无参数
正确：/models/deepseek-v4
错误：/models/deepseek-v4.html
错误：/models/deepseek_v4
错误：/models/DeepSeekV4

### Canonical标签
<link rel="canonical" href="https://burncloud.com/models/deepseek-v4">
注意：URL末尾不带斜杠，不带.html

### 内链规范
每个页面至少3个内链
模型页必须链接：/compare /pricing /docs/quickstart
博客页必须链接：相关模型页×2 + 首页
对比页必须链接：两个被对比的模型详情页

### Schema规范
模型页：Product schema
博客页：Article schema
对比页：FAQPage schema
文档页：HowTo schema
所有页面：BreadcrumbList schema

### 面包屑规范
首页 > 分类 > 当前页
例：Home > Models > DeepSeek V4

对应BreadcrumbList Schema：
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"https://burncloud.com"},
    {"@type":"ListItem","position":2,"name":"Models","item":"https://burncloud.com/models"},
    {"@type":"ListItem","position":3,"name":"DeepSeek V4","item":"https://burncloud.com/models/deepseek-v4"}
  ]
}

### 页面质量10项检查
□ 1. Title存在且<60字，包含主关键词
□ 2. Meta Description存在且<120字
□ 3. H1唯一且包含主关键词
□ 4. 面包屑导航存在
□ 5. BreadcrumbList Schema正确
□ 6. 内链>=3个，全部有效
□ 7. 页面大小<100KB
□ 8. 移动端meta viewport存在
□ 9. Canonical标签存在，URL无.html后缀
□ 10. Open Graph标签存在

-----

## 六、页面结构规范

### /models/index.html → 访问地址：/models
Title：
"All AI Models — One API Key |
 Compare Prices 2026 | BurnCloud"

Meta Description：
"Compare Claude, GPT-5.5, DeepSeek V4 and top
 Chinese LLMs. One API key, lowest cost,
 open source gateway."

Canonical: https://burncloud.com/models

H1: All AI Models — One API Key
H2: Chinese Models
H2: Frontier Models
H2: Full Price Comparison Table
H2: FAQ

内链：
→ /compare
→ /pricing
→ /docs/quickstart

Schema：ItemList + BreadcrumbList
自动更新：每天同步data/models.json价格

-----

### /models/[model-name]/index.html → 访问地址：/models/[model-name]
Title：
"[模型名] API — $[价格]/1M Tokens |
 2026 | BurnCloud"

Canonical: https://burncloud.com/models/[model-name]

H1: [模型名] API — [核心卖点]
H2: Pricing & Specifications
H2: How to Use [模型名] API
H2: Best Use Cases
H2: [模型名] vs Alternatives
H2: Frequently Asked Questions

侧边栏：
- 快速开始CTA
- 目录锚点
- 相关模型×3（链接到对应模型页）

内链：
→ /compare/[model]-vs-[competitor]
→ /blog/[model]-api-guide
→ /docs/quickstart

Schema：Product + BreadcrumbList
自动更新：每天同步价格数据

模型页创建优先级：
第一批：
/models/deepseek-v4/
/models/deepseek-v4-flash/
/models/claude-sonnet-4-6/
/models/claude-opus-4-7/
/models/gpt-5-4/
/models/gpt-5-5/

第二批：
/models/gemini-3-1-pro/
/models/gemini-3-5-flash/
/models/qwen-3-5/
/models/deepseek-v3-2/
/models/kimi-k2-6/
/models/step-3-5-flash/
/models/doubao-pro/
/models/minimax/
/models/glm-5-1/

-----

### /pricing/index.html → 访问地址：/pricing
Title：
"LLM API Pricing Calculator 2026 |
 Compare All Models | BurnCloud"

Canonical: https://burncloud.com/pricing

H1: LLM API Pricing Calculator
H2: Calculate Your Monthly Cost
H2: Full Model Pricing Table
H2: BurnCloud vs Official Pricing
H2: FAQ

内链：
→ /models
→ /compare
→ /docs/quickstart

Schema：FAQPage + BreadcrumbList
自动更新：每天同步价格

-----

### /compare/index.html → 访问地址：/compare
Title：
"Compare LLM Models & Providers 2026 |
 Side by Side | BurnCloud"

Canonical: https://burncloud.com/compare

H1: Compare AI Models Side by Side
H2: Select Models to Compare
H2: Popular Comparisons
H2: Compare by Use Case

内链：→ /models → /pricing
Schema：FAQPage + BreadcrumbList

-----

### /compare/[model-a]-vs-[model-b]/index.html
Title：
"[模型A] vs [模型B]:
 Cost & Performance 2026 | BurnCloud"

Canonical: https://burncloud.com/compare/[model-a]-vs-[model-b]

H1: [模型A] vs [模型B]: Complete Comparison 2026
H2: Quick Verdict
H2: Price Comparison
H2: Performance Benchmarks
H2: Speed & Latency
H2: Best Use Cases
H2: How to Switch
H2: FAQ

内链：
→ /models/[model-a]
→ /models/[model-b]
→ /pricing

Schema：FAQPage + BreadcrumbList
自动更新：每月更新价格和benchmark

对比页创建优先级：
/compare/deepseek-vs-openai/
/compare/deepseek-v4-vs-claude/
/compare/claude-vs-gpt/
/compare/burncloud-vs-openrouter/
/compare/burncloud-vs-siliconflow/

-----

### /alternatives/openrouter/index.html → /alternatives/openrouter
Title：
"Best OpenRouter Alternative 2026 |
 No Fees, Open Source | BurnCloud"

Canonical: https://burncloud.com/alternatives/openrouter

H1: The Best OpenRouter Alternative in 2026
H2: Why Developers Switch from OpenRouter
H2: Feature Comparison
H2: Price Difference Calculator
H2: Chinese Model Support
H2: How to Migrate
H2: FAQ

内链：
→ /compare/burncloud-vs-openrouter
→ /models
→ /pricing

Schema：FAQPage + BreadcrumbList
自动更新：每月检查OpenRouter新功能

-----

### /alternatives/siliconflow/index.html → /alternatives/siliconflow
Title：
"Best SiliconFlow Alternative 2026 |
 Global Models + Open Source | BurnCloud"

Canonical: https://burncloud.com/alternatives/siliconflow

H1: BurnCloud vs SiliconFlow:
    Global Models, Better Trust
H2: What SiliconFlow Doesn't Offer
H2: Feature Comparison
H2: Price Comparison
H2: How to Migrate
H2: FAQ

Schema：FAQPage + BreadcrumbList

-----

### /blog/index.html → 访问地址：/blog
Title：
"BurnCloud Blog | LLM API Guides,
 Tutorials & Industry News"

Canonical: https://burncloud.com/blog

H1: BurnCloud Blog
分类筛选：Tutorials · Comparisons · News

文章卡片包含：
- 分类标签
- H2文章标题
- 摘要100字
- 发布日期
- 阅读时间
- 链接到 /blog/[slug]

-----

### /blog/[slug]/index.html → 访问地址：/blog/[slug]
Title：
"[文章标题] | BurnCloud Blog"

Canonical: https://burncloud.com/blog/[slug]

结构：
面包屑：Home > Blog > [文章标题]

主内容区（70%）：
H1: 文章标题
发布日期 · 更新日期 · 阅读时间
H2: 章节一
H2: 章节二
H2: 章节三
H2: FAQ（5个问题）
内链×3
最终CTA

侧边栏（30%）：
- 目录（锚点导航）
- 相关文章×3
- CTA卡片："Try BurnCloud Free →"
- 相关模型快速入口

Schema：Article + BreadcrumbList

-----

### /use-cases/indie-developers/index.html
Title：
"BurnCloud for Indie Developers |
 Pay Per Token, No Commitment | BurnCloud"

H1: The LLM API Built for Indie Developers
H2: Why Indie Devs Choose BurnCloud
H2: Real Cost Examples
H2: No Lock-in Guarantee
H2: Start in 2 Minutes
H2: FAQ

内链：→ /pricing → /models → /docs/quickstart
Schema：FAQPage + BreadcrumbList

-----

### /use-cases/startups/index.html
Title：
"BurnCloud for Startups |
 Scale AI Without Breaking Budget | BurnCloud"

H1: Scale Your AI Product Without Breaking Budget
H2: The Startup Problem
H2: Multi-Model Strategy
H2: High Availability
H2: Cost Control
H2: FAQ

内链：→ /pricing → /models → /docs/quickstart
Schema：FAQPage + BreadcrumbList

-----

### /use-cases/enterprise/index.html
Title：
"BurnCloud for Enterprise |
 Secure, Auditable LLM Gateway | BurnCloud"

H1: Enterprise-Grade LLM Gateway
    You Can Actually Verify
H2: Enterprise Requirements Met
H2: Security Architecture
H2: Compliance
H2: Deployment Options
H2: SLA & Support
H2: FAQ

内链：→ /security → /self-host → /pricing
Schema：FAQPage + BreadcrumbList

-----

### /docs/quickstart/index.html → /docs/quickstart
Title：
"Quick Start Guide | BurnCloud API
 Setup in 2 Minutes"

H1: Quick Start Guide
H2: Step 1 — Create Your Account
H2: Step 2 — Add Credits
H2: Step 3 — Get Your API Key
H2: Step 4 — Make Your First Call
H2: Choose Your Model
H2: Next Steps

内链：→ /models → /pricing → /docs/api-reference
Schema：HowTo + BreadcrumbList

-----

### /self-host/index.html → /self-host
Title：
"Self-Host BurnCloud |
 Deploy Your Own LLM Gateway"

H1: Deploy BurnCloud on Your Own Server
H2: Why Self-Host?
H2: Requirements
H2: Installation
H2: Configuration
H2: Verify Your Deployment
H2: FAQ

内链：→ /security → /docs/quickstart
Schema：HowTo + BreadcrumbList

-----

### /suppliers/index.html → /suppliers
Title：
"Become a BurnCloud Supplier |
 Join the Verified LLM Marketplace"

H1: Join the BurnCloud Supplier Marketplace
H2: What is the BurnCloud Marketplace
H2: Supplier Requirements
H2: Benefits for Suppliers
H2: Verification Process
H2: Apply Now
H2: FAQ

Schema：FAQPage + BreadcrumbList

-----

### /status/index.html → /status
Title：
"BurnCloud System Status |
 Real-time Uptime & Latency"

H1: System Status
实时状态 + 每个模型延迟
H2: API Endpoints
H2: Uptime History (90 days)
H2: Incident History

自动更新：实时数据，全自动

-----

## 七、定时任务规范

### 任务一：每天早上9点 — 价格更新
执行步骤：
1. 抓取各官方价格页面
2. 对比现有data/models.json
3. 发现变化则更新
4. 同步到所有模型页面
5. 同步到/pricing
6. 生成日志到reports/price-log.md

完成标准：
- 所有页面价格与官方一致
- 价格变更日志已记录

-----

### 任务二：每周一早上10点 — 博客生成
选题来源（按优先级）：
1. Google Search Console排名11-30的关键词
2. HackerNews评论数>50的LLM相关帖子
3. Reddit r/MachineLearning upvote>100的问题
4. 竞品最新博客文章的关键词

选题评分标准：
月搜索量>1000：+3分
竞品已有文章：+2分
和BurnCloud产品直接相关：+2分
HN讨论热度高：+1分
我们已有类似文章：-3分
搜索量<100：-2分
总分>5分：本周必须写

文章类型比例：
40% 教程类
30% 对比类
20% 资讯类
10% 深度类

文章质量标准：
- 字数：1000-2000字
- 代码示例：至少1个
- 内链：>=3个
- FAQ：5个问题
- 发布日期：必须显示

URL格式：
/blog/[关键词-用连字符-连接-2026]/
例：/blog/deepseek-v4-api-guide-2026/

-----

### 任务三：每周三早上10点 — 页面质量检查
执行步骤：
1. 遍历所有页面
2. 对每个页面运行10项SEO检查
3. 发现问题自动修复
4. 无法修复记录到reports/issues.md

重点检查：
- Canonical URL不含.html后缀
- 所有内链URL不含.html后缀
- 面包屑链接正确

-----

### 任务四：每周五早上10点 — 竞品监控
监控对象：
openrouter.ai
siliconflow.com
litellm.ai

处理规则：
竞品新增模型页
→ BurnCloud支持：自动创建 /models/[model-name]/index.html
→ BurnCloud不支持：通知人工决策

竞品新增对比页
→ 月搜索量>500：自动创建对应页面
→ 月搜索量<500：忽略

竞品价格低于BurnCloud
→ 立即通知，等待人工处理

完成标准：
报告生成到reports/competitive.md

-----

### 任务五：每月1日早上10点 — 内容进化
检查所有博客文章Google排名：

排名1-10（表现好）：
→ 找3个相关长尾词
→ 生成3篇系列文章
→ 建立内链集群

排名11-30（可以优化）：
→ 重写Title和Meta Description
→ 补充内容到1500字以上
→ 更新价格数据
→ 更新发布日期

排名>30超过3个月（表现差）：
→ 生成分析报告
→ 通知人工决策

同时执行：
- 更新所有对比页benchmark数据
- 生成月度SEO报告到reports/monthly.md

-----

## 八、博客内链集群策略
每个主要模型建立内链集群：

DeepSeek集群：
核心页：/models/deepseek-v4
关联页：
- /blog/deepseek-v4-api-guide
- /blog/deepseek-vs-openai-cost
- /blog/how-to-use-deepseek-python
- /compare/deepseek-vs-openai
所有页面互相内链

Claude集群：
核心页：/models/claude-sonnet-4-6
关联页：
- /blog/claude-api-guide
- /blog/claude-vs-gpt-comparison
- /compare/claude-vs-gpt
所有页面互相内链

规则：
同一集群内的页面必须互相链接
集群内所有内链URL均不含.html后缀

-----

## 九、通知规则

### 立即停止并通知
- 需要修改受保护文件
- 价格数据异常（涨幅>50%）
- 竞品价格低于BurnCloud
- 连续失败3次以上
- 不确定如何执行

### 每周汇报（reports/weekly.md）
本周完成的页面列表（含访问URL）
本周发布的文章
价格变动记录
竞品动态
需要人工决策的事项

### 每月汇报（reports/monthly.md）
SEO整体排名变化
流量增长数据
内容进化结果
竞品对比分析
下月执行计划

-----

## 十、执行优先级

### 第一批（本周）
□ /models/index.html
□ /models/deepseek-v4/index.html
□ /models/claude-sonnet-4-6/index.html
□ /pricing/index.html
□ /privacy/index.html
□ /terms/index.html

### 第二批（下周）
□ /models/gpt-5-4/index.html
□ /models/deepseek-v4-flash/index.html
□ /compare/deepseek-vs-openai/index.html
□ /alternatives/openrouter/index.html
□ /docs/quickstart/index.html
□ /blog/[第一篇文章]/index.html

### 第三批（第三周）
□ /compare/burncloud-vs-openrouter/index.html
□ /alternatives/siliconflow/index.html
□ /use-cases/indie-developers/index.html
□ /security/index.html（人工审核后上线）
□ /blog/[第二批文章×3]

### 持续执行
□ 每周博客文章×1-3篇
□ 每天价格更新
□ 每周质量检查
□ 每月内容进化
□ 竞品监控跟进

-----

## 十一、绝对禁止
✗ URL含.html后缀
✗ URL含大写字母
✗ URL含下划线
✗ 修改受保护文件
✗ 删除已发布的页面
✗ 使用data/models.json以外的价格数据
✗ 修改核心Slogan
✗ 在没有通过10项SEO检查的情况下发布页面
✗ 一次执行超过1个页面的新建任务
✗ 在不确定的情况下继续执行

-----

## 十二、当你不确定的时候
停下来。
生成报告到reports/alert.md。
标注：[需要人工处理]
描述：
- 遇到了什么情况
- 有哪些选项
- 你的建议是什么
等待人工确认再继续。
