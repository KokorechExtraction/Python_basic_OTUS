from typing import Annotated, AsyncGenerator

from pydantic import PositiveInt
from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import PostsCRUD
from homework_07.blog_app.models import Post
from homework_07.blog_app.models.db_async import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


def post_crud(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> PostsCRUD:
    return PostsCRUD(session)


async def get_post_by_id(
    post_id: Annotated[PositiveInt, Path],
    crud: Annotated[
        PostsCRUD,
        Depends(post_crud),
    ],
) -> Post:
    post: Post | None = await crud.get_by_id(post_id)
    if post is not None:
        return post

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Post #{post_id} not found"
    )
