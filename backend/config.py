"""
Configuration management for the Outreach Engine
"""
import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings

# In backend/config.py
class Settings(BaseSettings):
    # ... existing settings ...
    
    # MongoDB Connection Details
    # Replace <db_username> with "rahul-campus-connect" 
    # Replace <db_password> with "rahul - password"
    MONGO_URI: str = "mongodb+srv://rahul-campus-connect:rahul - password@cluster1.fzyqxao.mongodb.net/?appName=Cluster1"
    DB_NAME: str = "Cluster1"

    # Paths
    BASE_DIR: Path = Path(__file__).parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    MODELS_DIR: Path = BASE_DIR / "models"
    # ... rest of the directory initialization ...

settings = Settings()