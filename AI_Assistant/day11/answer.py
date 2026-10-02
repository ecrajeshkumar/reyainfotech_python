
from config import *

def format_answer(state):

    prompt = f"""
The user asked:

{state["user_request"]}

Relevant previous memories:
{state["memories"]}

Tasks:
{state["tasks"]}

Actions:
{state["actions"]}

Observations:
{state["observations"]}

Intermediate Results:
{state["results"]}

Give the user a natural and concise answer.
Use relevant previous memories
when they help answer the user's question.


Do not mention:
- planner
- agent loop
- MCP
- internal state
- tools
- internal reasoning
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

    return response.choices[0].message.content.strip()

