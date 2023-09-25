from typing import Optional, Any, Sequence
from sqlalchemy import Row, RowMapping, select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.sql import expression


class BaseMixin:

    @staticmethod
    def execute_commit(query: expression, session: Session, values: Optional[list] = None) -> None:
        """Execute commit"""
        session.execute(query, values)
        session.commit()

    @staticmethod
    def get_by_id(table: Any, pk: int, session: Session) -> Any:
        """Returns object by id"""
        return session.query(table).get(pk)


class ListMixin(BaseMixin):

    @classmethod
    def list(cls, table: Any, session: Session) -> Sequence[Row | RowMapping | Any]:
        """Retrieves all objects"""
        query = select(table)
        objects = session.execute(query)
        return objects.scalars().all()


class CreateMixin(BaseMixin):

    @staticmethod
    def create(table: Any, input_data: dict, session: Session) -> Any:
        """Create model"""
        obj = table(**input_data)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj


class UpdateMixin(BaseMixin):

    @classmethod
    def update(cls, table: Any, pk: int, input_data: dict, session: Session) -> Sequence[Row | RowMapping | Any]:
        """Updates object by id using input_data"""
        query = update(table).where(table.id == pk).values(**input_data)
        cls.execute_commit(query=query, session=session)
        result = session.execute(select(table).where(table.id == pk))
        return result.scalars().first()


class DeleteMixin(BaseMixin):

    @classmethod
    def delete(cls, table: Any, pk: int, session: Session) -> str:
        """Delete db record by id"""
        query = delete(table).where(table.id == pk)
        cls.execute_commit(query=query, session=session)
        return 'deleted'
