from typing import Literal
from .tools import mcp

def run_http_server(transport: Literal["stdio", "sse", "streamable-http"] = "streamable-http") -> None:
    mcp.run(transport=transport)
