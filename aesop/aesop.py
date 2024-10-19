"""Main app page."""

import reflex as rx
from reflex_clerk import install_signin_page

from aesop.frontend.pages.create import index as create
from aesop.frontend.pages.home import index as home
from aesop.frontend.pages.story import story
from aesop.frontend.pages.talk import index as talk

app = rx.App(  # pylint: disable=E1102
    theme=rx.theme(
        appearance="light",
        has_background=True,
        accent_color="orange",
        panel_background="translucent",
    )
)

app.add_page(create, route="/create")
app.add_page(story, route="/story")
app.add_page(talk, route="/talk")
app.add_page(home)

install_signin_page(app)
