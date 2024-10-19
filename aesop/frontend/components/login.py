import os

import reflex as rx
from reflex_clerk import clerk_provider, sign_in_button


def index() -> rx.Component:
    return clerk_provider(
        rx.vstack(
            sign_in_button(),
            align="center",
            spacing="7",
        ),
    )
