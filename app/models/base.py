
from beanie import Document
from datetime import datetime, timezone
from bson import ObjectId

class BaseDocument(Document):
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

    class Settings:
        use_state_management = True
        validate_on_save = True

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }