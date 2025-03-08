from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from src.config.config import settings

# Create Async Engine
engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)

# Create Session Factory
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to Get Database Session
async def get_db() -> AsyncSession: 
    async with SessionLocal() as session:
        yield session

# Initialize Database (Startup)
async def init_db():
    async with engine.begin() as conn:
        from src.model.user_model import User
        from src.model.api_model import APIKey
        await conn.run_sync(SQLModel.metadata.create_all)
    print("✅ Database initialized successfully.")

# Close Database Connection (Shutdown)
async def close_db():
    await engine.dispose()
    print("🔒 Database connection closed.")

