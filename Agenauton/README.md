<div align="center">

# Agenauton 铸基

### The Agentic Standard

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)
[![Website](https://img.shields.io/badge/Website-agenauton.com-8b5cf6?style=for-the-badge)](https://agenauton.com)

**26 letters build every word. 26 dimensions build every Agent.**

**英语有 26 个字母构成所有文字，Agenauton 有 26 个维度覆盖 Agent 构建的所有关键决策。**

[官网](https://agenauton.com) · [快速上手](#quick-start) · [架构标准](#the-standard) · [商业拆解](../duoshe.html) · [马上开始](../zhujiliushi.html) · [在线引导](./guide/index.html)

</div>

---

> [!WARNING]
> **90% 的 Agent 项目死在 Demo 阶段。** 不是技术不行，是从一开始就没想清楚。

想一下你见过的 Agent 项目——

- 聊两句还行，一上生产就崩
- 写了三天 Prompt，换个模型全白费
- 上线一周，Token 费用炸了，老板脸绿了
- 用户一句奇怪的话，AI 开始胡说八道

**根本原因：没有标准。** 每个人都在凭感觉搭，搭完了才发现漏了关键环节。

---

## Agenauton 是什么

一份 **AI Agent 构建标准**。不是框架，不是 SDK，不写一行代码。

6 层架构，26 个维度，覆盖从模型选择到合规伦理的所有关键决策。技术无关——适用于任何模型、任何框架、任何语言。

> **「底子要硬，脑子要清，嘴巴要稳，出事要扛，上线要活。」**
>
> 5 句话，26 个维度，照着走，不翻车。

| 层 | 一句话 | 维度 |
|:---:|--------|------|
| **基础设施** | 底子要硬 | 环境依赖 · 并发伸缩 · 容错恢复 · 成本管控 |
| **数据状态** | 脑子要清 | 数据协议 · 状态记忆 · 知识时效 · 多模态 |
| **核心逻辑** | 脑子要清 | 架构拓扑 · Agent 分工 · 工具能力 · 决策规划 |
| **交互** | 嘴巴要稳 | 指令策略 · 意图理解 · 个性适配 · 输出体验 |
| **治理** | 出事要扛 | 质量闭环 · 幻觉抑制 · 安全防御 · 信任边界 |
| **演进** | 上线要活 | 遥测监控 · 评估测试 · 自演化 · 版本发布 · 合规伦理 · 可解释性 |

---

<a name="quick-start"></a>

## 快速上手 Quick Start

三种方式，选适合你的：

### 方式一：在线引导（零门槛，2 分钟）

打开 [在线引导](./guide/index.html)，回答 8 个选择题，自动生成你的 Agent 蓝图。

### 方式二：一行命令，让 AI 帮你搭

```bash
curl -s https://agenauton.com/skill.md | pbcopy
```

粘贴给你的 AI 编程工具（Cursor / Windsurf / Cline），它会按 26 维度帮你搭好架构骨架。

<details>
<summary><b>或者直接复制这段 Quick Prompt 给 AI</b></summary>

```
你是一位 AI Agent 架构师。请基于 Agenauton 26 维度标准帮我设计 Agent 架构。

在开始写任何代码之前，请先逐一确认以下 26 个维度的设计决策：

【基础设施层】01 环境依赖 02 并发与伸缩 03 容错与恢复 04 成本管控
【数据状态层】05 数据协议 06 状态与记忆 07 知识时效管理 08 多模态处理
【核心逻辑层】09 架构拓扑 10 Agent分工 11 工具能力 12 决策与规划
【交互层】13 指令策略 14 意图理解 15 个性化适配 16 输出体验
【治理层】17 质量闭环 18 幻觉抑制 19 安全防御 20 信任边界
【演进层】21 遥测监控 22 评估测试 23 自演化 24 版本发布 25 合规伦理 26 可解释性

请先问我业务需求，然后逐层给出架构建议，最后生成代码骨架。
```

</details>

### 方式三：下载清单自己填

下载 [26 维度清单模板](./02_Spirit_Refining/26_Dimensions_Template.md)，逐条思考和填写。填完你就有了一份完整的 Agent 架构蓝图。

```bash
git clone https://github.com/agenauton/agenauton.git
cd agenauton

# 打开在线引导
open guide/index.html

# 或复制 AI 执行指令到你的项目
cp 03_Soul_Forging/ai_architect_prompt.md your_project/
```

---

## 两大方法论

不管你是有想法还是没想法，都有路走。

### 铸基六式 / The Forge Flow

> **有想法但不知道怎么落地？六步铸成。**

口诀：**聊找理，投定铸。**

| 步骤 | 关键词 | 做什么 |
|:---:|--------|--------|
| **聊** | Chat | 跟对话大模型聊透你的想法，搞清楚要做什么、怎么做 |
| **找** | Find | 让 AI 找 5 轮开源对标项目，站在巨人肩膀上 |
| **理** | Prep | 把所有对话和参考整理成一份 MD 文档 |
| **投** | Feed | 把文档投喂给 AI 编程工具，这是你的实现思路 |
| **定** | Frame | 用 26 维度标准定好架构骨架 |
| **铸** | Forge | Vibe Coding，铸成产品 |

**不烧 Token，先烧脑子。** 想清楚了，剩下的就是六步的事。

**→ [查看完整铸基六式方法论 + 实战案例](../zhujiliushi.html)**

### 夺舍大法 / Agent Autopsy

> **没想法？先拆解别人的。**

三步：**搜魂 → 炼魄 → 锻造**

| 步骤 | 做什么 |
|:---:|--------|
| **搜魂** Probe | 用「炼魂 9 问」穿透目标 Agent，摸清底层机制 |
| **炼魄** Map | 用 26 维度标准化测绘，把碎片信息结构化 |
| **锻造** Forge | 基于测绘结果，用 AI 辅助生成你自己的代码骨架 |

> *不是复制别人的产品，是理解别人的智慧，然后超越。*

**→ [查看完整夺舍大法方法论 + 炼魂 9 问 + 案例库](../duoshe.html)**

---

<a name="the-standard"></a>

## 26 维度专业矩阵 The 26-Dimension Matrix

<details>
<summary><b>点击展开完整矩阵（供工程师、架构师和技术决策者参考）</b></summary>

Six architectural layers. Twenty-six dimensions. One standard.

### Layer 1: Infrastructure 基础设施层

| # | Dimension | Key Question |
|---|-----------|-------------|
| 01 | **Environment & Dependencies** 环境依赖 | 模型选择、运行库、API 版本、部署环境 |
| 02 | **Concurrency & Scaling** 并发与伸缩 | 多用户并发处理、负载均衡、弹性扩容、降级策略 |
| 03 | **Fault Tolerance** 容错与恢复 | 工具调用失败、模型超时、重试策略、降级方案 |
| 04 | **Cost Control** 成本管控 | Token 预算、模型路由（强模型/弱模型）、截断策略 |

### Layer 2: Data & State 数据与状态层

| # | Dimension | Key Question |
|---|-----------|-------------|
| 05 | **Data Schema** 数据协议 | 输入输出格式、内部数据结构、字段定义 |
| 06 | **State & Memory** 状态与记忆 | 短期/长期记忆、用户画像、会话持久化 |
| 07 | **Knowledge & Temporal** 知识时效管理 | RAG 检索、重排、知识更新、时间衰减 |
| 08 | **Multimodal** 多模态处理 | 文本/图片/音频/视频/文件的输入输出处理 |

### Layer 3: Core Logic 核心逻辑层

| # | Dimension | Key Question |
|---|-----------|-------------|
| 09 | **Architecture Topology** 架构拓扑 | 单体 Agent vs 多 Agent 编排 |
| 10 | **Agent Division** Agent 分工 | 子 Agent 职责、输入输出、协作协议 |
| 11 | **Tool Mapping** 工具能力 | 外部工具注册、触发条件、参数、错误处理 |
| 12 | **Planning & Reasoning** 决策与规划 | 任务分解、执行计划、条件路由 |

### Layer 4: Interaction 交互层

| # | Dimension | Key Question |
|---|-----------|-------------|
| 13 | **Instruction Strategy** 指令策略 | System Prompt 设计、角色设定、Golden Rules |
| 14 | **Intent Alignment** 意图理解 | 意图分类、歧义处理、多轮对话、工程 Trick |
| 15 | **Personalization** 个性化适配 | 风格适配、语言切换、人格设定、用户画像 |
| 16 | **Output Experience** 输出体验 | 流式输出、思考过程展示、引用呈现、格式设计 |

### Layer 5: Governance 治理层

| # | Dimension | Key Question |
|---|-----------|-------------|
| 17 | **Quality Loop** 质量闭环 | 自检逻辑、重试策略、反思循环 |
| 18 | **Hallucination Suppression** 幻觉抑制 | 事实核查、引用标注、不确定性表达 |
| 19 | **Safety Defense** 安全防御 | 内容审核、注入防御、敏感过滤 |
| 20 | **Trust Boundary** 信任边界 | 置信度量化、人工介入触发、升级机制 |

### Layer 6: Evolution 演进层

| # | Dimension | Key Question |
|---|-----------|-------------|
| 21 | **Telemetry & Monitoring** 遥测与监控 | 日志、指标、用户反馈收集 |
| 22 | **Evaluation & Testing** 评估与测试 | 基准测试、A/B 测试、回归测试 |
| 23 | **Self-Evolution** 自演化 | Prompt 动态调优、模型微调、自适应 |
| 24 | **Version & Release** 版本与发布 | 版本管理、灰度发布、回滚策略 |
| 25 | **Compliance & Ethics** 合规与伦理 | 数据隐私、AI 标识、监管合规 |
| 26 | **Explainability** 可解释性 | 决策透明度、推理过程可追溯 |

> [下载可填写的 26 维度专业模板 →](./02_Spirit_Refining/26_Dimensions_Template.md)

</details>

---

## 给 AI 编程工具的指令 For AI

> *以下内容专门设计给 AI 编程工具（Cursor、Windsurf、Cline 等）读取和执行。*

| 资源 | 说明 |
|------|------|
| [ai_architect_prompt.md](./03_Soul_Forging/ai_architect_prompt.md) | 完整的 AI 架构师指令（每个维度的详细检查项） |
| [forgebase.cursorrules](./cursor_rules/forgebase.cursorrules) | 可直接复制到项目的 `.cursorrules` 文件 |
| [skeleton_generator.md](./03_Soul_Forging/skeleton_generator.md) | 架构骨架生成元指令 |

---

## 项目结构 Project Structure

```
.
├── index.html                      # 官网首页（中英双语）
├── duoshe.html                        # 夺舍大法 — 商业拆解方法论
├── zhujiliushi.html                   # 铸基六式 — 从想法到产品的六步法
├── lang.js                            # 全站双语切换模块
│
├── Agenauton/                         # 核心标准库
│   ├── README.md                      # 你在这里
│   ├── LICENSE                        # MIT 开源协议
│   ├── CONTRIBUTING.md                # 参与贡献
│   │
│   ├── 01_Soul_Extraction/            # 搜魂 — 拆解学习指南
│   │   ├── README.md
│   │   ├── identity_masks.md          # 提问角度和话术模板
│   │   ├── probing_scripts.md         # 按维度分类的探测问题
│   │   └── advanced_techniques.md     # 进阶分析技巧
│   │
│   ├── 02_Spirit_Refining/            # 炼魄 — 26 维度清单
│   │   ├── README.md
│   │   ├── 26_Dimensions_Template.md  # 可填写的专业模板
│   │   └── glossary.md               # 术语表（大白话解释）
│   │
│   ├── 03_Soul_Forging/              # 锻造 — 架构生成
│   │   ├── README.md
│   │   ├── ai_architect_prompt.md     # AI 专用完整执行指令
│   │   ├── skeleton_generator.md      # 架构骨架生成元指令
│   │   └── cursor_rules.md           # Cursor IDE 规则说明
│   │
│   ├── 04_Case_Studies/              # 实战案例
│   │   └── README.md
│   │
│   ├── 05_Defensive_Lab/             # 防御实验室
│   │   ├── anti_probing.md            # 怎么保护自己的 Agent
│   │   └── safety_alignment.md        # 安全与伦理
│   │
│   ├── community/                     # 社区
│   │   └── roadmap.md                 # 路线图
│   │
│   ├── cursor_rules/                  # Cursor 规则包
│   │   └── forgebase.cursorrules      # 可直接使用的规则文件
│   │
│   └── guide/                         # 在线引导
│       └── index.html                 # 交互式问答（8 题生成蓝图）
│
└── marketing/                         # 推广素材
    ├── slogans.md                     # 口号库
    └── articles/                      # 中英文推广文章
```

---

## 路线图 Roadmap

### v1.0 — Foundation 铸基 (Current)

- [x] 26 维度矩阵定义
- [x] 可填写蓝图模板
- [x] 搜魂探测指令库 + 身份伪装库
- [x] 架构生成元指令 + Cursor Rules
- [x] 交互式在线引导（8 题生成蓝图）
- [x] 防御实验室
- [x] 双语 README
- [x] 官网 (index.html) + 中英双语
- [x] 夺舍大法页面 + 炼魂 9 问 + 案例库
- [x] 铸基六式页面 + 实战案例
- [x] 交互式 26 维度雷达图

### v1.1 — Automation 自动化

- [ ] CLI 工具：命令行快速创建蓝图
- [ ] VS Code / Cursor 扩展
- [ ] 自动化探测 Agent

### v2.0 — Intelligence 智能化

- [ ] 自审计 Agent：AI 审计 AI
- [ ] 实时维度评分
- [ ] Agent 市场集成

### v3.0 — Standard 标准化

- [ ] 行业采纳合作
- [ ] Agenauton 认证计划
- [ ] 年度 "State of Agentic Intelligence" 报告

---

## 参与贡献 Contributing

我们欢迎所有形式的贡献。详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

最有价值的贡献方式：

- **提交案例** — 用 26 维度分析一个 Agent，提交到 `04_Case_Studies/`
- **提交铸基六式实战** — 分享你从想法到产品的六步过程
- **完善标准** — 优化维度定义、添加探测话术、改进术语表
- **翻译** — 帮助更多语言的开发者使用 Agenauton

---

<div align="center">

**每一个想法都值得被铸造。**

**Think first. Build right. Build once.**

**© 2026 Agenauton — The Agentic Standard.**

[Back to Top](#agenauton-铸基)

</div>
