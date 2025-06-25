from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import mapped_column, Mapped


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        default=datetime.now,
    )
