"""
Async Users CRUD

Create
Read
Update
Delete
"""

import logging

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from homework_07.blog_app.models import User
from homework_07.blog_app.schemas.user import UserCreateSchema

from typing import List

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"

log = logging.getLogger(__name__)


class UsersCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        return list((await self.session.scalars(stmt)).all())

    async def get_by_id(self, user_id: int) -> User | None:
        return await self.session.get(User, user_id)

    async def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user
