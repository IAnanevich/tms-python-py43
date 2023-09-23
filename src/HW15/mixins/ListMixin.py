from typing import Any, Sequence
from sqlalchemy import select, Row, RowMapping
from sqlalchemy.orm import Session


class ListMixin:
    @classmethod
    def list(cls, table: Any, session: Session) -> Sequence[Row | RowMapping | Any]:
        query = select(table)
        objects = session.execute(query)
        return objects.scalars().all()

"""
сначала создаем получение айпи потом втсавляем https://ipinfo.io/161.185.160.93/geo
 и в https://ipinfo.io/(полученный айпи)/geo
"""
