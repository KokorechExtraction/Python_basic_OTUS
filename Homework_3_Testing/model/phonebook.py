from .contact import Contact
from .data_ru import *


class Phonebook:
    """Класс предназначен для хранения контактов справочника с учетом их ID в виде словаря.

    Класс содержит геттеры для пути справочника и самого справочника (использован декоратор property)
    """

    def __init__(self, path: str = PATH):
        self._path = path
        self._contacts: dict[int, Contact] = {}

    @property
    def path(self):
        """Вернуть путь справочника"""
        return self._path

    @property
    def contacts(self):
        """Вернуть справочник"""
        return self._contacts
