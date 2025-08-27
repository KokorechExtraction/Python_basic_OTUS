from datetime import datetime
from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):

    name: Annotated[str, Len(max_length=32)]
    username: Annotated[str, Len(max_length=150)]
    email: Annotated[EmailStr, Len(max_length=32)]


class UserCreateSchema(UserBaseSchema):
    """
    Create new user
    """


class UserReadSchema(UserBaseSchema):
    id: int
    created_at: datetime
