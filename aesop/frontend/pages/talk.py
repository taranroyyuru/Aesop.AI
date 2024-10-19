"""Talk page."""

import reflex as rx

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState


def talk():
    return rx.vstack(
        rx.heading("Talk"),
        rx.text("Welcome to the Talk page!"),
        padding="1em",
    )


@rx.page(on_load=BaseState.get_configs)
def talk_page() -> rx.Component:
    return rx.container(
        header(redirect_to_signin=True),
        talk(),
        footer(),
        padding="0",
    )
