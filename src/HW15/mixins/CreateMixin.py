from typing import Any
from sqlalchemy.orm import Session


class CreateMixin:

    @staticmethod
    def create(table: Any, input_data: dict, session: Session) -> Any:
        obj = table(**input_data)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
