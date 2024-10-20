"""Create page."""

import random
import time
from datetime import datetime

import reflex as rx
from PIL import Image

from aesop.backend.dboperations import add_story
from aesop.backend.generate_story import generate_story, generate_story_image
from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState
from aesop.models.story_card import StoryCard


class State(rx.State):
    form_data: dict = {}
    character_image = "https://ibb.co/kHB2Btr"  # Image.open("https://ibb.co/kHB2Btr")

    def handle_character_change(self, character: str):
        """Handle the character change."""
        self.character_image = self.character_list[character]
        self.form_data["character"] = character

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        if (
            not form_data.get("character")
            or not form_data.get("reading_level")
            or not form_data.get("description")
        ):
            rx.toast("Please fill in all fields!", status="warning")
            return

        self.form_data = form_data

        story = generate_story(
            form_data["character"], form_data["description"], form_data["reading_level"]
        )

        # image_description = [content.image_description for content in story.content]
        image_urls = generate_story_image(story.general_description)

        story_body = [content.story for content in story.content]
        story_id = random.randint(1, 10000)

        add_story(
            story=StoryCard(
                story_id=story_id,
                date=datetime.now(),
                author="test author",
                title=story.title,
                subject=story.subject,
                image_urls=image_urls,
                story_body=" ".join(story_body),
                description=form_data.get("description"),
                reading_level=form_data.get("reading_level"),
            )
        )

        return rx.redirect(f"/story/{story_id}")

    @rx.var
    def character_list(self) -> dict[str, str]:
        """Get the dictionary of characters and their image URLs."""
        return {
            "Thor": "https://ibb.co/mvYcNYf",
            "Batman": "https://ibb.co/GJZygyc",
            "Superman": "https://ibb.co/B25P8HZ",
            "Iron-Man": "https://ibb.co/KxYr0qt",
            "Spider-Man": "https://ibb.co/RNh2ZZw",
            "Wonder-Woman": "https://ibb.co/BgJHZgt",
            "Captain America": "https://ibb.co/cFbTWX7",
            "Make My Own": "https://ibb.co/kHB2Btr",
        }

    @rx.var
    def reading_level_list(self) -> list[str]:
        """Get the list of reading levels."""
        return ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]


def form():
    return rx.vstack(
        rx.heading("Let's Make Something Amazing!", size="xl"),
        rx.image(
            src=State.character_image,
            alt="Character",
            height="300px",
            object_fit="cover",
            border_radius="30px",
        ),
        rx.form(
            rx.vstack(
                rx.select(
                    State.character_list.keys(),
                    placeholder="Select main character",
                    name="character",
                    width="100%",
                    on_change=State.handle_character_change,
                ),
                rx.cond(
                    State.form_data["character"] == "Make My Own",
                    rx.text_field(
                        placeholder="Who is your character?",
                        name="character",
                        width="100%",
                    ),
                ),
                rx.select(
                    State.reading_level_list,
                    placeholder="Select reading level",
                    name="reading_level",
                    width="100%",
                ),
                rx.text_area(
                    placeholder="Describe what you want to learn from the story!",
                    name="description",
                    width="100%",
                    height="150px",
                    padding="1em 0.5em",
                ),
                rx.button(
                    "Create My Story!",
                    type="submit",
                    width="100%",
                    _hover={
                        "cursor": "pointer",
                    },
                ),
                spacing="3",
            ),
            on_submit=State.handle_submit,
        ),
        width="100%",
        padding="1em",
        max_width="550px",
        margin="0 auto",
        justify="center",
        align="center",
    )


@rx.page(on_load=BaseState.get_configs)
def create_page() -> rx.Component:
    return rx.container(
        header(redirect_to_signin=True),
        form(),
        footer(),
        padding="0",
    )
