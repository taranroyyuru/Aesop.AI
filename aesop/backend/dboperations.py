import json
from datetime import datetime

import reflex as rx
import sqlalchemy

from aesop.models.story_card import StoryCard


# gets story as dict
def add_story(story):
    with rx.session() as session:
        session.add(story)
        session.commit()


def row_to_story(row):
    story = dict(row)
    print(story)
    story["story_body"] = json.loads(story["story_body"])
    return story


# TODO: account for Array refactor
def get_story(id):
    with rx.session() as session:
        res = session.query(StoryCard).filter(StoryCard.story_id == id).first()

        # story = row_to_story(res)
        return res


# TODO: account for Array refactor
def get_latest(n: int):
    with rx.session() as session:
        res = session.query(StoryCard).order_by(StoryCard.date).limit(n)
        return list(map(row_to_story, res))


def get_count():
    with rx.session() as session:
        return session.query(StoryCard).count()
