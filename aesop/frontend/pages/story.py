import reflex as rx

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState


def double_page(story_text, story_image_url) -> rx.Component:
    return rx.center(
        rx.grid(
            rx.box(
                rx.text(
                    story_text,
                    font_size="lg",
                    text_align="justify",
                ),
                display="flex",
                justify_content="center",
                align_items="center",
                background_color="white",
                box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
                border_radius="10px",
                border="1px solid #ddd",
                height="100%",
                padding="2em",
            ),
            rx.box(
                rx.image(
                    src=story_image_url,
                    alt="Story image",
                    width="100%",
                    height="auto",
                    object_fit="cover",
                ),
                background_color="white",
                box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
                border_radius="10px",
                border="1px solid #ddd",
                height="100%",
            ),
            gap="1em",
            style={
                "gridTemplateColumns": "1fr 1fr",
                "gap": "1em",
            },
        ),
        padding="2em",
        background_color="#f0f0f0",
    )


def single_page(story_text, story_image_url) -> rx.Component:
    return rx.center(
        rx.grid(
            rx.box(
                rx.image(
                    src=story_image_url,
                    alt="Story image",
                    width="100%",
                    height="auto",
                    object_fit="cover",
                ),
                background_color="white",
                box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
                border_radius="10px",
                border="1px solid #ddd",
                height="100%",
            ),
            rx.box(
                rx.text(
                    story_text,
                    font_size="lg",
                    text_align="justify",
                ),
                display="flex",
                justify_content="center",
                align_items="center",
                background_color="white",
                box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
                border_radius="10px",
                border="1px solid #ddd",
                height="100%",
                padding="2em",
            ),
            style={
                "gridTemplateColumns": "1fr",
                "gap": "1em",
            },
        ),
        padding="2em",
        background_color="#f0f0f0",
    )


def story() -> rx.Component:
    return rx.vstack(
        rx.heading("Story Heading by Author", size="xl", padding="1em"),
        rx.mobile_only(
            single_page(
                "Once upon a time, in a magical land far away, there lived a brave hero who embarked on an incredible journey...",
                "https://picsum.photos/400",
            ),
        ),
        rx.tablet_and_desktop(
            double_page(
                "Once upon a time, in a magical land far away, there lived a brave hero who embarked on an incredible journey...",
                "https://picsum.photos/400",
            ),
        ),
    )


@rx.page(on_load=BaseState.get_configs)
def story_page() -> rx.Component:
    return rx.container(
        header(),
        story(),
        footer(),
        padding="0",
    )
