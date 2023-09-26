from src.lesson_13.Rich_hw_13.mixins.mixin import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class BaseManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass
