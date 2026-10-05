from config import *
import json

def review(task, code):
    prompt = f"""
You are a code reviewer agent. Review the following code based on the task and provide feedback.
Task: {task}:
Solution:{code}

Check:
1. Correctness
2. programming language syntax
3. Logic
4. Missing issues
5. Possible improvements

Return ONLY valid JSON.

Use exactly this format:

{{
    "status": "approved",
    "feedback": "The solution is correct."
}}

OR:

{{
    "status": "needs_revision",
    "feedback": "Explain what needs to be changed."
}}

Use "approved" only when the solution
is acceptable.

Use "needs_revision" when the solution
requires a correction.
"""
    response = client.chat.completions.create(
        model = model_1,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

    return json.loads(result)