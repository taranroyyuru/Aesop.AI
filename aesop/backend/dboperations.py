import reflex as rx
from aesop.models.story_card import StoryCard
from datetime import datetime
import sqlalchemy
from sqlalchemy import Array, String, Column
import json

# gets story as dict
def add_story(story):
	with rx.session() as session:
		session.add(
			StoryCard(title=story['title'],
    description=story['description'],
    date=datetime.strptime(story['date'], "%Y-%m-%d"),
    author = story['author'],
    subject = story['subject'],

    reading_level =  story['reading_level'],
    image_urls = story['image_urls'],
    story_id = story['story_id'],
	story_body = story['story_body']
		)
	)
	
		session.commit()
	
def row_to_story(row):
	story = dict(row)
	print(story)
	story['story_body'] = json.loads(story['story_body'])['']
	return story

# TODO: account for Array refactor
def get_story(id):
	with rx.session() as session:
		res = session.query(StoryCard)\
				.filter(StoryCard.story_id == id).first()
		
		story = row_to_story(res)
		return story

# TODO: account for Array refactor
def get_latest(n:int):
	with rx.session() as session:
		res = session.query(StoryCard)\
		.order_by(StoryCard.date).limit(n)
		return list(map(row_to_story, res))

def get_count():
	with rx.session() as session:
		return session.query(StoryCard).count()