from datetime import datetime
from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, EmailStr, Field


class PostBaseSchema(BaseModel):

    title: Annotated[str, Len(max_length=120)]
    body: str
    user_id: Annotated[int, Len(max_length=40)]


class PostCreateSchema(PostBaseSchema):
    """
    Create new user
    """


class PostReadSchema(PostBaseSchema):
    id: int
    created_at: datetime
