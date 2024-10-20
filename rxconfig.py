import reflex as rx
from dotenv import load_dotenv
import os
# config
# url = 
# print(url)
# url = db_url= f"postgresql://{os.getenv('DB_LOGIN')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}:5432/storiesdb"
# print(url)
config = rx.Config(
    app_name="aesop",
	db_url= "postgresql://aesopadmin:aesop123@aesop2-1.ctq6oauek6z5.us-east-2.rds.amazonaws.com:5432/storiesdb"
	)