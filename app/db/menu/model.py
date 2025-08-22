from ..session import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated, Optional

primary_id = Annotated[int, mapped_column(primary_key=True, index=True)]


class MenuItem(Base):
    __tablename__ = "menu_items"
    __table_args__ = {'schema': 'public'}  # ваша схема здесь

    PROFILE = "profile"
    SETTINGS = "settings"

    MENU_TYPES = (
        (PROFILE, "Профиль пользователя"),
        (SETTINGS, "Настройки профиля")
    )

    id: Mapped[primary_id]
    parent_menu_item_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{__table_args__['schema']}.{__tablename__}.id"),
        nullable=True
    )

    name: Mapped[str] = mapped_column(String(50))
    nickname: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(50))

    def __repr__(self):
        return f"{self.id} - {self.name}"