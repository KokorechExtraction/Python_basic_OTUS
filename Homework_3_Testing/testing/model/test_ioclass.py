import os
from wsgiref.handlers import read_environ

from urllib3.filepost import writer

from Homework_3_Testing.model.model import Phonebook
from Homework_3_Testing.model.ioclass import IOClass, Reader, Writer
from Homework_3_Testing.model.custom_exceptions import WrongFormatError
from Homework_3_Testing.model.data_ru import *

import pytest


class TestIOClass:

    @pytest.mark.parametrize(
        "data, expected", [("123", "123"), ({"123": "123"}, {"123": "123"})]
    )
    def test_data_files(self, data, expected):
        data_files = IOClass(Phonebook(), data)
        assert data_files.data_files == expected

    @pytest.mark.parametrize(
        "data, expected", [("123", "123"), ({"123": "123"}, {"123": "123"})]
    )
    def test_data_files_setter(self, data, expected):
        data_files = IOClass(Phonebook())
        data_files.data_files = data
        assert data_files.data_files == expected

    @pytest.mark.parametrize(
        "path, expected",
        [
            ("1.txt", True),
            ("asd.txt", True),
            ("asd1.txt", True),
            ("!@#.txt", True),
            ("ASD.txt", True),
            ("asd1.JSON", False),
            ("phonebook.jsosn", wrong_format_msg),
        ],
    )
    def test_format_check(self, path, expected):
        ioclass = IOClass(Phonebook(path))
        try:
            assert ioclass.format_check() == expected
        except WrongFormatError as e:
            assert e.__str__() == wrong_format_msg


class TestReader:
    def test_open(self, temp_file):
        reader = Reader(Phonebook(temp_file))
        reader.open()
        print(type(reader.data_files))
        assert reader.data_files == ["Миша;123123;миша"]

    def test_open_empty(self, empty_file):
        reader = Reader(Phonebook(empty_file))
        reader.open()
        assert reader.data_files == []


class TestWriter:
    @pytest.mark.parametrize("written_data", "Миша;123123;миша", "")
    def test_save(self, written_data):
        writer = Writer(Phonebook("test_phone_book.txt"))
        writer.data_files = written_data
        writer.save()
        assert writer.data_files == written_data
        os.remove("test_phone_book.txt")
