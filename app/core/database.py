from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(
    settings.mongo_uri,
    tls=True,
    tlsAllowInvalidCertificates=False,  # set True only if Windows certs are broken
    serverSelectionTimeoutMS=30000,
)
db = client[settings.db_name]


async def create_indexes():
    await db.users.create_index("email", unique=True)
    