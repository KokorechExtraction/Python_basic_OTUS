from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .mixins import TimeStampsMixin
from .mixins import IDMixin

if TYPE_CHECKING:
    from . import Post


class User(
    IDMixin,
    TimeStampsMixin,
    Base,
):

    name: Mapped[str] = mapped_column(
        String(length=32),
        nullable=False,
    )
    username: Mapped[str] = mapped_column(
        String(length=150),
        unique=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(length=32),
        nullable=False,
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
