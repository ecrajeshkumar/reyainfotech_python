# runner.py

import asyncio

from config import  *

from client import *
from planner import planner
from executor import execute_action
from loop import run_agent_loop


def format_answer(state):

    prompt = f"""
The user asked:

{state["user_request"]}

Actions performed:

{state["actions"]}

Observations:

{state["observations"]}

Answer the user naturally.

Do not mention internal planning.
Do not mention state.
Do not mention tools.
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


async def main():

    client = await connect()

    tools = await discover_tools(client)

    # print()
    # print("Available Tools")
    # print("----------------")

    # for tool in tools:
    #     print(tool.name)

    user_request = input("\nUser : ")

    state = await run_agent_loop(user_request, planner, execute_action, format_answer, tools, client)
    # print()
    print("Final Answer:")
    print(state["final_answer"])
    await disconnect(client)


if __name__ == "__main__":
    asyncio.run(main())
