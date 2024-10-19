"""Create page."""

# TODO: on submit -> submit the form (call api)

import reflex as rx
from PIL import Image

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState


class State(rx.State):
    form_data: dict = {}
    character_image = Image.open("assets/characters/default.png")

    def handle_character_change(self, character: str):
        """Handle the character change."""
        self.character_image = Image.open(self.character_list[character])
        self.form_data["character"] = character

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        if (
            not form_data.get("character")
            or not form_data.get("reading_level")
            or not form_data.get("description")
        ):
            rx.toast("Please fill in all fields!", status="warning")
            return

        self.form_data = form_data

        # Call the API or perform your logic here
        print(form_data)
        story_id = "test"

        return rx.redirect(f"/story/{story_id}")

    @rx.var
    def character_list(self) -> dict[str, str]:
        """Get the dictionary of characters and their image URLs."""
        return {
            "Thor": "assets/characters/thor.png",
            "Batman": "assets/characters/batman.png",
            "Superman": "assets/characters/superman.png",
            "Iron-Man": "assets/characters/ironman.png",
            "Spider-Man": "assets/characters/spiderman.png",
            "Wonder-Woman": "assets/characters/wonderwoman.png",
            "Captain America": "assets/characters/captainamerica.png",
            "Make My Own": "assets/characters/default.png",
        }

    @rx.var
    def reading_level_list(self) -> list[str]:
        """Get the list of reading levels."""
        return ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]


def form():
    return rx.vstack(
        rx.heading("Let's Make Something Amazing!", size="xl"),
        rx.image(
            src=State.character_image,
            alt="Character",
            height="300px",
            object_fit="cover",
            border_radius="30px",
        ),
        rx.form(
            rx.vstack(
                rx.select(
                    State.character_list.keys(),
                    placeholder="Select main character",
                    name="character",
                    width="100%",
                    on_change=State.handle_character_change,
                ),
                rx.cond(
                    State.form_data["character"] == "Make My Own",
                    rx.text_field(
                        placeholder="Who is your character?",
                        name="character",
                        width="100%",
                    ),
                ),
                rx.select(
                    State.reading_level_list,
                    placeholder="Select reading level",
                    name="reading_level",
                    width="100%",
                ),
                rx.text_area(
                    placeholder="Describe what you want to learn from the story!",
                    name="description",
                    width="100%",
                    height="150px",
                    padding="1em 0.5em",
                ),
                rx.button(
                    "Create My Story!",
                    type="submit",
                    width="100%",
                    _hover={
                        "cursor": "pointer",
                    },
                ),
                spacing="3",
            ),
            on_submit=State.handle_submit,
        ),
        width="100%",
        padding="1em",
        max_width="550px",
        margin="0 auto",
        justify="center",
        align="center",
    )


@rx.page(on_load=BaseState.get_configs)
def index() -> rx.Component:
    return rx.container(
        header(),
        form(),
        footer(),
        padding="0",
    )
