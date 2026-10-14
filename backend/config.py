import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/nexus_ai")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-nexus-key")
    PAPER_STARTING_BALANCE: float = 100.0
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
      
