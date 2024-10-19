"""Talk page."""

import reflex as rx

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState


def story() -> rx.Component:
    return rx.vstack(
        rx.heading("Story 2"),
        rx.text("Welcome to the Story page!"),
    )


@rx.page(on_load=BaseState.get_configs)
def story_page() -> rx.Component:
    return rx.container(
        header(),
        story(),
        footer(),
        padding="0",
    )
