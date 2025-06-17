from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""

    make_com_webhook_url: Optional[str] = None
    custom_server_webhook_url: Optional[str] = None
    database_url: Optional[str] = None  # Example DB URL

    # Configuration for Pydantic Settings (loads from .env)
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
