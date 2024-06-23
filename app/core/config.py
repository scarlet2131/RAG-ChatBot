# app/core/config.py
# After
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os


load_dotenv()  # take environment variables from .env.
class Settings(BaseSettings):
    MONGO_URL: str
    MONGO_DB: str = "rag_db"  # Default value if not set
    OPENAI_API_KEY: str

    class Config:
        # Tells Pydantic to read the environment variables.
        env_file = ".env"

settings = Settings()
print(f"MONGO_URL: {settings.MONGO_URL}")
print(f"OPENAI_API_KEY: {settings.OPENAI_API_KEY}")