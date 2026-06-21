import os
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.database import engine, Base
from app.routers.pages import router as pages_router
from app.routers.users import router as users_router

# Функция, которая выполнится ПЕРЕД стартом сервера
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создает таблицы в Postgres, если их еще нет
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Тут можно что-то закрывать при выключении сервера (например, пул соединений)

app = FastAPI(lifespan=lifespan) # Передаем lifespan в FastAPI

app.include_router(pages_router, tags=["Pages"])
app.include_router(users_router, tags=["Users"])

if os.path.exists("app/public"):
    app.mount("/public", StaticFiles(directory="app/public"), name="public")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)