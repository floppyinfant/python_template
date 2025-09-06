"""
https://github.com/modelcontextprotocol/servers
https://github.com/modelcontextprotocol/python-sdk
https://huggingface.co/learn/mcp-course/unit0/introduction

BlenderMCP
https://github.com/ahujasid/blender-mcp
https://blender-mcp.com/

OpenWebUI + mcpo
https://docs.openwebui.com/openapi-servers/mcp/

uv add "mcp[cli]"
uv run mcp

uv run mcp dev server.py
uv run mcp install server.py
"""

# ----------------------------------------------------------------------------

"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."
