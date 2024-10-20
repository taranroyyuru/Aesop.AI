from datetime import datetime
from typing import List

import reflex

from sqlalchemy import ARRAY, String, Column 
class StoryCard(reflex.Model, table=True):
    title: str
    description: str
    date: datetime
    author: str
    subject: str
    reading_level: str
    image_urls:List[str] = ARRAY
    story_id: str = Column(String)
    # jsonstr
    story_body:List[str] = ARRAY
