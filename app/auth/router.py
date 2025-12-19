from fastapi import APIRouter, HTTPException, status
from app.auth.schemas import RegisterSchema, LoginSchema
from app.auth.service import register_user, authenticate_user
from app.utils.response import APIResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=201)
async def register(payload: RegisterSchema):
    await register_user(payload.email, payload.password)
    return APIResponse.success(data=None, message="User registered")


@router.post("/login")
async def login(payload: LoginSchema):
    token = await authenticate_user(payload.email, payload.password)
    print(token)
    if not token:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    return APIResponse.success(data= token)