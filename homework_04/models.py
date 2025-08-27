"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
import uuid
from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Text


from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://app:123@localhost:5432/homework6"
)

db_url = "postgresql+asyncpg://app:123@localhost:5432/homework6"

engine = create_async_engine(db_url, echo=True)


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"


class IDMixin:
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        default=datetime.now,
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class TimeStampsMixin(CreatedAtMixin, UpdatedAtMixin):
    pass


Session = async_sessionmaker(bind=engine)


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


class Post(
    IDMixin,
    TimeStampsMixin,
    Base,
):
    # __tablename__ = "posts"
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

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="posts")
