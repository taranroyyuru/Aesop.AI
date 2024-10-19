"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_clerk import install_signin_page

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.components.login import index as login
from rxconfig import config


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.container(
        header(),
        login(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            background_color="green",
        ),
        footer(),
        padding="0",
    )


app = rx.App()
app.add_page(index)
install_signin_page(app)
