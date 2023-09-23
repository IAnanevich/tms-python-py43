from typing import Any, Sequence
from sqlalchemy import select, Row, RowMapping
from sqlalchemy.orm import Session


class ReadMixin:

    @classmethod
    def read(cls, table: Any, session: Session) -> Sequence[Row | RowMapping | Any]:
        # Конструктор чтения всех
        query = select(table)
        objects = session.execute(query)
        return objects.scalars().all()
