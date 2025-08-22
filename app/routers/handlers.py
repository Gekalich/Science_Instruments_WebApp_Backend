from fastapi import FastAPI
from .menu_handlers import router as menu_router
from .user_handlers import router as user_router


# другие обработчики по аналогии
def register_handlers(app: FastAPI):
    """Регистрируем все роутеры приложения"""
    app.include_router(menu_router, prefix="/menu")
    app.include_router(user_router, prefix="/users")
    # подключаем остальные роутеры
