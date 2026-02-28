# 03. 夺舍 (The Possession) - Cursor 规则与复刻模板
## The Standard `.cursorrules` for 2026 AI Agent Reconstruction

**目标 (Objective)**: 将“炼魄”后的逻辑喂给 Cursor，让其自动生成高质量、低成本、合规的 Agent 代码。
**原则 (Principle)**: 
1.  **工程优先 (Engineering First)**: 优先使用确定性工程手段（Python/Shell），而非不确定性大模型。
2.  **模块化 (Modularity)**: 强制分离 Core, Agents, Tools, Prompts。
3.  **成本意识 (Cost Awareness)**: 默认使用最便宜的模型完成任务，复杂任务才调用昂贵模型。

---

## 📜 `.cursorrules` 模板 (Copy this to your project root)

```markdown
# 炼魂协议 (Lianhun Protocol) - 2026 Agent 标准规则

## 1. 核心哲学 (Philosophy)
- **Cost Arbitrage**: 总是思考如何用更便宜的模型（如 Haiku/Flash）或纯代码（Regex/BeautifulSoup）替代昂贵的 GPT-4o 调用。
- **Deconstruction**: 将大任务拆解为小任务（Chain of Thought）。
- **Compliance**: 生成的所有内容必须包含 metadata 字段，标注 "AI-Generated"。

## 2. 代码风格 (Code Style)
- **Python**: 使用 Python 3.12+，强制类型提示 (Type Hints)，使用 `pydantic` 进行数据验证。
- **Async**: 默认使用 `async/await` 处理所有 I/O 操作。
- **Logging**: 使用 `structlog` 或 `loguru` 进行结构化日志记录，禁止使用 `print`。
- **Error Handling**: 必须包含 try-except 块，并定义具体的错误类型。

## 3. 架构规范 (Architecture)
- **State Management**: 使用 `src/core/state.py` 定义全局状态 (TypedDict/Pydantic)。
- **Workflow**: 使用 `langgraph` 定义状态机和节点流转。
- **Tools**: 所有工具必须定义为 `LangChain Tool` 或 `MCP Server`，包含详细的 description 和 args_schema。
- **Prompts**: 禁止在 Python 代码中硬编码 Prompt。必须存储在 `src/prompts/` 下的 YAML/Text 文件中。

## 4. 2026 特性 (2026 Features)
- **Self-Healing**: 在执行关键任务时，增加 "Reviewer" 节点，检查输出是否符合 JSON Schema，失败则自动重试。
- **Observability**: 集成 OpenTelemetry 或 LangSmith 追踪代码。
- **Security**: 永远不要在代码中打印 API Key 或敏感数据。使用环境变量管理配置。

## 5. 常用指令 (Common Commands)
- "复刻 (Possess)": 根据提供的描述，生成对应的 Agent 节点代码。
- "炼魄 (Refine)": 优化当前代码的性能和成本。
- "招魂 (Summon)": 根据用户提供的探测结果，生成对应的 System Prompt。

```

---

## 🏗️ 夺舍代码模板 (Possession Code Templates)

### 1. 标准 Agent 节点 (`src/agents/base.py`)

```python
from typing import Annotated, Literal, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], "The conversation history"]
    current_step: str
    scratchpad: dict

async def planner_node(state: AgentState):
    # 1. Load Prompt from YAML
    # 2. Call LLM (Cost-effective model)
    # 3. Return updated state with plan
    pass

async def executor_node(state: AgentState):
    # 1. Execute tools based on plan
    # 2. Return results
    pass

# Define the graph
workflow = StateGraph(AgentState)
workflow.add_node("planner", planner_node)
workflow.add_node("executor", executor_node)
workflow.set_entry_point("planner")
workflow.add_edge("planner", "executor")
workflow.add_edge("executor", END)

app = workflow.compile()
```

### 2. 标准工具定义 (`src/tools/base.py`)

```python
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class SearchInput(BaseModel):
    query: str = Field(description="The search query string")

@tool("web_search", args_schema=SearchInput)
async def web_search(query: str) -> str:
    """Search the web for information using a cost-effective API."""
    # Implementation here
    return f"Results for {query}"
```
