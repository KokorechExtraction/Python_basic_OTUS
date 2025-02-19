import os

import pytest
from urllib3.filepost import writer

from Homework_3_Testing.model.contact import Contact
from Homework_3_Testing.model.ioclass import Reader, Writer
from Homework_3_Testing.model.phonebook import Phonebook
from Homework_3_Testing.model.data_ru import *


@pytest.fixture()
def data_names():
    names = [
        "Миша",
        "миша",
        "Серж",
        "МИША",
        "   Миша",
        "Миша   ",
        "Миша Миша",
        "Миша123",
        'Миша"№;',
        123,
        True,
        23.14,
        "",
        None,
    ]
    return names


@pytest.fixture()
def data_number():
    number = [
        "1231231231",
        "12312312311",
        "5",
        " 1231231231",
        "1231231231 ",
        "12312 31231",
        "a231231231",
        1231231231,
        12312312311,
        123123123,
        True,
        123.12,
        "",
        None,
    ]
    return number


@pytest.fixture()
def data_path():
    path = [
        "1.txt",
        "ASD.txt",
        "asd.txt",
        "asd1.txt",
        "asd1.TXT",
        "!@#.txt",
        "asd.txt",
        "ASD.json",
        "asd.json",
        "asd1.json",
        "asd1.JSON",
        "!@#.json",
        "!@#.JSON",
        "phonebook.jsosn",
    ]
    return path


@pytest.fixture()
def data_contact(data_names, data_number):
    contact = []
    for name, number in zip(data_names, data_number):
        contact.append(Contact(name, number, name))
    return contact


@pytest.fixture()
def test_path():
    return "test_phone_book.txt"


@pytest.fixture()
def data_phonebook_dict(data_contact):
    phonebook = dict(enumerate(data_contact, 1))
    return phonebook


@pytest.fixture()
def data_phonebook(data_phonebook_dict, test_path):
    phonebook = Phonebook(test_path)
    for contact_id, contact in data_phonebook_dict.items():
        phonebook.contacts[contact_id] = contact
    return phonebook

@pytest.fixture()
def data_book_short(data_names, data_number):
    phonebook = Phonebook()
    for item in range(7):
        phonebook.contacts[item + 1] = Contact(
            data_names[item], data_number[item], data_names[item]
        )
    return phonebook



@pytest.fixture()
def temp_file(test_path):

    file_path = test_path

    with open(test_path, "w", encoding="UTF-8") as file:
        file.write("Миша;123123;миша")
    yield file_path
    os.remove(file_path)


@pytest.fixture()
def empty_file():
    file_path = "empty_phonebook_test.txt"

    with open(file_path, "w", encoding="UTF-8") as file:
        file.write("")
    yield file_path
    os.remove(file_path)
