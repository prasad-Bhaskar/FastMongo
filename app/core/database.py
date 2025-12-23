from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.models.blacklist import BlacklistedToken
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.db_name]

async def init_db():
    await init_beanie(
        database=db,
        document_models=[
            User,
            RefreshToken,
            BlacklistedToken
        ]
    )