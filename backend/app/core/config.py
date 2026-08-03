"""
---------------------------------------------------------
Project     : NovaCopilot AI
File        : config.py
Description : Application Configuration
Author      : Arun + OpenAI
---------------------------------------------------------
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Application Settings
    """

    # =====================================================
    # PROJECT
    # =====================================================

    PROJECT_NAME: str = "NovaCopilot AI"

    PROJECT_VERSION: str = "1.0.0"

    API_PREFIX: str = "/api"

    DEBUG: bool = True

    # =====================================================
    # DATABASE
    # =====================================================

    DB_HOST: str

    DB_PORT: int

    DB_NAME: str

    DB_USER: str

    DB_PASSWORD: str

    # =====================================================
    # JWT
    # =====================================================

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # =====================================================
    # OLLAMA
    # =====================================================

    OLLAMA_URL: str

    MODEL_NAME: str

    # =====================================================
    # CORS
    # =====================================================

    FRONTEND_URL: str

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()