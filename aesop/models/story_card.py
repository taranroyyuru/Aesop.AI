from datetime import datetime
from typing import List

import reflex
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import ARRAY, String, Column 
class StoryCard(reflex.Model, table=True):
    title: str
    description: str
    date: datetime
    author: str
    subject: str
    reading_level: str
    image_urls:list[str] = ARRAY[String]
    story_id: str = Column(String)
    # jsonstr
    story_body: str = ARRAY[String]
