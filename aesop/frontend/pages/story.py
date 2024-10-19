"""Talk page."""

import reflex as rx

from aesop.frontend.utils import BaseState


@rx.page(on_load=BaseState.get_configs)
def story() -> rx.Component:
    return rx.vstack(
        rx.heading("Story 2"),
        rx.text("Welcome to the Story page!"),
    )
