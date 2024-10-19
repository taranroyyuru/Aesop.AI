"""Create page."""

import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def index():
    return rx.flex(
        rx.button(
            "Back",
            on_click=rx.redirect("/previous-page"),
            position="absolute",
            top="1em",
            left="1em",
        ),
        rx.box(
            rx.image(
                src="/logo.png",
                width="100px",
                height="auto",
                position="absolute",
                top="1em",
                left="1em",
            ),
            position="relative",
            width="100%",
            height="100vh",
        ),
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.select(
                        ["Thor", "Batman", "Superman", "Iron-Man", "Spider-Man", "Wonder-Woman", "Captain America"],
                        placeholder="Select Character",
                        name="dropdown1",
                        width="200px",
                        height="300px"
                    ),
                    rx.select(
                        ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"],
                        placeholder="Select Grade Level",
                        name="dropdown2",
                        width="200px",
                        height="300px"
                    ),
                    rx.input(
                        placeholder="Subject",
                        name="subject",
                        width="200px"
                    ),
                    rx.button("Submit", type="submit"),
                    spacing="1em",
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            width="100%",
            max_width="500px",
            spacing="2em",
        ),
        direction="column",
        align="flex-center",
        justify="center",
        width="100%",
        height="100vh",
        padding_left="45%",
        padding_bottom="200px"
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)