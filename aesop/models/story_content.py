import reflex as rf


class StoryContent(rf.Model, table=True):
    title: str
    story_id: str
    body: str
