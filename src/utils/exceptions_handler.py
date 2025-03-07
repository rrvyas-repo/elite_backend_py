from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from src.utils.response import ResponseModel
from src.utils.exceptions import AppException

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseModel(
            success=False,
            status_code=exc.status_code,
            error=exc.detail,
            error_code=exc.error_code
        ).model_dump(),
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseModel(
            success=False,
            status_code=exc.status_code,
            error=exc.detail,
            error_code="HTTP_ERROR"
        ).model_dump(),
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ResponseModel(
            success=False,
            status_code=500,
            error="Internal Server Error",
            error_code="SERVER_ERROR"
        ).model_dump(),
    )
