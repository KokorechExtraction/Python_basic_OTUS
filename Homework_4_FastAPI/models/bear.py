from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated

#
# bears = [
#     {"id": 1, "name": "Игорь", "age": "59"},
#     {"id": 2, "name": "Игорь2", "age": "59"},
#     {"id": 3, "name": "Игорь3", "age": "59"},
# ]


class Bear(BaseModel):
    id: PositiveInt
    name: Annotated[str, Field(min_length=3, max_length=15)]
    age: Annotated[int, Field(ge=14, le=100)]


bears = [
    Bear(id=1, name="Игорь", age="59"),
    Bear(id=2, name="Игорь1", age="59"),
    Bear(id=3, name="Игорь2", age="59"),
]
