from config import *

from research_agent import research
from coding_agent import write_code
from reviewer_agent import review
from state import create_state

MAX_REVISIONS = 3

def choose_worker(state):

    prompt = f"""
You are the manager of a multi-agent system. The current state of the task is as follows:
Your task is to decide which worker should be assigned next based on the current state of the task.

Original Task: {state['task']}
Research: {state['research']}
Code: {state['code']}
Review: {state['review']}
History: {state['history']}
Revision Count: {state['revision_count']}
Maximum Revisions: {MAX_REVISIONS}

Available Workers:
1. Research Agent: Responsible for conducting research and gathering information.
2. Coding Agent: Responsible for writing code based on the research findings.
3. Reviewer Agent: Responsible for reviewing the code and providing feedback.
4. finish: Indicates that all tasks are completed.

Decision rules:
- If Research is empty, choose research.

- If Research exists and Code is empty, choose coding.

- If a Review exists with status
  "needs_revision" and the Revision count is below the maximum, choose coding.

- If Code exists and there is no Review, choose review.

- If the previous review requested
  revision and new code has been generated,  choose review again.

- If the latest Review status is
  "approved", choose finish.

- If the maximum revision count has
  been reached, choose finish.

Return ONLY one word:

research
coding
review
finish
"""
    response = client.chat.completions.create(
        model = model_1,
        messages = [{"role": "user", "content": prompt}]
        )

    return response.choices[0].message.content.strip().lower()


def run_manager(task):
    # Initialize state
    state = create_state(task)

    while True:

        worker = choose_worker(state)
        print(f"Manager assigned task to: {worker}")

        if worker == "research":
            state["research"] = research(state["task"])
            state["history"].append("Research completed.")
        elif worker == "coding":
            if (state["review"] and state["revision_count"] >= MAX_REVISIONS):
                print("Maximum revisions reached.")
                break
            feedback = ""
            if state["review"]:
                feedback = state["review"].get("feedback","")
            state["revision_count"] += 1
            state["code"] = write_code(state["task"], state["research"],feedback)
            state["review"] = ""
            state["history"].append("coding")
        elif worker == "review":
            state["review"] = review(state["task"], state["code"])
            state["history"].append("review")
        elif worker == "finish":
            break
        else:
            raise ValueError(f"Unknown worker: {worker}")
    return state
