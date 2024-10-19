"""Home page."""

import reflex as rx


def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Home"),
        rx.text("Welcome to the Home page!"),
    )
