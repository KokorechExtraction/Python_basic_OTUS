from .contact import Contact
from .data_ru import *


class Phonebook:

    def __init__(self, path: str = PATH):
        self._path = path
        self._contacts: dict[int, Contact] = {}

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path: str):
        self._path = path

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts: dict):
        self._contacts = contacts
