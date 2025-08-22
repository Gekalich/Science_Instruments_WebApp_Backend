from .model import MenuItem
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional


class MenuItemDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_menu_item(
        self,
        name: str,
        nickname: Optional[str] = None,
        description: Optional[str] = None,
        parent_menu_item_id: Optional[int] = None
    ) -> MenuItem:
        """Создаёт новый элемент меню"""
        new_item = MenuItem(
            name=name,
            nickname=nickname,
            description=description,
            parent_menu_item_id=parent_menu_item_id
        )
        self.db_session.add(new_item)
        await self.db_session.commit()
        await self.db_session.refresh(new_item)
        return new_item

    async def get_menu_item(self, item_id: int) -> Optional[MenuItem]:
        """Получает элемент меню по id"""
        result = await self.db_session.execute(
            select(MenuItem).where(MenuItem.id == item_id)
        )
        return result.scalar_one_or_none()

    async def get_all_menu_items(self) -> List[MenuItem]:
        """Возвращает все элементы меню"""
        result = await self.db_session.execute(select(MenuItem))
        return result.scalars().all()

    async def update_menu_item(
        self,
        item_id: int,
        name: Optional[str] = None,
        nickname: Optional[str] = None,
        description: Optional[str] = None,
        parent_menu_item_id: Optional[int] = None
    ) -> Optional[MenuItem]:
        """Обновляет поля элемента меню"""
        item = await self.get_menu_item(item_id)
        if not item:
            return None
        if name is not None:
            item.name = name
        if nickname is not None:
            item.nickname = nickname
        if description is not None:
            item.description = description
        if parent_menu_item_id is not None:
            item.parent_menu_item_id = parent_menu_item_id
        await self.db_session.commit()
        await self.db_session.refresh(item)
        return item

    async def delete_menu_item(self, item_id: int) -> bool:
        """Удаляет элемент меню"""
        item = await self.get_menu_item(item_id)
        if not item:
            return False
        await self.db_session.delete(item)
        await self.db_session.commit()
        return True
