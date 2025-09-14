from pydantic import BaseModel, Field
from typing import Optional


class Response(BaseModel):
    success: bool = Field(
        default=False, description="Holds weather operation got success or not."
    )
    message: Optional[str] = Field(
        default=None, description="Holds the response message"
    )
    error: Optional[str] = Field(default=None, description="Holds the error message.")
