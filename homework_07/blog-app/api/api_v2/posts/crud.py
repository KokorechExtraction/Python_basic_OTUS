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

from homework_07.blog_app.models import Post
from homework_07.blog_app.schemas.post import PostCreateSchema

from typing import List

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"

log = logging.getLogger(__name__)


class PostsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> list[Post]:
        stmt = select(Post).order_by(Post.id)
        return list((await self.session.scalars(stmt)).all())

    async def get_by_id(self, post_id: int) -> Post | None:
        return await self.session.get(Post, post_id)

    async def create(self, post_create: PostCreateSchema) -> Post:
        user = Post(**post_create.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user
