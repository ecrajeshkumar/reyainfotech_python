from fastmcp import Client

async def connect():
    """
    This function establishes a connection to the MCP Server.
    """
    client = Client(mcp_server.py)
    await client.__aenter__()
    print("MCP Server connected ...")
    return client

async def disconnect(client):
    """
    This function establishes a disconnection to the MCP Server.
    """
    await client.__aexit__(None, None, None)

async def discover_tools(client):
    """
    This function retrive all tools from server.
    """
    tools = await client.list_tools()
    return tools

async def execute_tool(client, tool_name, arguments = None):
    """
    This function execute a specific tool
    """
    if arguments is None:
        arguments = {}
    result = await client.call_tool(tool_name, arguments)
    return result

# Print the docstring
# print(connect.__doc__)
# print(disconnect.__doc__)
# print(discover_tools.__doc__)
# print(excute_tool.__doc__)

