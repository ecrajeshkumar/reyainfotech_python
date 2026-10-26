'''
Let's Create Our Own StateGraph
Suppose LangGraph module didn't exist in python package.
'''

class StateGraph:

    def __init__(self, state_schema):
        self.state_schema = state_schema
        self.nodes = {}
        self.edges = []

    def add_node(self, name, func):
        self.nodes[name] = func

    def add_edge(self, from_node, to_node):
        if from_node not in self.nodes or to_node not in self.nodes:
            raise ValueError("Both nodes must be added before creating an edge.")
        # For simplicity, we won't store edges explicitly in this example.  



from typing import TypedDict
# as the shared memory/data structure
class AgentState(TypedDict):
    user_request: str
    current_step: int
    max_steps: int
    actions: list
    observations: list
    finished: bool
    final_answer: str

'''
Every node receives AgentState
Every node returns AgentState
'''
def planner_node(state: AgentState):

    state["actions"].append("Plan created")

    return state


def llm_node(state: AgentState):

    state["final_answer"] = "8"

    return state

# as the workflow engine that moves this state through multiple agents like planner_node and llm_node and so on, until the final answer is produced.
# Every agent receives the same AgentState, updates it, and passes it to the next agent. This is the core idea behind LangGraph-based multi-agent systems.
# initialize the state graph class with the AgentState schema
workflow = StateGraph(AgentState)  

# Register Nodes
workflow.add_node("planner", planner_node)
workflow.add_node("llm", llm_node)

# Create Edges
workflow.add_edge("planner", "llm")

# Compile Graph
app = workflow.compile()

# Run Graph
result = app.invoke({
    "user_request": "Add 5 and 3",
    "current_step": 0,
    "max_steps": 5,
    "actions": [],
    "observations": [],
    "finished": False,
    "final_answer": ""
})

print(result)

print(workflow.state_schema)  # OP: <class '__main__.AgentState'

'''
OP:
{
    'user_request': 'Add 5 and 3',
    'current_step': 0,
    'max_steps': 5,
    'actions': ['Plan created'],
    'observations': [],
    'finished': False,
    'final_answer': '8'
}
'''

