from fastapi import HTTPException

class AppException(HTTPException):
    """Base class for custom exceptions"""
    def __init__(self, status_code: int, detail: str, error_code: str):
        self.error_code = error_code
        super().__init__(status_code=status_code, detail=detail)

class NotFoundException(AppException):
    """Exception for 404 Not Found"""
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail, error_code="NOT_FOUND")

class UnauthorizedException(AppException):
    """Exception for 401 Unauthorized"""
    def __init__(self, detail: str = "Unauthorized access"):
        super().__init__(status_code=401, detail=detail, error_code="UNAUTHORIZED")

class BadRequestException(AppException):
    """Exception for 400 Bad Request"""
    def __init__(self, detail: str = "Bad request"):
        super().__init__(status_code=400, detail=detail, error_code="BAD_REQUEST")

class ForbiddenException(AppException):
    """Exception for 403 Forbidden"""
    def __init__(self, detail: str = "Access forbidden"):
        super().__init__(status_code=403, detail=detail, error_code="FORBIDDEN")

class ConflictException(AppException):
    """Exception for 409 Conflict"""
    def __init__(self, detail: str = "Conflict error"):
        super().__init__(status_code=409, detail=detail, error_code="CONFLICT")
