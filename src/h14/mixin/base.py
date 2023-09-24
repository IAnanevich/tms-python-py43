from typing import Any
from sqlalchemy.orm import session
from sqlalchemy.sql import expression


class BaseMixin:
    """Base mixin"""

    @staticmethod
    def execute_commit(query: expression, ses: session, values: list = None) -> None:
        """Execute commit"""
        ses.execute(query, values)
        ses.commit()

    @staticmethod
    def get_by_id(table: Any, pk: int, ses: session) -> Any:
        """Returns object by id"""
        return ses.query(table).get(pk)
