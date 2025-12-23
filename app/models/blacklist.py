from datetime import datetime, timezone
from beanie import Document
from app.models.base import BaseDocument


class BlacklistedToken(BaseDocument):
    token: str
    blacklisted_at: datetime = datetime.now(timezone.utc)

    class Settings:
        name = "blacklisted_tokens"
