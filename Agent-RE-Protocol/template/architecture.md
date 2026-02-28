# Standard Agent Architecture (2026 Edition)

This template defines the standard folder structure and component organization for a production-ready AI Agent project in 2026.

## 1. Directory Structure

```
my-agent-project/
├── .cursorrules          # AI Coding Assistant Rules (Cost/Quality Optimization)
├── pyproject.toml        # Dependency Management (Poetry/uv)
├── README.md             # Project Documentation
├── src/
│   ├── __init__.py
│   ├── core/             # Core Framework & Configuration
│   │   ├── config.py     # Environment Variables & Settings
│   │   ├── state.py      # Global State Definition (Pydantic Models)
│   │   ├── graph.py      # LangGraph/Workflow Definition
│   │   └── llm.py        # LLM Provider Setup (OpenAI/Anthropic/Local)
│   ├── agents/           # Sub-Agents (The "Brains")
│   │   ├── planner.py    # High-level Planning Agent
│   │   ├── executor.py   # Task Execution Agent
│   │   ├── reviewer.py   # Quality Assurance Agent
│   │   └── router.py     # Conditional Routing Logic
│   ├── tools/            # External Capabilities (The "Hands")
│   │   ├── web_search.py # Internet Access
│   │   ├── file_ops.py   # File System Operations
│   │   └── api_client.py # Custom API Integrations
│   ├── prompts/          # Prompt Engineering Assets (The "Soul")
│   │   ├── system.yaml   # System Prompts for each Agent
│   │   └── few_shot.json # Examples for In-Context Learning
│   └── utils/            # Helper Functions
│       ├── logger.py     # Structured Logging
│       └── parser.py     # Output Parsing & Validation
├── tests/                # Testing Strategy
│   ├── unit/             # Component Tests
│   ├── integration/      # Workflow Tests
│   └── adversarial/      # Red-teaming / Safety Tests
└── scripts/              # Deployment & Ops
    ├── deploy.sh         # CI/CD Pipeline
    └── evaluate.py       # Performance Evaluation Script
```

## 2. Key Components

### 2.1 State Management (`src/core/state.py`)
- Define the `AgentState` using `TypedDict` or `Pydantic`.
- Must include: `messages`, `plan`, `current_step`, `scratchpad`.

### 2.2 Workflow Definition (`src/core/graph.py`)
- Use `LangGraph` (or similar state machine library) to define nodes and edges.
- Define conditional edges for dynamic routing (e.g., `should_continue`, `route_to_tool`).

### 2.3 Prompt Management (`src/prompts/`)
- Store prompts in external files (YAML/Text) for easy editing and version control.
- Separation of Code and Logic.

### 2.4 Tool Abstraction (`src/tools/`)
- Tools should be stateless functions or classes with standardized `run` methods.
- Use `pydantic` for argument validation.

## 3. 2026 Standardization Checklist

- [ ] **Compliance**: Add watermark/metadata to all AI-generated outputs.
- [ ] **Cost Control**: Use smaller models (e.g., Haiku/Flash) for simple tasks, larger models (Opus/Pro) only for complex reasoning.
- [ ] **Observability**: Implement tracing (LangSmith/Arize) for all agent steps.
- [ ] **Human-in-the-loop**: Add breakpoints for critical actions (e.g., modifying files, spending money).
