"""
Configuration management for the Outreach Engine
"""
import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # MongoDB Connection Details
    # Default provided for local testing, but will be overridden by environment variables
    # Ensure no spaces exist in the actual password
    MONGO_URI: str = "mongodb+srv://rahul-campus-connect:rahul-password@cluster1.fzyqxao.mongodb.net/?appName=Cluster1"
    DB_NAME: str = "Cluster1"

    # Paths
    # BASE_DIR points to the root of your project
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    MODELS_DIR: Path = BASE_DIR / "models"

    # Pydantic configuration to load from .env file
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

    def create_directories(self):
        """
        Ensures required folders exist for offline inference and data storage.
        This is vital for the 100% offline inference requirement.
        """
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Instantiate the settings object
settings = Settings()

# Initialize the directory structure immediately upon import
settings.create_directories()
