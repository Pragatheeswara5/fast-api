from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDB:
    client:AsyncIOMotorClient=None
    db=None
    
mongodb=MongoDB()

def init_db():
    mongodb.client=AsyncIOMotorClient(settings.MONGODB_URI)
    mongodb.db=mongodb.client[settings.DATABASE_NAME]
    
    
def get_db():
    return mongodb.db