import reflex as rx
from reflex_clerk import (
    clerk_provider,
    sign_in_button,
    signed_in,
    signed_out,
    user_button,
)


def index() -> rx.Component:
    return clerk_provider(
        signed_in(
            rx.hstack(
                user_button(
                    show_name=True,
                    user_profile_mode="modal",
                ),
            )
        ),
        signed_out(
            rx.button(
                sign_in_button(mode="modal"),
            )
        ),
    )
