from typing import Any
from sqlalchemy.orm import session
from src.h14.mixin.base import BaseMixin


class CreateMixin(BaseMixin):
    """
    The CreateMixin class is a subclass of the BaseMixin class
    """
    @staticmethod
    def create(table: Any, input_data: dict, ses: session) -> Any:
        """Create model"""
        obj = table(**input_data)
        ses.add(obj)
        ses.commit()
        ses.refresh(obj)
        return obj
