
from fastmcp import Client

async def connect_to_server():
    """Connect to the FastMCP server and call its tools."""
    '''
    The Client class is responsible for MCP protocol logic, while the Transport handles connection establishment 
    and management. Client provides methods for working with resources, prompts, tools and other MCP capabilities.
    '''
    client = Client("server.py")
    await client.__aenter__()
    print("Connected to MCP Server")
    return client

async def discover_tools(client):
    """
    Retrieve all tools from the server
    """
    tools = await client.list_tools()
    return tools

async def execute_tools(client, tool_name, arguments = None):
    """
    Execute a tool on the server.
    """
    if arguments is None:
        arguments = {}
    result = await client.call_tool(tool_name, arguments)
    return result

async def disconnect(client):
    """
    Close the mCP connection
    """
    await client.__aexit__(None,None,None)

