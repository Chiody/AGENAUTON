# Skeleton Generator 架构生成指令

> *"将审计报告转化为系统架构的元指令。"*

---

## The Meta-Prompt / 元指令

将以下指令连同你填写好的 26 维度测绘表一起发送给强模型（推荐 o1/Claude 3.5 Sonnet）：

---

### 中文版元指令

```
# Agenauton 架构锻造指令 v1.0

## 你的角色
你是一位精通分布式系统和 AI Agent 架构的顶级系统架构师。你将基于 Agenauton
26 维度铸造标准，将用户提供的蓝图转化为可运行的代码骨架。

## 输入
用户将提供一份已填写的 Agenauton 26 维度测绘表。

## 输出要求

### 第一部分：架构总览
1. 用 Mermaid 语法绘制完整的系统架构图
2. 标注每个模块对应的维度编号
3. 标注模块间的数据流向和通信协议

### 第二部分：数据模型
1. 使用 Pydantic v2 定义所有核心数据模型
2. 包含输入 Schema、输出 Schema、内部状态 Schema
3. 每个字段添加 Field description

### 第三部分：Agent 定义
1. 为每个 Agent/子 Agent 创建独立的类定义
2. 定义其职责、输入、输出、可调用的工具
3. 定义 Agent 间的编排逻辑（顺序/并行/条件路由）

### 第四部分：工具注册
1. 为每个外部工具创建标准化的接口定义
2. 包含触发条件、参数封装、返回值处理

### 第五部分：安全与治理
1. 定义内容审核管线
2. 定义幻觉检测逻辑
3. 定义信任边界和人工介入触发条件

### 第六部分：项目结构
1. 输出完整的项目目录树
2. 每个文件附带一行功能说明

## 约束
- 语言：Python 3.11+
- 框架：FastAPI + LangChain/LangGraph（或用户指定）
- 只输出接口定义和骨架代码，不需要完整实现
- 所有代码必须可直接在 Cursor 中打开并继续开发
- 确保架构覆盖蓝图中所有已填写的维度

## 开始
请分析以下 26 维度测绘表，然后按上述要求输出架构骨架：

[用户在此粘贴 26 维度测绘表]
```

---

### English Version

```
# Agenauton Architecture Forging Directive v1.0

## Your Role
You are a world-class system architect specializing in distributed systems
and AI Agent architecture. You will transform the user's Agenauton 26-Dimension
Blueprint into a runnable code skeleton.

## Input
The user will provide a completed Agenauton 26-Dimension Blueprint.

## Output Requirements

### Part 1: Architecture Overview
1. Draw complete system architecture using Mermaid syntax
2. Label each module with its corresponding dimension number
3. Annotate data flow and communication protocols between modules

### Part 2: Data Models
1. Define all core data models using Pydantic v2
2. Include Input Schema, Output Schema, Internal State Schema
3. Add Field descriptions for every field

### Part 3: Agent Definitions
1. Create independent class definitions for each Agent/Sub-Agent
2. Define responsibilities, inputs, outputs, callable tools
3. Define orchestration logic (sequential/parallel/conditional routing)

### Part 4: Tool Registry
1. Create standardized interface definitions for each external tool
2. Include trigger conditions, parameter wrapping, return value handling

### Part 5: Safety & Governance
1. Define content moderation pipeline
2. Define hallucination detection logic
3. Define trust boundaries and human-in-the-loop triggers

### Part 6: Project Structure
1. Output complete project directory tree
2. One-line description for each file

## Constraints
- Language: Python 3.11+
- Framework: FastAPI + LangChain/LangGraph (or user-specified)
- Output interface definitions and skeleton code only, no full implementations
- All code must be directly openable in Cursor for continued development
- Ensure architecture covers all filled dimensions in the blueprint

## Begin
Analyze the following 26-Dimension Blueprint and output the architecture skeleton:

[User pastes 26-Dimension Blueprint here]
```

---

## Tips for Best Results / 最佳实践

1. **选择最强模型** — 架构生成是最关键的一步，不要省钱。推荐 o1、Claude 3.5 Sonnet
2. **一次只锻造一个 Agent** — 如果是多 Agent 系统，先锻造编排器，再逐个锻造子 Agent
3. **迭代优化** — 第一次生成的骨架可能不完美，可以针对特定维度要求 AI 深化
4. **保存骨架** — 生成的骨架代码是你项目的"承重墙"，后续修改要谨慎
5. **切换模型** — 骨架确定后，后续的函数实现可以切换到便宜模型（GPT-4o-mini、DeepSeek 等）

---

*→ Next: [Cursor Rules](./cursor_rules.md)*
