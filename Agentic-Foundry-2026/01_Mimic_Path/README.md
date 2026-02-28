# 01. 模仿者之路 (The Mimic) - 炼魂夺舍
## The Path of The Mimic: Reverse Engineering & Soul Stealing

> **"如果你没有灵感，就去最好的地方寻找它。"**

### 🔮 核心理念 (Core Concept)
*   **Deconstruction (解构)**: 将一个复杂的黑盒应用（如 Gemini, Perplexity）拆解为原子级的 Prompt 和 Workflow。
*   **Probing (探测)**: 使用社会工程学 Prompt (咒语) 提取 System Prompt 和 Hidden Parameters。
*   **Reconstruction (重构)**: 使用开源组件 (LangGraph, IP-Adapter) 复刻其核心功能。

### 🛠️ 工具集 (Toolkit)

1.  **Summoning Probes (招魂咒语)**:
    *   `architect_eye.md`: 探测竞品架构与多 Agent 协同逻辑。
    *   `law_book.md`: 探测竞品合规边界与负向约束。
    *   `core_probe.md`: 探测竞品生成参数与视觉 Prompt 风格。

2.  **Architecture Mapping (架构映射)**:
    *   `visual_consistency`: 竞品用了 ReferenceNet -> 我们用 IP-Adapter。
    *   `complex_reasoning`: 竞品用了 CoT -> 我们用 LangGraph Planner。
    *   `high_cost_gen`: 竞品全视频生成 -> 我们用 MoviePy + Stable Diffusion。

3.  **Possession Rules (夺舍规则)**:
    *   `.cursorrules`: 放入项目根目录，让 Cursor 自动模仿竞品代码风格。

### 🚀 快速上手 (Quick Start)
1.  选择目标竞品。
2.  使用 `Summoning Probes` 提取其核心逻辑。
3.  将提取的逻辑填入 `Architecture Mapping` 表。
4.  使用 `Possession Rules` 生成复刻代码。

👉 [查看详细探测指南](./Probes/)
