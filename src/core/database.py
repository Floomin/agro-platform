from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from src.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,  # Поставь True, если хочешь видеть все SQL-запросы
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """FastAPI dependency для получения сессии БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db_and_tables() -> None:
    """Создаёт все таблицы (будем вызывать при старте)"""
    SQLModel.metadata.create_all(bind=engine)
