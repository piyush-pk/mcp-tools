from pydantic import Field, HttpUrl
from typing import List, Optional
from .response_model import Response


# class YouTubeVideoInfo(BaseModel):
#     title: str = Field(..., description="The title of the YouTube video")
#     description: Optional[str] = Field(
#         None, description="The description of the YouTube video"
#     )
#     views: int = Field(..., description="The number of views on the video")
#     length: int = Field(..., description="The length of the video in seconds")
#     author: str = Field(..., description="The channel name or author of the video")
#     channel: str = Field(..., description="Channel name of the uploader")


class YoutubeResponse(Response):
    url: Optional[HttpUrl] = Field(default=None, description="Hold Youtube video url.")
    transcript: Optional[str] = Field(
        default=None, description="Holds Transcript of the Youtube video"
    )
    video_id: Optional[str] = Field(
        default=None, description="Holds youtube video unique video id."
    )
    language_codes: List[str] = Field(
        default=["en", "hi"],
        description="Holds youtube video transcript language codes.",
    )
