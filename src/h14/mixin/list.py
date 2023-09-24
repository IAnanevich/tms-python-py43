from typing import Any
from sqlalchemy import select
from sqlalchemy.orm import session
from src.h14.mixin.base import BaseMixin


class ListMixin(BaseMixin):
    """
    The ListMixin class is a subclass of the BaseMixin class
    """
    @classmethod
    def list(cls, table: Any, ses: session) -> Any:
        """Retrieves all objects"""
        query = select(table)
        objects = ses.execute(query)
        return objects.scalars().all()
