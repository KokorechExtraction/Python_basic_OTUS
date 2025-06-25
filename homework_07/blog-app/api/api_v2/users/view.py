from typing import Annotated

from fastapi import Depends, APIRouter

from .crud import UsersCRUD
from .dependencies import user_crud, get_user_by_id
from homework_07.blog_app.models import User
from homework_07.blog_app.schemas.user import UserReadSchema, UserCreateSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UsersCRUD])
async def get_users(
        crud: Annotated[
            UsersCRUD,
            Depends(user_crud),
        ],
) -> list[User]:
    return await crud.get()

@router.get("/{user_id}/", response_model=UserReadSchema)
def get_user(
        user: Annotated[
            User,
            Depends(get_user_by_id),
        ],
) -> User:
    return user

@router.post("/", response_model=UserReadSchema)
async def create_user(
        user_in: UserCreateSchema,
        crud: Annotated[
            UsersCRUD,
            Depends(user_crud),
        ],
) -> User:
    return await crud.create(user_create=user_in)