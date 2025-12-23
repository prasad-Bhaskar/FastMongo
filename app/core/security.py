from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed:str) -> bool:
    return pwd_context.verify(password, hashed)

def create_access_token(payload_data:dict)  -> tuple[str, int]:
    payload = payload_data.copy()
    expires_delta = settings.access_token_expire
    payload["exp"] = datetime.now(timezone.utc) + expires_delta
    access_token = jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm
    )
    expires_in = int(expires_delta.seconds)
    return access_token, expires_in


def generate_refresh_token() -> str:
    payload = {
        "exp": datetime.now(timezone.utc) + settings.refresh_token_expire
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)