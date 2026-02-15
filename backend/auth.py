"""
Authentication handler for HyperReach Local
Connects to MongoDB Cluster1 for user verification
"""
import logging
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from backend.config import settings

logger = logging.getLogger(__name__)

# Initialize MongoDB Client using config settings
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

async def verify_user(username, password):
    """
    Check if user exists in Cluster1 and password matches
    """
    try:
        # Access the 'users' collection
        user = await db.users.find_one({"username": username})
        
        if user and user["password"] == password:
            logger.info(f"✓ Authentication successful for user: {username}")
            return True
        
        logger.warning(f"⚠ Failed login attempt for: {username}")
        return False
    except Exception as e:
        logger.error(f"❌ Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Authentication server error")