from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..db.session import get_async_session
from ..db.user.dal import UserDAL
from ..models.query import QueryService

router = APIRouter()

@router.get("/")
async def get_all_users(db: AsyncSession = Depends(get_async_session)):
    dal = UserDAL(db)
    users = await dal.get_all_users()  # возвращает список ORM объектов
    query_service = QueryService()
    return query_service.get_response_format_query(users)
