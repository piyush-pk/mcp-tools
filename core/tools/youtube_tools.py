from pydantic import PrivateAttr
from youtube_transcript_api import YouTubeTranscriptApi

from core import YoutubeResponse


class YoutubeTool(YoutubeResponse):
    __yt: YouTubeTranscriptApi = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self.__yt = YouTubeTranscriptApi()
        self._parse_url()

    def _parse_url(self) -> None:
        from urllib.parse import urlparse, parse_qs

        # Convert the HttpUrl object to a string before parsing
        parsed_url = urlparse(str(self.url))
        video_id = None

        # Handle short youtu.be links
        if "youtu.be" in parsed_url.netloc:
            video_id = parsed_url.path.strip("/")

        # Handle regular youtube.com links
        elif "youtube.com" in parsed_url.netloc:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]

        self.video_id = video_id

    def fetch_transcript(self):
        try:
            transcript_list = self.__yt.list(video_id=self.video_id)
            fetched_transcript = transcript_list.find_generated_transcript(
                language_codes=self.language_codes  # only return one language transcrip even if multiple available and priority will be for first match in language codes
            ).fetch()

            # create a unified string with all text that we get as transcript
            self.transcript = "\n".join(item.text for item in fetched_transcript)
            self.success = True
            self.message = "Transcript Fetched Successfully."
            return self
        except Exception:
            self.success = False
            self.error = f"Could not fetch transcript for {self.video_id}: Please check youtube video link."
            return self

    def build_response(self):
        return YoutubeResponse(
            success=self.success,
            url=self.url,
            video_id=self.video_id,
            error=self.error,
            message=self.message,
            transcript=self.transcript,
        ).model_dump_json()
