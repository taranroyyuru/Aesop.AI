"""
Logo component.
"""

import reflex as rx
from PIL import Image

# class ImageState(rx.State):
#     image_path = "https://ibb.co/yhTRK9b"
#     image = Image.open(image_path)


def logo(
    width="5em",
    height="auto",
    border_radius="25%",
):
    return rx.image(
        src="https://ibb.co/yhTRK9b",
        width=width,
        height=height,
        border_radius=border_radius,
    )
