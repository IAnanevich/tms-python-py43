from ..mixins.mixin import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class BaseManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


class UserManager(BaseManager):
    pass


class BookManager(BaseManager):
    pass


class OrderManager(BaseManager):
    pass


class GenreManager(BaseManager):
    pass
