from app.auth.schemas import TokenSchema
from app.core.database import db
from pymongo.errors import DuplicateKeyError, PyMongoError
from app.utils.exceptions import (
    EmailAlreadyExistsException,
    DatabaseException,
    InvalidCredentialsException,
    UserCreationException
)
from app.core.security import hash_password, verify_password, create_access_token

async def register_user(email: str, password: str) -> None:
    user = {
        "email": email,
        "password": hash_password(password)
    }

    try:
        await db.users.insert_one(user)
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
    try:
        user = await db.users.find_one({"email": email})

        if not user or not verify_password(password, user["password"]):
            raise InvalidCredentialsException()

        access_token = create_access_token({"sub": user["email"]})

        return TokenSchema(
            access_token=access_token
        )

    except PyMongoError:
        raise DatabaseException()
