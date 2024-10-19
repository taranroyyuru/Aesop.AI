# placeholder for pydantic model that holds all story content
from pydantic import BaseModel
import reflex as rf
from sqlalchemy import Column, JSON
class StoryContent(rf.Model, table=True):
    title: str
    story_id:str
    body:str