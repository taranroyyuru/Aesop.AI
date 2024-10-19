"""Home page."""

# TODO: actually fetch story data and fix their urls

from datetime import datetime

import reflex as rx
from PIL import Image

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState
from aesop.models.story_card import StoryCard


def story_card_to_dict(story_card: StoryCard) -> dict:
    return {
        "title": story_card.title,
        "description": story_card.description,
        "date": story_card.date.strftime("%B %d, %Y"),
        "author": story_card.author,
        "subject": story_card.subject,
        "reading_level": story_card.reading_level,
        "image_url": story_card.image_url,
        "story_url": story_card.story_url,
    }


class State(rx.State):
    @rx.var
    def latest_stories(self) -> list[dict]:
        return [
            story_card_to_dict(
                StoryCard(
                    title="Story Title",
                    description="Story description",
                    date=datetime.now(),
                    author="Story author",
                    subject="Story subject",
                    reading_level="Story reading level",
                    image_url="https://picsum.photos/200",
                    story_url="Story URL",
                )
            )
        ] * 10

    @rx.var
    def top_stories(self) -> list[dict]:
        return [
            story_card_to_dict(
                StoryCard(
                    title="Story Title2222",
                    description="Story description",
                    date=datetime.now(),
                    author="Story author",
                    subject="Story subject",
                    reading_level="Story reading level",
                    image_url="https://picsum.photos/200",
                    story_url="Story URL",
                )
            )
        ] * 10


def story_card(story_data: dict) -> rx.Component:
    title = rx.heading(f"{story_data["title"]}", padding="0", size="4")

    author = rx.heading(f"{story_data['author']}", padding="0", size="3")

    story_image = rx.image(
        src=story_data["image_url"],
        alt=str(story_data["title"]),
        height="150px",
        width="100%",
        object_fit="cover",
    )

    badges = rx.hstack(
        rx.badge(story_data["subject"], color_scheme="blue"),
        rx.badge(story_data["reading_level"], color_scheme="green"),
        rx.badge(story_data["date"], color_scheme="gray"),
        spacing="2",
        align_items="flex-start",
        flex_wrap="wrap",
    )

    card_content = rx.box(
        story_image,
        rx.vstack(
            rx.box(
                title,
                author,
            ),
            badges,
            padding="1em",
        ),
        border_radius="md",
        width="300px",
        box_shadow="md",
    )

    return rx.card(
        card_content,
        on_click=rx.redirect(story_data["story_url"]),
        _hover={
            "cursor": "pointer",
        },
        padding="0",
    )


class CreateStoryImage(rx.State):
    image_path = "assets/characters.jpg"
    image = Image.open(image_path)


class DiscussStoryImage(rx.State):
    image_path = "assets/talking_characters.jpg"
    image = Image.open(image_path)


def top_story_section() -> rx.Component:

    create_story_card = rx.card(
        rx.image(
            src=CreateStoryImage.image,
            alt="Create Story",
            object_fit="cover",
            height="100%",
            width="100%",
        ),
        rx.box(
            rx.heading(
                "Create Your Own Story", size="lg", color="white", text_align="center"
            ),
            rx.box(
                rx.text(
                    "Choose characters",
                    color="white",
                    weight="bold",
                    text_align="center",
                ),
                rx.text(
                    "Pick learning outcomes",
                    color="white",
                    weight="bold",
                    text_align="center",
                ),
                rx.text(
                    "Adjust reading level and plot",
                    color="white",
                    weight="bold",
                    text_align="center",
                ),
                padding_top="1em",
            ),
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            padding="1em",
            background="rgba(0, 0, 0, 0.4)",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),
        position="relative",
        border_radius="md",
        overflow="hidden",
        width="100%",
        height="300px",
        transition="transform 0.3s ease",
        _hover={
            "cursor": "pointer",
            "box_shadow": "lg",
            "transform": "scale(1.05)",
        },
        padding="0",
    )

    talk_story_card = rx.card(
        rx.image(
            src=DiscussStoryImage.image,
            alt="Discuss Story",
            object_fit="cover",
            height="100%",
            width="100%",
        ),
        rx.box(
            rx.heading(
                "Talk About the Story", size="lg", color="white", text_align="center"
            ),
            rx.box(
                rx.text(
                    "Chat with characters",
                    color="white",
                    weight="bold",
                    text_align="center",
                ),
                rx.text(
                    "Discuss story plot",
                    color="white",
                    weight="bold",
                    text_align="center",
                ),
                rx.text(
                    "Explore different endings",
                    color="white",
                    weight="bold",
                    text_align="center",
                ),
                padding_top="1em",
            ),
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            padding="1em",
            background="rgba(0, 0, 0, 0.4)",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),
        position="relative",
        border_radius="md",
        overflow="hidden",
        width="100%",
        height="300px",
        transition="transform 0.3s ease",
        _hover={
            "cursor": "pointer",
            "box_shadow": "lg",
            "transform": "scale(1.05)",
        },
        padding="0",
    )

    return rx.container(
        rx.mobile_only(
            rx.vstack(
                rx.link(
                    create_story_card,
                    href="/create",
                ),
                rx.link(
                    talk_story_card,
                    href="/talk",
                ),
                spacing="6",
                width="100%",
                align_items="stretch",
                display={
                    "base": "block",
                    "md": "flex",
                },
            ),
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                rx.link(
                    create_story_card,
                    href="/create",
                    width="100%",
                ),
                rx.link(
                    talk_story_card,
                    href="/talk",
                    width="100%",
                ),
                spacing="6",
                width="100%",
                align_items="stretch",
                display={
                    "base": "block",
                    "md": "flex",
                },
            ),
        ),
        max_width="1200px",
        width="100%",
        padding="1em 0",
        margin="0 auto",
    )


def home() -> rx.Component:
    return rx.vstack(
        rx.container(
            rx.heading("Create Your Own Stories!", size="lg"),
            top_story_section(),
            padding="1em",
            max_width="1200px",
            width="100%",
            margin="0 auto",
        ),
        rx.container(
            rx.heading("Latest Stories", size="lg"),
            rx.box(
                rx.hstack(
                    rx.foreach(
                        State.latest_stories,
                        story_card,
                    ),
                    spacing="4",
                    padding="1em 0",
                ),
                overflow_x="auto",
                display="flex",
                max_width="100%",
                white_space="nowrap",
            ),
            max_width="1200px",
            width="100%",
            margin="0 auto",
            padding="1em",
        ),
        rx.container(
            rx.heading("Trending Stories", size="lg"),
            rx.box(
                rx.hstack(
                    rx.foreach(
                        State.top_stories,
                        story_card,
                    ),
                    spacing="4",
                    padding="1em 0",
                ),
                overflow_x="auto",
                display="flex",
                max_width="100%",
                white_space="nowrap",
            ),
            max_width="1200px",
            width="100%",
            margin="0 auto",
            padding="1em",
        ),
        width="100%",
        spacing="4",
    )


@rx.page(on_load=BaseState.get_configs)
def index() -> rx.Component:
    return rx.container(
        header(),
        home(),
        footer(),
        padding="0",
    )
