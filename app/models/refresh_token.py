from datetime import datetime, timezone
from beanie import PydanticObjectId
from pydantic import Field
from app.models.base import BaseDocument
from pymongo import IndexModel


class RefreshToken(BaseDocument):
    user_id: PydanticObjectId = Field(index=True)
    refresh_token: str = Field(unique=True, index=True)
    expires_at: datetime
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    revoked: bool = False

    class Settings:
        name = "refresh_tokens"
        indexes = [
            IndexModel(
                [("expires_at", 1)],
                expireAfterSeconds=0
            )
        ]