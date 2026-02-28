# 02. 构建者之路 (The Builder) - 标准化架构
## The Path of The Builder: Standardized Scaffolding & Patterns

> **"你有绝妙的想法，我们教你如何优雅地实现它。"**

### 🏗️ 核心理念 (Core Concept)
*   **Separation of Concerns (关注点分离)**: 强制将 Logic (Prompt), Workflow (Graph), Data (State) 分离。
*   **Engineering First (工程优先)**: 优先使用 Python/Shell 代码解决确定性问题，大模型只负责不确定性。
*   **Observability (可观测性)**: 全链路 Tracing 与 Metrics，确保 Agent 运行透明。

### 🧠 架构模式 (Architectural Patterns)

1.  **Planner-Executor-Reviewer (PER)**:
    *   **Planner**: 拆解任务为步骤。
    *   **Executor**: 执行每个步骤。
    *   **Reviewer**: 检查结果是否符合 Schema，自我纠错。

2.  **Supervisor-Workers (SW)**:
    *   **Supervisor**: 中央调度器，分发任务给子 Agent。
    *   **Workers**: 专注单一领域的子 Agent (如 Search, Code, Visual)。

3.  **Reflection-Critique (RC)**:
    *   **Actor**: 生成初稿。
    *   **Critic**: 提出修改意见。
    *   **Refiner**: 根据意见优化。

### ⚡ 最佳实践 (Best Practices)
*   **Async/Await**: 所有 I/O 操作必须异步。
*   **Streaming**: 必须流式输出 Token，提升用户体验。
*   **Typed State**: 使用 Pydantic 定义强类型 State。

👉 [查看标准脚手架](./Scaffolding/)
