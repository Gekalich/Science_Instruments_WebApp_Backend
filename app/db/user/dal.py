from .model import UserData
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional, List

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, username: str, email: str, password: str) -> UserData:
        """Создаёт пользователя с захэшированным паролем"""
        hashed_password = pwd_context.hash(password)
        new_user = UserData(
            username=username,
            email=email,
            password_hash=hashed_password
        )
        self.db_session.add(new_user)
        await self.db_session.commit()
        await self.db_session.refresh(new_user)
        return new_user

    @staticmethod
    def verify_user_password(plain_password: str, hashed_password: str) -> bool:
        """Проверяет пароль пользователя"""
        return pwd_context.verify(plain_password, hashed_password)

    async def get_user_by_id(self, user_id: int) -> Optional[UserData]:
        """Получает пользователя по id"""
        result = await self.db_session.execute(select(UserData).where(UserData.id == user_id))
        return result.scalar_one_or_none()

    async def update_password(self, user_id: int, new_password: str) -> Optional[UserData]:
        """Обновляет пароль пользователя"""
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        user.password_hash = pwd_context.hash(new_password)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user

    async def update_email(self, user_id: int, new_email: str) -> Optional[UserData]:
        """Обновляет email пользователя"""
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        user.email = new_email
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user

    async def update_name(self, user_id: int, new_name: str) -> Optional[UserData]:
        """Обновляет имя пользователя"""
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        user.name = new_name
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user

    async def get_all_users(self) -> List[UserData]:
        """Возвращает список всех пользователей"""
        result = await self.db_session.execute(select(UserData))
        # Convert Sequence to List
        return list(result.scalars().all())