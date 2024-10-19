from datetime import datetime
from typing import List

import reflex
from sqlalchemy import ARRAY, Column, String


class StoryCard(reflex.Model, table=True):
    title: str
    description: str
    date: datetime
    author: str
    subject: str
    reading_level: str
    image_urls: str
    story_id: str
    # jsonstr
    story_body: str
