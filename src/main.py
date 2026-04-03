from contextlib import asynccontextmanager

from fastapi import FastAPI


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
