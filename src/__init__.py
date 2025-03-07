from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config import config
from src.utils.exceptions import AppException
from src.utils.exceptions_handler import http_exception_handler, app_exception_handler, generic_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.database.database import init_db, close_db
from fastapi.middleware.cors import CORSMiddleware

ALLOWED_ORIGINS = [
    "http://localhost:4200",  # Angular localdev
    "https://myfrontend.com",  # Production Frontend
    "http://localhost:8000",  # Allow API itself (self-origin for Swagger, API calls)
]

# Define lifespan function for managing startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting FastAPI Application...")
    await init_db()  # Initialize database
    yield  # Allows the application to run
    print("🛑 Shutting down FastAPI Application...")
    await close_db()  # Close database connection

# Create FastAPI app with lifespan context
app = FastAPI(debug=config.settings.DEBUG, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # Only allow specified origins
    allow_credentials=True,  # Allow sending cookies (e.g., authentication)
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Specify allowed HTTP methods
    allow_headers=["Authorization", "Content-Type"],  # Restrict allowed headers
)

# Register Exception Handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, http_exception_handler)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Root Route
@app.get("/")
async def root():
    return {"message": "FastAPI with PostgreSQL Connected!"}
