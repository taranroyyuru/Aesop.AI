from datetime import datetime


import reflex
from sqlalchemy import ARRAY, String,Column
class StoryCard(reflex.Model, table=True):
    title: str
    description: str
    date: datetime
    author: str
    subject: str
    reading_level: str
    image_urls:Column(ARRAY(String))
    story_id:str
    # jsonstr
    story_body:str
