from app.auth.schemas import TokenSchema
from app.core.database import db
from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.core.config import settings
from pymongo.errors import DuplicateKeyError, PyMongoError
from app.utils.exceptions import (
    EmailAlreadyExistsException,
    DatabaseException,
    InvalidCredentialsException,
    UserCreationException
)
from app.core.security import hash_password, verify_password, create_access_token, generate_refresh_token
from datetime import datetime, timezone

async def register_user(email: str, password: str, name:str) -> None:
    try:
        user = User(
            email=email,
            password=hash_password(password),
            name=name
        )
        await user.insert()
    except DuplicateKeyError:
        # Email uniqueness violation
        raise EmailAlreadyExistsException()

    except PyMongoError:
        # Any other MongoDB-related issue
        raise DatabaseException()

    except Exception:
        # Truly unexpected error
        raise UserCreationException()

async def authenticate_user(email: str, password: str) -> TokenSchema:
    user = await User.find_one(User.email == email)

    if not user or not verify_password(password, user.password):
        raise InvalidCredentialsException()

    access_token, expires_in = create_access_token({"sub": user.email})
    refresh_token = generate_refresh_token()
    await RefreshToken(
        user_id=user.id,
        refresh_token=refresh_token,
        expires_at= datetime.now(timezone.utc) + settings.refresh_token_expire
    ).insert()

    return TokenSchema(
        access_token=access_token,
        token_type="bearer",
        expires_in=expires_in,
        refresh_token=refresh_token
    )
