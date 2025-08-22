from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..db.session import get_async_session
from ..db.menu.dal import MenuItemDAL
from ..models.query import QueryService  # общий класс для форматирования / пагинации

router = APIRouter()

@router.get("/")
async def get_all_menu_items(db: AsyncSession = Depends(get_async_session)):
    dal = MenuItemDAL(db)
    items = await dal.get_all_menu_items()  # возвращает список ORM объектов
    query_service = QueryService()
    return query_service.get_response_format_query(items)
