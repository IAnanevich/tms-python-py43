from src.lesson_13.hw_13.mixins.mixin import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class BaseManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass
