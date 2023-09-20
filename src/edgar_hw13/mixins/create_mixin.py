from typing import Any

from sqlalchemy.orm import Session

from src.edgar_hw13.mixins.base_mixin import BaseMixin


class CreateMixin(BaseMixin):
    """
    The CreateMixin class is a subclass of the BaseMixin class and provides a method called create
    that is used to create a new model object in the database.
    """

    @staticmethod
    def create(table: Any, input_data: dict, session: Session) -> Any:
        """Create model"""
        obj = table(**input_data)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
