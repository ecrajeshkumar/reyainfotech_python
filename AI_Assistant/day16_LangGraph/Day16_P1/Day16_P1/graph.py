from langgraph.graph import (
    StateGraph,
    START,
    END
)
# StateGraph is a class that represents a directed graph where nodes are states and edges are transitions between states. 
# It is used to model the flow of an agent's decision-making process.
# START and END are constants that represent the starting and ending points/nodes of the graph, respectively.

# from agent.planner import planner
import agent.planner as agent_planner
from agent.state import AgentState

# Create and return a planner node that can be used in the state graph. The planner node is responsible for determining the next action based on the current state and available tools.
# node means just 
def create_planner_node(tools):
    # The planner_node function is a node in the state graph that represents the planning step of the agent.
    # It takes the current state of the agent as input, calls the planner function to determine the next action, 
    # and returns an updated state dictionary that includes the selected action, observations, current step, 
    # and whether the agent has finished its task. This node is used in the state graph to model the planning phase of the agent's decision-making process.
    def planner_node(state: AgentState):

        action = agent_planner.planner(state,tools)

        print("\nPlanner Selected:")
        print(action)

        return {
            "actions": state["actions"],
            "observations": state["observations"],
            "current_step": state["current_step"],
            "finished": action == "FINISH",
            "final_answer": state["final_answer"]
        } 

    return planner_node  # Effectively,  it returns a function that can be registered with LangGraph which is used as a node in the state graph, allowing the agent to make decisions based on its current state and available tools.

'''
def planner_node(state: AgentState):
    print(state["user_request"])

    The parameter state should be a dictionary having the structure defined in AgentState.
    state = {
        "user_request": "What is 5 + 3?",
        "current_step": 1,
        "max_steps": 5,
        "actions": [],
        "observations": [],
        "finished": False,
        "final_answer": ""
    }
    planner_node(state)
'''

def build_graph(tools):

    builder = StateGraph(AgentState)
    '''
    StateGraph is a class, not a method. StateGraph(AgentState) invokes the class constructor (__init__) and creates an instance of the graph using AgentState 
    as the state schema shared between all nodes in the workflow.

    StateGraph is a class that represents a directed graph where nodes are states and edges are transitions between states.
    Every agent receives the same AgentState, updates it, and passes it to the next agent. This is the core idea behind LangGraph-based multi-agent systems.
    
    '''
    planner_node = create_planner_node(tools)

    builder.add_node(
        "planner",
        planner_node
    )

    builder.add_edge(
        START,
        "planner"
    )

    builder.add_edge(
        "planner",
        END
    )

    return builder.compile()

