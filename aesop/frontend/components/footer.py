"""
Footer component.
"""

import reflex as rx


def index() -> rx.Component:
    """Footer component."""
    return rx.container(
        "Made with ❤️ by the Reflex team",
        size="1",
        background_color="white",
    )
