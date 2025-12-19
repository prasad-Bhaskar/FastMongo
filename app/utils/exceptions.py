from fastapi import status
from app.utils.error_codes import ErrorCode

class BaseAppException(Exception):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "Application error"
    error_code: str | None = None

    def __init__(self, message: str | None = None):
        if message:
            self.message = message
        super().__init__(self.message)

class EmailAlreadyExistsException(BaseAppException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Email already exists"
    error_code = ErrorCode.EMAIL_ALREADY_EXISTS

class InvalidCredentialsException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Invalid credentials"
    error_code = ErrorCode.INVALID_CREDENTIALS

class UnauthorizedException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Unauthorized access"
    error_code = ErrorCode.UNAUTHORIZED
    
class InternalErrorException(BaseAppException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal server error"
    error_code = ErrorCode.INTERNAL_ERROR

class ValidationErrorException(BaseAppException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    message = "Validation error"
    error_code = ErrorCode.VALIDATION_ERROR

class DatabaseException(BaseAppException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Database error"
    error_code = ErrorCode.INTERNAL_ERROR

class UserCreationException(BaseAppException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Failed to create user"
    error_code = ErrorCode.INTERNAL_ERROR
