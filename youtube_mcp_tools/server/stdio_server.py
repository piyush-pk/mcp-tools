from typing import Literal
from .tools import mcp

def run_stdio(transport: Literal["stdio", "sse", "streamable-http"] = "stdio") -> None:
    mcp.run(transport=transport)
