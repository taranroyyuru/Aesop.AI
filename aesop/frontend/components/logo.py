"""
Logo component.
"""

import reflex as rx
from PIL import Image


class ImageState(rx.State):
    image_path = "assets/logo.png"
    image = Image.open(image_path)


def logo(
    width="5em",
    height="auto",
    border_radius="25%",
):
    return rx.image(
        src=ImageState.image,
        width=width,
        height=height,
        border_radius=border_radius,
    )
