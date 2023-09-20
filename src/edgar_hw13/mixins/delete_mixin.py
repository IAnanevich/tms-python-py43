from typing import Any

from sqlalchemy import delete
from sqlalchemy.orm import Session

from src.edgar_hw13.mixins.base_mixin import BaseMixin


class DeleteMixin(BaseMixin):
    """
    The DeleteMixin class is a subclass of the BaseMixin class and provides a method called delete that is used to
    delete a record from a database table based on its primary key.
    """

    @classmethod
    def delete(cls, table: Any, pk: int, session: Session) -> str:
        """Delete db record by id"""
        query = delete(table).where(table.id == pk)
        cls.execute_commit(query=query, session=session)
        return 'deleted'
