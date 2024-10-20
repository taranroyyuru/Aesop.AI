import reflex as rx

from aesop.backend.dboperations import get_story
from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.models.story_card import StoryCard


class State(rx.State):
    story_data: StoryCard = None

    @rx.var
    def curr_story_data(self) -> StoryCard:
        """
        The current story data to be displayed.

        This variable is triggered when the page loads and when the story_id parameter in the URL changes.
        It fetches the story data from the database and stores it in the state.
        """
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        return self.story_data

    @rx.var
    def story_title(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return self.story_data.title
        return None

    @rx.var
    def story_subject(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return self.story_data.subject
        return None

    @rx.var
    def story_reading_level(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return self.story_data.reading_level
        return None

    @rx.var
    def story_image_urls(self) -> str:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))
        if self.story_data:
            return str(self.story_data.image_urls)
        return None

    @rx.var
    def story_body(self) -> list[str]:
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))

        if self.story_data:
            return str(self.story_data.story_body).split("|")
        return None

    def curr_data(self):
        self.story_data: StoryCard = get_story(self.router.page.params.get("story_id"))


def single_page() -> rx.Component:
    return rx.center(
        rx.grid(
            rx.box(
                rx.image(
                    src=State.story_image_urls,
                    alt="Story image",
                    width="100%",
                    height="auto",
                    object_fit="cover",
                ),
                background_color="white",
                box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
                border_radius="10px",
                border="1px solid #ddd",
                height="100%",
            ),
            rx.box(
                rx.text(
                    State.story_body,
                    font_size="lg",
                    text_align="justify",
                ),
                display="flex",
                justify_content="center",
                align_items="center",
                background_color="white",
                box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
                border_radius="10px",
                border="1px solid #ddd",
                height="100%",
                padding="2em",
            ),
            style={
                "gridTemplateColumns": "1fr",
                "gap": "1em",
            },
        ),
        padding="2em",
        background_color="#f0f0f0",
    )


def story() -> rx.Component:
    return rx.vstack(
        rx.heading(State.story_title, size="xl"),
        rx.hstack(
            rx.text(
                f"{State.story_subject} ({State.story_reading_level} grade level)",
            ),
        ),
        single_page(),
    )


@rx.page(on_load=State.curr_data)
def story_page() -> rx.Component:
    return rx.container(
        header(),
        story(),
        footer(),
        padding="0",
    )
