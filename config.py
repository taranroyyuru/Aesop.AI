import os

import yaml
from pydantic import BaseModel, ValidationError


class ClerkConfig(BaseModel):
    clerk_publishable_key: str
    clerk_secret_key: str


class AppConfig(BaseModel):
    clerk_config: ClerkConfig


# Global variable to store the loaded configuration
_config = None


def load_config_from_yaml(file_path: str) -> AppConfig:
    print("Loading configurations...")
    try:
        with open(file_path, "r") as file:
            config_dict = yaml.safe_load(file)
            config = AppConfig(**config_dict)

            set_clerk_keys_as_env(config)

            return config
    except FileNotFoundError:
        print(f"Error: Configuration file {file_path} not found.")
        raise
    except ValidationError as e:
        print(f"Error loading configuration: {e}")
        raise


def set_clerk_keys_as_env(config: AppConfig):
    os.environ["CLERK_PUBLISHABLE_KEY"] = config.clerk_config.clerk_publishable_key
    os.environ["CLERK_SECRET_KEY"] = config.clerk_config.clerk_secret_key
    print("Clerk keys have been set in environment variables.")


def get_config(file_path: str = "config.yaml") -> AppConfig:
    global _config
    if _config is None:
        _config = load_config_from_yaml(file_path)
    return _config


# Call get_config() whenever you need to access the config
config = get_config()
