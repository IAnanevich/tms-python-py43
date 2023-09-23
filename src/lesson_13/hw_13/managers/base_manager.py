from src.lesson_13.hw_13.mixins.create_mixin import CreateMixin
from src.lesson_13.hw_13.mixins.delete_mixin import DeleteMixin
from src.lesson_13.hw_13.mixins.list_mixin import ListMixin
from src.lesson_13.hw_13.mixins.update_mixin import UpdateMixin


class BaseManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass
