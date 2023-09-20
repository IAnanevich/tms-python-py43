from src.edgar_hw13.mixins.create_mixin import CreateMixin
from src.edgar_hw13.mixins.delete_mixin import DeleteMixin
from src.edgar_hw13.mixins.list_mixin import ListMixin
from src.edgar_hw13.mixins.update_mixin import UpdateMixin


class BaseManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass
