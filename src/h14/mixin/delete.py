from typing import Any
from sqlalchemy import delete
from sqlalchemy.orm import session
from src.h14.mixin.base import BaseMixin


class DeleteMixin(BaseMixin):
    """
    The DeleteMixin class is a subclass of the BaseMixin class
    """
    @classmethod
    def delete(cls, table: Any, pk: int, ses: session) -> str:
        """Delete by id"""
        query = delete(table).where(table.id == pk)
        cls.execute_commit(query=query, session=ses)
        return 'deleted'
