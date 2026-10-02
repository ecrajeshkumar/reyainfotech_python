
state = {
        "user_request": user_request,
        "tasks": [],
        "current_task": None,
        "current_step": 0,
        "max_steps": max_steps,
        "actions": [],
        "observations": [],
        "results": [],
        "finished": False,
        "final_answer": ""
        }


state["tasks"] = {
                    "task": task,
                    "status": "pending"
                }

if not state["tasks"]:
        return False
