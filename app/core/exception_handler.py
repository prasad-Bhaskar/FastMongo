from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.exceptions import BaseAppException
from app.utils.response import APIResponse
import logging

logger = logging.getLogger(__name__)


async def app_exception_handler(request: Request, exc: BaseAppException):
    logger.warning(f"{exc.error_code} | {exc.message}")

    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponse.error(
            message=exc.message,
            error_code=exc.error_code
        ),
    )