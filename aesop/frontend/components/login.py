import reflex as rx
from reflex_clerk import (
    clerk_provider,
    redirect_to_sign_in,
    sign_in_button,
    signed_in,
    signed_out,
    user_button,
)


def index(redirect_to_signin: bool = False) -> rx.Component:
    if redirect_to_signin and not signed_in():
        return clerk_provider(signed_out(redirect_to_sign_in()))
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
