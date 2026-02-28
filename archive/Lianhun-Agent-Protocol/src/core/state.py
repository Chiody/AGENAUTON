from typing import Annotated, TypedDict, List
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    """
    The standardized state for a Lianhun Agent.
    Every node in the graph will receive and return this state.
    """
    messages: Annotated[List[BaseMessage], operator.add]
    plan: List[str]
    current_step: int
    final_answer: str
