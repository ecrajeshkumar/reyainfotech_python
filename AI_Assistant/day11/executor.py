# from mcp_client import execute_tool
import mcp_client as client

async def execute_action(
    action,
    state,
    client
):

    result = await client.execute_tool(
        client,
        action
    )

    if hasattr(result, "content"):

        if result.content:
            return result.content[0].text

    return str(result)

