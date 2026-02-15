from fastapi import FastAPI, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import logging

# 1. IMPORT YOUR SETTINGS (Fixes the NameError)
from backend.config import settings

# Initialize logging
logger = logging.getLogger("uvicorn")

# 2. INITIALIZE APP
app = FastAPI(title="HyperReach Local API")

# 3. DATABASE CONNECTION
# Uses the URI and DB Name from your config.py
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/login", tags=["Auth"])
async def login(request: LoginRequest):
    """
    Verifies user credentials against MongoDB
    """
    try:
        # Search the 'users' collection for the matching username
        user = await db.users.find_one({"username": request.username})
        
        # Verify the password (Note: In production, use hashed passwords)
        if user and user["password"] == request.password:
            logger.info(f"✓ Login successful: {request.username}")
            return {"status": "success", "message": "Authenticated"}
        
        # If no match or wrong password
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
