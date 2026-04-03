from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from src.core.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Агро Платформа запущена (Modular Monolith)")
    yield
    print("⛔ Агро Платформа остановлена")


app = FastAPI(
    title="Агро Платформа",
    description="Единая платформа управления агрохолдингом",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "message": "Агро Платформа работает успешно! ✅",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "architecture": "Modular Monolith",
    }


# Добавляем тестовый эндпоинт для проверки связи с БД
@app.get("/health/db")
async def health_check_db():
    try:
        # Пробуем открыть соединение и выполнить простейший запрос
        with engine.connect() as connection:
            result = connection.execute(text("SELECT @@VERSION")).scalar()
            return {
                "status": "success",
                "message": "Подключение к базе данных установлено! 🚀",
                "db_version": result,
            }
    except Exception as e:
        return {
            "status": "error",
            "message": "Ошибка подключения к базе данных ❌",
            "details": str(e),
        }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
