def create_state(task):
    return {
        "task": task,
        "research": None,
        "code": None,
        "review": None,
        "history": [],
        "revision_count": 0
    }