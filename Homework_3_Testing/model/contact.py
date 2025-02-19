from dataclasses import dataclass


@dataclass
class Contact:
    """Класс предназначен для хранения данных контакта справочника.

    Класс содержит геттеры и сеттеры для имени, телефонного номера, комментария (использован декоратор property)
    """

    _name: str = None
    _number: str = None
    _comment: str = None

    @property
    def name(self) -> str:
        """Вернуть имя контакта"""
        return self._name

    @name.setter
    def name(self, name: str):
        """Установить значение имени контакта"""
        self._name = name

    @property
    def number(self) -> str:
        """Вернуть номер контакта"""
        return self._number

    @number.setter
    def number(self, number: str):
        """Установить значение номера контакта"""
        self._number = number

    @property
    def comment(self) -> str:
        """Вернуть комментарий для контакта"""
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Установить значение комментария для контакта"""
        self._comment = comment
