from typing import Annotated

from fastapi import Depends, APIRouter

from .crud import PostsCRUD
from .dependencies import post_crud, get_post_by_id
from homework_07.blog_app.models import Post
from homework_07.blog_app.schemas.post import PostReadSchema, PostCreateSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[PostsCRUD])
async def get_posts(
    crud: Annotated[
        PostsCRUD,
        Depends(post_crud),
    ],
) -> list[Post]:
    return await crud.get()


@router.get("/{post_id}/", response_model=PostReadSchema)
def get_post(
    post: Annotated[
        Post,
        Depends(get_post_by_id),
    ],
) -> Post:
    return post


@router.post("/", response_model=PostReadSchema)
async def create_post(
    post_in: PostCreateSchema,
    crud: Annotated[
        PostsCRUD,
        Depends(post_crud),
    ],
) -> Post:
    return await crud.create(post_create=post_in)
