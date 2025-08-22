from fastapi import FastAPI
from .db.session import Base, engine
from .routers.handlers import register_handlers


def create_app() -> FastAPI:
    app = FastAPI(title="Science Instruments WebApp")

    # Создаём таблицы при старте (опционально)
    Base.metadata.create_all(bind=engine)

    # Подключаем все роутеры через handlers.py
    register_handlers(app)

    return app
