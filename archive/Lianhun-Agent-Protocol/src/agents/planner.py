from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import List
from pydantic import BaseModel, Field

from src.core.state import AgentState
from src.core.config import settings

class Plan(BaseModel):
    steps: List[str] = Field(description="List of steps to complete the user's request")

async def planner_node(state: AgentState):
    """
    The Brain: Deconstructs the user's request into actionable steps.
    Using 'Smart Model' for high-quality reasoning.
    """
    model = ChatOpenAI(model=settings.MODEL_SMART)
    parser = JsonOutputParser(pydantic_object=Plan)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert planner. Deconstruct the user's request into clear, actionable steps. Return a JSON object with a 'steps' key."),
        ("user", "{input}")
    ])
    
    chain = prompt | model | parser
    
    user_input = state["messages"][-1].content
    result = await chain.ainvoke({"input": user_input})
    
    return {"plan": result["steps"], "current_step": 0}

async def executor_node(state: AgentState):
    """
    The Hands: Executes the first step using a cost-effective model.
    Using 'Fast Model' for cost arbitrage.
    """
    model = ChatOpenAI(model=settings.MODEL_FAST)
    
    current_step_idx = state["current_step"]
    if current_step_idx >= len(state["plan"]):
        return {"final_answer": "Task completed."}
        
    step = state["plan"][current_step_idx]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Execute the following step concisely."),
        ("user", "{step}")
    ])
    
    response = await model.ainvoke({"step": step})
    
    return {
        "messages": [response],
        "current_step": current_step_idx + 1,
        "final_answer": response.content
    }
