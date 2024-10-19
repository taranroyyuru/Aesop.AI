import base64
from io import BytesIO

import reflex as rx
from PIL import Image

from aesop.backend.dboperations import get_story
from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState
from aesop.models.story_card import StoryCard


def base64_to_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    return image_bytes


def create_image_from_bytes(image_bytes):
    # Create a BytesIO object to handle the image data
    image_stream = BytesIO(image_bytes)

    # Open the image using Pillow (PIL)
    image = Image.open(image_stream)
    return image


class State(rx.State):
    story_data: StoryCard = None

    @rx.var
    def curr_story_data(self) -> StoryCard:
        """
        The current story data to be displayed.

        This variable is triggered when the page loads and when the story_id parameter in the URL changes.
        It fetches the story data from the database and stores it in the state.
        """
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        return self.story_data

    @rx.var
    def story_title(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return self.story_data.title
        return None

    @rx.var
    def story_subject(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return self.story_data.subject
        return None

    @rx.var
    def story_reading_level(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return self.story_data.reading_level
        return None

    @rx.var
    def story_image_urls(self) -> list[str]:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return str(self.story_data.image_urls).split("|")
        return None

    @rx.var
    def story_body(self) -> list[str]:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))

        if self.story_data:
            return str(self.story_data.story_body).split("|")
        return None

    def curr_data(self):
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))


def img64_to_color(img_url: str):
    # Render an image component
    return rx.image(src=img_url, width="100px", height="100px")  # Adjust size as needed


def story() -> rx.Component:
    return rx.vstack(
        rx.heading(State.story_title, size="xl", padding="1em"),
        rx.hstack(
            rx.heading(State.story_subject, size="md"),
            rx.heading(State.story_reading_level, size="md"),
        ),
        rx.center(
            rx.grid(
                State.story_body,
                style={
                    "gridTemplateColumns": "1fr",
                    "gap": "1em",
                },
            ),
            padding="2em",
            background_color="#f0f0f0",
        ),
        rx.cond(
            (State.story_image_urls is not None),
            rx.vstack(
                rx.foreach(
                    State.story_image_urls,
                    lambda row: rx.hstack(
                        rx.foreach(
                            row,
                            rx.image,
                        )
                    ),
                ),
            ),
        ),
    )


@rx.page(on_load=State.curr_data)
def story_page() -> rx.Component:
    return rx.container(
        header(),
        story(),
        footer(),
        padding="0",
    )
