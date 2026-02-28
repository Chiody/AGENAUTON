# 炼魂协议 (Lianhun Protocol)
## The 2026 AI Agent Standardization & Deconstruction Manifesto
### "从黑盒到白盒，从魔法到工程" (From Black Box to Glass Box, From Magic to Engineering)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standard: 2026-Ready](https://img.shields.io/badge/Standard-2026--Ready-blueviolet.svg)](https://github.com/lianhun/protocol)
[![Philosophy: Deconstruction](https://img.shields.io/badge/Philosophy-Deconstruction-ff69b4.svg)](https://sheji.md)

---

## 🔮 为什么要有这个协议？ (Why This Protocol?)

99% 的 AI Agent 都是玩具。它们缺乏**灵魂 (Soul)**、**骨骼 (Structure)** 和 **自我进化 (Evolution)** 的能力。
在 2026 年的 AI 时代，我们不应该再从零开始写 Prompt。我们需要一套**工业化标准**，将顶尖 AI 应用（如 Gemini, Claude, Perplexity）的能力**“解构 (Deconstruct)”**、**“提炼 (Refine)”** 并 **“重塑 (Reconstruct)”** 为我们自己的生产力。

**Lianhun Protocol** 是业内首个定义 **“AI Agent 逆向工程与标准化复刻”** 的开源协议。
它不仅仅是一堆代码，它是一套**“赛博炼金术” (Cyber Alchemy)**：

1.  **招魂 (Summoning)**: 探测与提取黑盒 Agent 的核心 Prompt 与逻辑。
2.  **炼魄 (Refining)**: 将提取的逻辑映射为标准化的开源组件与架构。
3.  **夺舍 (Possession)**: 使用 Cursor + LangGraph 极速复刻并超越原版。
4.  **进化 (Evolution)**: 注入私有数据与合规层，建立商业护城河。

---

## 🧬 核心四部曲 (The 4 Stages of Agent Alchemy)

### 01. 招魂 (The Summoning) - `01_Summoning/`
> **"不仅要看它的皮囊，更要看它的灵魂。"**

这一阶段定义了标准化的**探测工具集 (Probing Toolkit)**。
通过社会工程学注入 (Social Engineering Injection) 与角色扮演，我们获取目标 Agent 的：
*   **System Prompt (灵魂)**: 核心指令与人设。
*   **Constraints (戒律)**: 安全边界与输出限制。
*   **Hidden Parameters (内丹)**: 隐藏的参数与温度设置。

👉 [查看招魂手册 (Summoning Manual)](./01_Summoning/probes.md)

### 02. 炼魄 (The Refining) - `02_Refining/`
> **"去伪存真，提取骨架。"**

将探测到的感性逻辑转化为理性的**工程架构 (Engineering Architecture)**。
这一阶段定义了标准映射表：
*   `Visual Consistency` -> **IP-Adapter / Pulid** (开源平替)
*   `Complex Reasoning` -> **LangGraph StateMachine** (逻辑复刻)
*   `High Cost Generation` -> **ComfyUI / MoviePy** (成本套利)

👉 [查看炼魄图谱 (Refining Map)](./02_Refining/architecture_map.md)

### 03. 夺舍 (The Possession) - `03_Possession/`
> **"以我之躯，承载神力。"**

这是最核心的**复刻阶段 (Reconstruction Phase)**。
我们提供了一套标准化的 **`.cursorrules`** 和 **代码模板**，让 Cursor 成为你的顶级架构师。
只要将“炼魄”后的逻辑喂给 Cursor，它就能生成符合 2026 标准的 Agent 代码。

*   **Standard Stack**: Python 3.12 + LangGraph + Pydantic + FastAPI.
*   **Core Feature**: 自愈能力 (Self-Healing)、异步并发 (Async/Await)、类型安全 (Type Safety)。

👉 [获取夺舍规则 (.cursorrules)](./03_Possession/cursor_rules.md)

### 04. 进化 (The Evolution) - `04_Evolution/`
> **"超越原版，自成一派。"**

复刻只是开始，超越才是目的。
这一阶段关注 **2026 年商业化 Agent** 的核心壁垒：
*   **Compliance (合规)**: 自动添加水印与 AI 标识 (符合 2026 监管)。
*   **Cost Arbitrage (成本套利)**: 智能路由 (Smart Router) 选择最便宜的模型完成任务。
*   **Private Knowledge (私有知识)**: 注入 RAG 形成数据飞轮。

---

## 🏗️ 2026 标准化架构 (The Standard Architecture)

一个合格的 2026 Agent 项目结构应该是这样的：

```
Lianhun-Agent/
├── .cursorrules          # [夺舍核心] AI 编程助手规则 (The Brain)
├── src/
│   ├── core/             # [核心层]
│   │   ├── state.py      # 全局状态定义 (Pydantic Schema)
│   │   ├── config.py     # 环境变量与模型配置
│   │   └── llm.py        # 模型路由 (Model Router)
│   ├── agents/           # [大脑层] (LangGraph Nodes)
│   │   ├── planner.py    # 任务规划器
│   │   ├── executor.py   # 执行器
│   │   └── reviewer.py   # 质量审计员 (Self-Reflection)
│   ├── tools/            # [四肢层] (MCP / APIs)
│   │   ├── search.py     # 联网搜索
│   │   └── media.py      # 多媒体处理 (FFmpeg/ComfyUI)
│   └── prompts/          # [灵魂层] (YAML/Jinja2)
│       ├── system.yaml   # 角色定义
│       └── few_shot.json # 示例库
├── tests/                # [试炼场]
│   └── adversarial/      # 红队测试 (Red Teaming)
└── deploy/               # [飞升台]
    ├── Dockerfile
    └── k8s-chart/
```

---

## 🚀 快速开始 (Start the Ritual)

1.  **Clone the Protocol**:
    ```bash
    git clone https://github.com/your-org/Lianhun-Agent-Protocol.git
    cd Lianhun-Agent-Protocol
    ```

2.  **Summon a Target**:
    使用 `01_Summoning/probes.md` 中的 Prompt，去探测你想要复刻的 Agent。

3.  **Possess with Cursor**:
    将 `03_Possession/cursor_rules.md` 复制到你的项目根目录，并重命名为 `.cursorrules`。
    然后告诉 Cursor: *"按炼魂协议标准，复刻目标 Agent 的逻辑。"*

---

## 📜 宣言 (Manifesto)

我们相信：
*   **代码是廉价的，逻辑是昂贵的。** (Code is cheap, Logic is expensive.)
*   **不要重复造轮子，要学会组装引擎。** (Don't reinvent the wheel, assemble the engine.)
*   **最好的防御是进攻 (逆向)。** (The best defense is offense/reverse-engineering.)

**加入炼魂计划，定义 2026 Agent 标准。**

---
*Based on the "Soul Link" (Lianhun) Methodology.*
