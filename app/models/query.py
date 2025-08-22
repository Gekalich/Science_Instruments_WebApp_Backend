from .base import CustomBaseModel
from typing import List, Any, Dict


class MenuItemSchema(CustomBaseModel):
    id: int
    name: str


class QueryService:
    """
    Универсальный класс для форматирования и пагинации результатов DAL.
    """

    def get_response_format_query(self, items: List[Any]) -> List[Dict]:
        """
        Форматирует список ORM объектов в список словарей.
        Используется вместо Pydantic-схем.
        """
        return [self._item_to_dict(item) for item in items]

    def get_paginated_data(self, items: List[Any], page: int = 1, page_size: int = 20) -> Dict:
        """
        Делает простую пагинацию результатов.
        """
        total = len(items)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_items = items[start:end]
        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "items": [self._item_to_dict(item) for item in paginated_items]
        }

    def _item_to_dict(self, item: Any) -> Dict:
        """
        Преобразует ORM объект в словарь.
        Берёт все атрибуты, кроме внутренних SQLAlchemy.
        """
        return {
            k: v for k, v in vars(item).items() if not k.startswith("_sa_")
        }
