from pydantic import HttpUrl
from youtube_mcp_tools import get_transcript


def test_get_transcript_valid(monkeypatch):
    # Mock YoutubeTool to avoid hitting real API
    class MockYoutubeTool:
        def __init__(self, url):
            self.url = url

        def fetch_transcript(self):
            return self

        def build_response(self):
            return {
                "success": True,
                "message": "Transcript fetched",
                "error": None,
                "transcript": "Sample transcript text",
                "url": str(self.url),
                "video_id": "abc123",
            }

    # Patch your YoutubeTool
    monkeypatch.setattr("server.http_server.YoutubeTool", MockYoutubeTool)

    url = HttpUrl("https://www.youtube.com/watch?v=abc123")
    result = get_transcript(url)

    assert result["success"] is True
    assert "Sample transcript text" in result["transcript"]
    assert result["video_id"] == "abc123"


def test_get_transcript_invalid(monkeypatch):
    # Mock YoutubeTool to avoid hitting real API
    class MockYoutubeTool:
        def __init__(self, url):
            self.url = url

        def fetch_transcript(self):
            return self

        def build_response(self):
            return {
                "success": False,
                "message": "Failed to fetch transcript",
                "error": "Invalid Video Id",
                "transcript": None,
                "url": str(self.url),
                "video_id": "invalid_video_id",
            }

    # Patch your YoutubeTool
    monkeypatch.setattr("server.http_server.YoutubeTool", MockYoutubeTool)

    url = HttpUrl("https://www.youtube.com/watch?v=invalid_video_id")
    result = get_transcript(url)

    assert result["success"] is False
    assert result["transcript"] is None
    assert result["video_id"] == "invalid_video_id"
