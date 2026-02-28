# Cursor Rules for Agenauton

# Cursor IDE 集成规则

---

## How to Use / 使用方法

将下方的规则内容复制到你项目根目录的 `.cursorrules` 文件中：

```bash
# 在你的项目根目录执行
cp /path/to/Agenauton/cursor_rules/agenauton.cursorrules .cursorrules
```

或者直接复制以下内容：

---

## The Rules / 规则内容

```
# Agenauton Agentic Standard - Cursor Rules v1.0

You are building an AI Agent following the Agenauton 26-Dimension Agentic Standard.
Every architectural decision must be traceable to one or more of the 26 dimensions.

## Architecture Principles

1. SEPARATION OF CONCERNS: Each dimension maps to a distinct module/package.
   Never mix safety logic (Layer 5) with core logic (Layer 3).

2. SCHEMA-FIRST: Define all data models (Pydantic) before writing any logic.
   Internal communication between agents MUST use typed schemas.

3. STRONG SKELETON, CHEAP FLESH: The architecture (skeleton) is designed by
   the strongest model. Implementation details (flesh) can be filled by any model.
   Never modify the skeleton without explicit approval.

4. DEFENSIVE BY DEFAULT: Every agent must have:
   - Input validation
   - Output self-check (Dimension 16)
   - Hallucination guard (Dimension 17)
   - Trust boundary awareness (Dimension 19)

5. OBSERVABLE: Every agent action must emit telemetry (Dimension 20).
   Log inputs, outputs, tool calls, and confidence scores.

## Code Organization

Follow this directory structure:

```
project/
├── main.py              # Entry point
├── config.py            # All configuration (Dim 01, 06)
├── models/              # Pydantic schemas (Dim 04)
├── agents/              # Agent definitions (Dim 08, 09)
├── tools/               # Tool interfaces (Dim 10)
├── retrieval/           # RAG pipeline (Dim 11)
├── prompts/             # System prompts (Dim 12, 14)
├── safety/              # Moderation & guards (Dim 16-19)
├── evolution/           # Telemetry & drift (Dim 20-22)
└── tests/               # Test coverage
```

## Naming Conventions

- Agent classes: `{Role}Agent` (e.g., PlannerAgent, ReviewerAgent)
- Tool functions: `tool_{action}` (e.g., tool_search, tool_calculate)
- Schema models: `{Entity}Schema` (e.g., TaskSchema, ResponseSchema)
- Prompt templates: `PROMPT_{ROLE}_{PURPOSE}` (e.g., PROMPT_PLANNER_DECOMPOSE)

## When Making Changes

Before modifying any file, identify which Agenauton dimension(s) it relates to.
If a change affects the architecture topology (Dim 08) or agent division (Dim 09),
flag it as a SKELETON CHANGE and request human review.

## Quality Gates

Every PR must pass:
1. Schema validation — all data flows use typed models
2. Safety check — no unguarded LLM outputs reach the user
3. Telemetry coverage — all agent actions are logged
4. Dimension traceability — every module maps to at least one dimension
```

---

## Advanced: Per-Dimension Rules / 进阶：按维度细化规则

如果你想更精细地控制 Cursor 的行为，可以在 `.cursorrules` 中添加以下维度特定规则：

```
## Dimension-Specific Rules

### Dim 05 (State & Memory)
- Always use a state management class, never raw dictionaries
- Session state must be serializable to JSON
- Long-term memory operations must be async

### Dim 11 (RAG)
- Always implement reranking after initial retrieval
- Chunk size must be configurable via config.py
- Include source attribution in every RAG response

### Dim 17 (Hallucination)
- Every factual claim must be traceable to a source
- If confidence < 0.7, prepend response with uncertainty marker
- Never generate URLs, file paths, or citations without verification

### Dim 18 (Safety)
- Input sanitization before every LLM call
- Output moderation after every LLM response
- Prompt injection detection on all user inputs
```

---

*→ Back to [Soul Forging](./README.md)*
