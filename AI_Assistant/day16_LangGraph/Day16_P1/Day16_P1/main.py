import asyncio

# from agent.mcp_client import (
#     connect,
#     disconnect,
#     discover_tools
# )
# import agent.mcp_client as client
import agent.mcp_client as mcp_client

# from graph import build_graph
import graph as graph_module

async def main():

    client = await mcp_client.connect()

    tools = await mcp_client.discover_tools(client)

    print("\nAvailable Tools")
    print("----------------")

    for tool in tools:
        print(tool.name)

    graph = graph_module.build_graph(tools)

    user_request = input("\nUser : ")

    initial_state = {
        "user_request": user_request,
        "current_step": 0,
        "max_steps": 5,
        "actions": [],
        "observations": [],
        "finished": False,
        "final_answer": ""
    }

    result = graph.invoke(
        initial_state
    )

    print("\nFinal State")
    print("-----------")
    print(result)

    await mcp_client.disconnect(client)


if __name__ == "__main__":
    asyncio.run(main())
