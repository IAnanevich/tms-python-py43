from typing import Any, Sequence
from sqlalchemy import select, Row, RowMapping
from sqlalchemy.orm import Session


class ListMixin:
    @classmethod
    def list(cls, table: Any, session: Session) -> Sequence[Row | RowMapping | Any]:
        query = select(table)
        objects = session.execute(query)
        return objects.scalars().all()
