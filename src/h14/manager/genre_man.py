from src.h14.mixin.create import CreateMixin
from src.h14.mixin.delete import DeleteMixin
from src.h14.mixin.list import ListMixin
from src.h14.mixin.update import UpdateMixin


class GenreManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass
