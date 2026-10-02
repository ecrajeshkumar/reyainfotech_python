import asyncio

# from mcp_client import (
#     connect,
#     disconnect,
#     discover_tools
# )
import mcp_client as clnt
# from planner import planner
import planner as plan
# from executor import execute_action
import executor as exut
# from loop import run_agent_loop
import loop as lp
# from answer import format_answer
import answer as ans
# from memory import create_database
import memory as mem

async def main():
    mem.create_database()
    client = await clnt.connect()

    tools = await clnt.discover_tools(
        client
    )

    print("\nAvailable Tools")
    print("----------------")

    for tool in tools:
        print(tool.name)

    user_request = input(
        "\nUser : "
    )

    state = await lp.run_agent_loop(
        user_request,
        plan.planner,
        exut.execute_action,
        ans.format_answer,
        tools,
        client
    )

    print("\nFinal Answer")
    print("------------")

    print(
        state["final_answer"]
    )

    await clnt.disconnect(client)


if __name__ == "__main__":
    asyncio.run(main())

