from typing import Any, Sequence

from sqlalchemy import select, Row, RowMapping, update
from sqlalchemy.orm import Session

from src.edgar_hw13.mixins.base_mixin import BaseMixin


class UpdateMixin(BaseMixin):
    """
    The UpdateMixin class is a subclass of the BaseMixin class and provides a method called update
    for updating a row in a database table.
    """

    @classmethod
    def update(cls, table: Any, pk: int, input_data: dict, session: Session) -> Sequence[Row | RowMapping | Any]:
        """Updates object by id using input_data"""
        query = update(table).where(table.id == pk).values(**input_data)
        cls.execute_commit(query=query, session=session)
        result = session.execute(select(table).where(table.id == pk))
        return result.scalars().first()
