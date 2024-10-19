"""Main app page."""

import reflex as rx
from reflex_clerk import install_signin_page

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.pages.create import index as create
from aesop.frontend.pages.home import index as home
from aesop.frontend.pages.talk import index as talk
from config import get_config
from rxconfig import config


class State(rx.State):
    """The app state."""

    def get_configs(self) -> None:
        get_config("config.yaml")


@rx.page(on_load=State.get_configs)
def index() -> rx.Component:
    return rx.container(
        header(),
        home(),
        footer(),
        padding="0",
        max_width="100vw",
    )


app = rx.App(  # pylint: disable=E1102
    theme=rx.theme(
        appearance="light",
        has_background=True,
        accent_color="orange",
        panel_background="translucent",
    )
)

app.add_page(index)
app.add_page(create, route="/create")
app.add_page(talk)
install_signin_page(app)
