from datetime import datetime

from pydantic import BaseModel


class StoryCard(BaseModel):
    title: str
    description: str
    date: datetime
    author: str
    subject: str
    reading_level: str
    image_url: str
    story_url: str
