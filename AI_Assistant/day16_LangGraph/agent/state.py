from typing import TypedDict

# Create state for the agent to keep track of its progress and actions 

class AgentState(TypedDict):
    user_request: str
    current_step: int
    max_steps: int
    actions: list
    observations: list
    finished: bool
    final_answer: str

