import reflex as rx
from dotenv import load_dotenv
import os
load_dotenv()
# config
config = rx.Config(
    app_name="aesop",
	db_url=f"postgresql://{os.getenv('DB_LOGIN')}@{os.getenv('DB_URL')}:5432/storiesdb"
)