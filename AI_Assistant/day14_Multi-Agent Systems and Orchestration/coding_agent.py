from config import *


def write_code(task, research, feedback = ""):
    prompt = f"""
You are a coding agent. Write or revise code based on
the task and research.
Your task is to write code for the following Task: {task}

Research findings: {research}

Feedback: {feedback}

Please write clean, efficient, and well-documented code that addresses the task and incorporates the research findings and feedback. 
Your response should be a valid code snippet.
If reviewer feedback is provided,
correct the identified problems.

Return:

1. Short explanation
2. Complete code in language as user asked for
"""
    response = client.chat.completions.create(
        model = model_1,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content
