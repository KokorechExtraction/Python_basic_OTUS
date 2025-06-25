from .created_at_mixin import CreatedAtMixin
from .updated_at_mixin import UpdatedAtMixin


class TimeStampsMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
