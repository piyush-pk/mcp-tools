from ..core import YoutubeTool, YoutubeResponse
from mcp.server.fastmcp import FastMCP
from pydantic import HttpUrl, Field
import os

host = os.getenv("MCP_HOST", "0.0.0.0")  # default 0.0.0.0
port = int(os.getenv("MCP_PORT", 8000))  # default 8000

mcp = FastMCP("PK TOOLS", host=host, port=port)


@mcp.tool(
    name="get_transcript",
    title="Get Youtube Transcript",
    description="Fetch Youtube Video Transcript",
    structured_output=True
)
def get_transcript(url: HttpUrl = Field(None, description="Url of Youtube Video",)) -> YoutubeResponse:
    """
    Fetch or Get Youtube video transcript.
    args:
        - url: HttpUrl = Youtube video Url
    returns
        - JSON
            {{
                "success": boolean,
                "message": str,
                "error": str,
                "transcript": str,
                "url": str,
                "video_id": str
            }}
    """
    return YoutubeTool(url=url).fetch_transcript().build_response()