from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # синхронный URL, пример: postgresql://user:pass@host/db

# Правильное преобразование для asyncpg
if DATABASE_URL.startswith("postgresql://"):
    ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
elif DATABASE_URL.startswith("postgres://"):
    ASYNC_DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://")
else:
    ASYNC_DATABASE_URL = DATABASE_URL

# ------------------------------
# Синхронная сессия (для скриптов / миграций)
# ------------------------------
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ------------------------------
# Асинхронная сессия (для FastAPI)
# ------------------------------
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True, future=True)

# Используйте async_sessionmaker для асинхронных сессий
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# ------------------------------
# Общая база для всех моделей
# ------------------------------
Base = declarative_base()

# ------------------------------
# Зависимости для FastAPI
# ------------------------------

async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session