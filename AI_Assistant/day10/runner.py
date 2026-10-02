from config import *
import asyncio

# from mcp_client import *
import mcp_client as clnt
# from mcp_client import (connect, disconnect, discover_tools)
from loop import run_agent_loop

async def main():
    client = await clnt.connect()
    tools = await clnt.discover_tools(client)

    # print("\nAvailable Tools")
    # print("----------------")
    # for tool in tools:
    #     print(tool.name)

    user_request = input("\nUser : ")

    state = await run_agent_loop(user_request, tools, client)
    print(state["final_answer"])
    await clnt.disconnect(client)

    if __name__ == "__main__":
        asyncio.run(main())
