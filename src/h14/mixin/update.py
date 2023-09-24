from typing import Any
from sqlalchemy import select, update
from sqlalchemy.orm import session
from src.h14.mixin.base import BaseMixin


class UpdateMixin(BaseMixin):
    """
    The UpdateMixin class is a subclass of the BaseMixin class
    """
    @classmethod
    def update(cls, table: Any, pk: int, input_data: dict, ses: session) -> Any:
        """Updates object by id using input_data"""
        query = update(table).where(table.id == pk).values(**input_data)
        cls.execute_commit(query=query, session=ses)
        result = ses.execute(select(table).where(table.id == pk))
        return result.scalars().all()
