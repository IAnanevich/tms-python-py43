from typing import Any, Sequence

from sqlalchemy import select, Row, RowMapping
from sqlalchemy.orm import Session

from src.edgar_hw.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    """
    The ListMixin class is a subclass of the BaseMixin class and provides a method called list
    that retrieves all objects from a specified table in the database.
    """

    @classmethod
    def list(cls, table: Any, session: Session) -> Sequence[Row | RowMapping | Any]:
        """Retrieves all objects"""
        query = select(table)
        objects = session.execute(query)
        return objects.scalars().all()
