"""
Header component.
"""

import reflex as rx

from aesop.frontend.components.login import index as login
from aesop.frontend.components.logo import logo


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def index() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                logo(
                    width="2.25em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading("Aesop", size="7", weight="bold"),
                align_items="center",
            ),
            rx.menu.root(
                login(),
                justify="end",
            ),
            justify="between",
            align_items="center",
        ),
        rx.divider(margin="1em 0 0 0"),
        padding="1em",
        width="100%",
        on_click=rx.redirect("/"),
        _hover={
            "cursor": "pointer",
        },
    )
