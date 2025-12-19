from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed:str) -> bool:
    return pwd_context.verify(password, hashed)

def create_access_token(payload_data:dict) -> str :
    payload = payload_data.copy()
    payload['exp'] =  datetime.utcnow() + settings.access_token_expire
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
