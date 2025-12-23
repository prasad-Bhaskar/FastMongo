
from app.models.base import BaseDocument
from pydantic import EmailStr, Field

class User(BaseDocument):
    name:str = Field(...)
    email: EmailStr = Field(..., unique=True, index=True)
    password: str = Field(...)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    class Settings:
        name = "users"
