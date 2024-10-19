import reflex as rx

from config import get_config


class BaseState(rx.State):
    """The app state."""

    def get_configs(self) -> None:
        get_config("config.yaml")
