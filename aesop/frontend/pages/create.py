"""Create page."""

import reflex as rx


def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Create"),
        rx.text("Welcome to the Create page!"),
    )
