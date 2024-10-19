"""
Header component.
"""

import reflex as rx

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
                rx.heading("Reflex", size="7", weight="bold"),
                align_items="center",
            ),
            # rx.hstack(
            #     navbar_link("Home", "/#"),
            #     navbar_link("About", "/#"),
            #     navbar_link("Pricing", "/#"),
            #     navbar_link("Contact", "/#"),
            #     spacing="5",
            # ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.icon_button(
                        rx.icon("user"),
                        size="2",
                        radius="full",
                    )
                ),
                rx.menu.content(
                    rx.menu.item("Settings"),
                    rx.menu.item("Earnings"),
                    rx.menu.separator(),
                    rx.menu.item("Log out"),
                ),
                justify="end",
            ),
            justify="between",
            align_items="center",
        ),
        padding="1em",
        width="100%",
    )
