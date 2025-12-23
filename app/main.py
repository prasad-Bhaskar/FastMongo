from app.core.exception_handler import app_exception_handler
from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.utils.exceptions import BaseAppException
from app.core.database import init_db


app = FastAPI(title="FastAPI JWT Auth")

@app.get("/")
def root():
    return {"status": "ok"}
app.add_exception_handler(BaseAppException, app_exception_handler)
app.include_router(auth_router)

@app.on_event("startup")
async def startup():
    await init_db()