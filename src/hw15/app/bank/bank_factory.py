from typing import Callable
from .api import BankApi


class Bank(object):

    @staticmethod
    def get(class_name: str) -> object:
        if type(class_name) != str:
            raise ValueError("class_name must be a string!")

        raw_subclasses_ = BankApi.__subclasses__()
        classes: dict[str, Callable[..., object]] = {c.__name__: c for c in raw_subclasses_}
        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_

        raise "ClassNotFoundError"
