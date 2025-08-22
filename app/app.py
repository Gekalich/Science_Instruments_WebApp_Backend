from fastapi import FastAPI
from .db.session import Base, engine
from .routers.handlers import register_handlers


def create_app() -> FastAPI:
    # Создаём FastAPI приложение
    app = FastAPI(title="Science Instruments WebApp")

    # Опционально создаём таблицы при старте
    Base.metadata.create_all(bind=engine)

    # Регистрируем все роутеры через handlers.py
    register_handlers(app)

    return app
