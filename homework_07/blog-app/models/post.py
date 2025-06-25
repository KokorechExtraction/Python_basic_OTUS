from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .mixins import TimeStampsMixin
from .mixins import IDMixin

if TYPE_CHECKING:
    from . import User


class Post(
    IDMixin,
    TimeStampsMixin,
    Base,
):

    title: Mapped[str] = mapped_column(
        String(length=120),
        nullable=False,
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="posts")
