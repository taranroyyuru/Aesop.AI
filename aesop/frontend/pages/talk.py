"""Talk page."""

import reflex as rx


def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Talk"),
        rx.text("Welcome to the Talk page!"),
    )
