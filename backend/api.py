from fastapi import APIRouter, status # Add to existing imports
from motor.motor_asyncio import AsyncIOMotorClient # Install 'motor' via pip
from pydantic import BaseModel

# Initialize MongoDB Client using your provided URI
# URI: mongodb+srv://<db_username>:<db_password>@cluster1.fzyqxao.mongodb.net/?appName=Cluster1
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/login", tags=["Auth"])
async def login(request: LoginRequest):
    """
    Verifies user credentials against MongoDB Cluster1
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
    except Exception as e:
        logger.error(f"❌ Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")