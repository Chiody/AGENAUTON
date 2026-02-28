import asyncio
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from src.core.state import AgentState
from src.agents.planner import planner_node, executor_node
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def main():
    print("🔮 Lianhun Agent Protocol Initialized...")
    
    # 1. Define the Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add Nodes
    workflow.add_node("planner", planner_node)
    workflow.add_node("executor", executor_node)
    
    # 3. Add Edges
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", END)
    
    # 4. Compile
    app = workflow.compile()
    
    # 5. Execute
    user_input = input("Enter your command (Summon/Refine/Possess): ")
    inputs = {"messages": [HumanMessage(content=user_input)], "current_step": 0}
    
    async for output in app.astream(inputs):
        for key, value in output.items():
            print(f"Node '{key}':")
            print(value)
            print("---")

if __name__ == "__main__":
    asyncio.run(main())
