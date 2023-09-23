from typing import Optional, Any

from sqlalchemy.orm import Session
from sqlalchemy.sql import expression


class BaseMixin:
    """"Base database mixin"""

    @staticmethod
    def execute_commit(query: expression, session: Session, values: Optional[list] = None) -> None:
        """Execute commit"""
        session.execute(query, values)
        session.commit()

    @staticmethod
    def get_by_id(table: Any, pk: int, session: Session) -> Any:
        """Returns object by id"""
        return session.query(table).get(pk)
