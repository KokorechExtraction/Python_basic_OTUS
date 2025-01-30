from dataclasses import dataclass


@dataclass
class Contact:

    _name: str = None
    _number: str = None
    _comment: str = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, number: str):
        self._number = number

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        self._comment = comment
