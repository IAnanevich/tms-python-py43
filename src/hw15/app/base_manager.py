from sqlalchemy.exc import IntegrityError
from database import session, engine # noqa: F401
# TODO посставил костыль. что то напутал с путями и бъет ошибку. и pycharm ругается. прога работает.


class BaseManager:
    LIMIT_ITEM_PAGE = 5

    def __init__(self) -> None:
        self.entity = None

    def list(self, filter: list | None = None, limit: int | None = None, page: int | None = 0) -> list:
        query = session.query(self.entity)
        if limit is not None and limit > 0:
            query = query.limit(limit)
        if page is not None and page > 1:
            query = query.offset((page - 1) * self.LIMIT_ITEM_PAGE)
        if filter is not None:
            query = query.filter(filter)

        return query.all()

    def _save(self, obj: object) -> None:
        try:
            session.add(obj)
            session.flush()
            session.commit()
        except IntegrityError as e:
            print(e)
            session.rollback()

    def _delete(self, pk: int) -> None:
        try:
            obj = self.get_by_id(pk=pk)
            if obj is not None:
                session.delete(obj)
                session.commit()
        except IntegrityError as e:
            print(e)
            session.rollback()
