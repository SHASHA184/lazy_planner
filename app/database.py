from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from .config import (
    POSTGRES_HOST,
    POSTGRES_USER,
    POSTGRES_DB,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
)


DATABASE_URL = (
    f"postgresql+asyncpg://{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base class for ORM models
Base = declarative_base()


# Dependency to get a session per request
async def get_db():
    async with async_session() as session:
        yield session
