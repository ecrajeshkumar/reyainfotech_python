import asyncio

from client import *

async def main():

    client = await connect_to_server()

    tools = await discover_tools(client)

    print("Available Tools")
    print("----------------")

    for tool in tools:
        print(tool.name)
    print("----------------")

    tool_descriptions = build_tool_descriptions(tools)
    for tool_name, description in tool_descriptions.items():
        print(f"{tool_name}: {description}")

    result = await execute_tools(client, "roll_dice")
    print("Dice Result:", result.content[0].text)

    await disconnect(client)

asyncio.run(main())
