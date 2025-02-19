from pathlib import Path
from .phonebook import Phonebook
from .custom_exceptions import WrongFormatError
from .data_ru import *
import json


class IOClass:
    """Родительский класс для ввода и вывода.

    Методы класса
    data_files - getter
    data_files - setter
    format_check - проверка формата txt или json

    Дочерние классы
    Reader - класс для записи
    Writer - класс для чтения
    """

    def __init__(self, phonebook: Phonebook, data_files: str | dict[str, str] = None):
        self.phonebook = phonebook
        self._data_files = data_files

    @property
    def data_files(self):
        """Получить значение data_files"""
        return self._data_files

    @data_files.setter
    def data_files(self, data_files):
        """Записать значение data_files"""
        self._data_files = data_files

    def format_check(self):
        """Проверить совместимость формата (txt или json) или вызвать исключение"""
        if Path(self.phonebook.path).suffix.lower() == ".txt":
            return True
        elif Path(self.phonebook.path).suffix.lower() == ".json":
            return False
        else:
            raise WrongFormatError(wrong_format_msg)


class Reader(IOClass):
    """Класс для чтения из файла.

    Класс синглтон, потому что могу
    Методы класса:
    open - открывает файл через контекстный менеджер
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = cls._instance or super().__new__(cls)
        return cls._instance

    def __init__(self, phonebook, data_files: str | dict[str, str] = None):
        super().__init__(phonebook, data_files)

    def open(self):
        """Записать данные в переменную класса data_files из файла txt или json"""
        with open(self.phonebook.path, "r", encoding="utf-8") as data_file:
            if super().format_check():
                self.data_files = data_file.readlines()
            else:
                self.data_files = json.load(data_file)


class Writer(IOClass):
    """Класс для записи в файл.

    Класс синглтон, потому что могу
    Методы класса:
    save - осуществляет запись в файл через контекстный менеджер
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = cls._instance or super().__new__(cls)
        return cls._instance

    def __init__(self, phonebook, data_files: str | dict[str, str] = None):
        super().__init__(phonebook, data_files)

    def save(self):
        """Записать данные из data_files в файл txt или json"""
        with open(self.phonebook.path, "w", encoding="utf-8") as data_file:
            data_file.write(self.data_files)
