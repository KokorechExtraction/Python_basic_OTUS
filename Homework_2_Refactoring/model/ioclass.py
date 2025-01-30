from pathlib import Path
from .phonebook import Phonebook
from .custom_exceptions import WrongFormatError
from .data_ru import *
import json


class IOClass:

    def __init__(self, phonebook: Phonebook, data_files: str | dict[str, str] = None):
        self._data_files = data_files
        self.phonebook = phonebook

    @property
    def data_files(self):
        return self._data_files

    @data_files.setter
    def data_files(self, data_files):
        self._data_files = data_files

    def format_check(self):
        if Path(self.phonebook.path).suffix.lower() == ".txt":
            return True
        elif Path(self.phonebook.path).suffix.lower() == ".json":
            return False
        else:
            raise WrongFormatError(wrong_format_msg)


class Reader(IOClass):
    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = cls._instance or super().__new__(cls)
        return cls._instance

    def __init__(self, phonebook, data_files: str | dict[str, str] = None):
        super().__init__(phonebook, data_files)

    def open(self):

        with open(self.phonebook.path, "r", encoding="utf-8") as data_file:
            if super().format_check():
                self.data_files = data_file.readlines()
            else:
                self.data_files = json.load(data_file)


class Writer(IOClass):
    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = cls._instance or super().__new__(cls)
        return cls._instance

    def __init__(self, phonebook, data_files: str | dict[str, str] = None):
        super().__init__(phonebook, data_files)

    def save(self):
        with open(self.phonebook.path, "w", encoding="utf-8") as data_file:
            data_file.write(self.data_files)
