from typing import Annotated, AsyncGenerator

from pydantic import PositiveInt
from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import UsersCRUD
from homework_07.blog_app.models import User
from homework_07.blog_app.models.db_async import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


def user_crud(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> UsersCRUD:
    return UsersCRUD(session)


async def get_user_by_id(
    user_id: Annotated[PositiveInt, Path],
    crud: Annotated[
        UsersCRUD,
        Depends(user_crud),
    ],
) -> User:
    user: User | None = await crud.get_by_id(user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User #{user_id} not found"
    )
