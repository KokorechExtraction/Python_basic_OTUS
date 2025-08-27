import pytest


from Homework_3_Testing.model.model import (
    add_to_buffer_from_file,
    contact_to_str,
    contact_to_json,
    create_contact,
    find_key_word,
    find_contact,
    change_contact,
    delete_contact,
)
from Homework_3_Testing.model.phonebook import Phonebook
from Homework_3_Testing.model.contact import Contact
from Homework_3_Testing.model.ioclass import Reader, Writer
from Homework_3_Testing.model.data_ru import *
from Homework_3_Testing.model.custom_exceptions import ContactNotFoundError


@pytest.fixture()
def phone_book_data(temp_file):
    return Phonebook(temp_file)


@pytest.fixture()
def data_files_data():
    return "Миша;123123;миша"


@pytest.fixture()
def reader_data(phone_book_data, data_files_data):
    return Reader(phone_book_data, data_files_data)


@pytest.fixture()
def writer_data(phone_book_data):
    return Writer(phone_book_data)


@pytest.fixture()
def data_key_word():
    return [
        "Миша",
        "миша",
        "мМиша",
        "иша",
        "",
        "5",
        "1ц",
    ]


@pytest.fixture()
def data_founded_contacts():
    return {
        1: Contact("Миша", "1231231231", "Миша"),
        2: Contact("миша", "12312312311", "миша"),
        4: Contact("МИША", " 1231231231", "МИША"),
        5: Contact("   Миша", "1231231231 ", "   Миша"),
        6: Contact("Миша   ", "12312 31231", "Миша   "),
        7: Contact("Миша Миша", "a231231231", "Миша Миша"),
    }





@pytest.fixture()
def changed_book_short(data_book_short):
    data_book_short.contacts[1] = Contact("Серж", "1234567891", "")
    return data_book_short


@pytest.fixture()
def deleted_book_short(data_book_short):
    data_book_short.contacts.pop(1)
    data_book_short.contacts.pop(2)
    return data_book_short


def test_add_to_buffer_from_file(phone_book_data, data_files_data, reader_data):
    add_to_buffer_from_file(phone_book_data, reader_data)
    assert phone_book_data.contacts == {1: Contact("Миша", "123123", "миша")}


def test_contact_to_str(phone_book_data, writer_data, data_files_data):
    phone_book_data.contacts[1] = Contact("Миша", "123123", "миша")
    contact_to_str(phone_book_data, writer_data)
    assert writer_data.data_files == data_files_data


def test_contact_to_json(phone_book_data, writer_data, data_files_data):
    phone_book_data.contacts[1] = Contact("Миша", "123123", "миша")
    contact_to_json(phone_book_data, writer_data)
    assert writer_data.data_files == {
        "1": {"comment": "миша", "name": "Миша", "number": "123123"}
    }


def test_create_contact(data_phonebook, data_names, data_number):
    phonebook = Phonebook()
    for item in range(0, len(data_names)):
        create_contact(phonebook, data_names[item], data_number[item], data_names[item])
    assert phonebook.contacts == data_phonebook.contacts


@pytest.mark.parametrize(
    "name, number, comment, key_word, expected",
    [
        ("Миша", "1231231231", "Миша", "Миша", True),
        ("Миша", "1231231231", "Миша", "миша", True),
        ("Миша", "1231231231", "Миша", "иша", True),
        ("Миша", "1231231231", "Миша", "123", True),
        ("Миша", "1231231231", "", "", True),
        ("Миша", "1231231231", "Миша", "Игорь", False),
        ("Миша", "1231231231", "Миша", "5", False),
    ],
)
def test_find_key_word(name, number, comment, key_word, expected):
    contact = Contact(name, number, comment)
    result = find_key_word(contact, key_word)
    assert result == expected


@pytest.mark.parametrize(
    "key_word",
    [
        "Миша",
        "миша",
        "мМиша",
        "иша",
    ],
)
def test_find_contact(data_book_short, data_founded_contacts, key_word):
    try:
        results = find_contact(data_book_short, key_word)
        assert results == data_founded_contacts
    except ContactNotFoundError as e:
        assert e.__str__() == contact_not_found_msg


@pytest.mark.parametrize(
    "name, number, comment, contact_id",
    [("Серж", "1234567891", "", 1), ("Серж", "1234567891", "", 98)],
)
def test_change_contact(
    data_book_short, changed_book_short, name, number, comment, contact_id
):
    try:
        change_contact(data_book_short, contact_id, name, number, comment)
        assert data_book_short.contacts == changed_book_short.contacts
    except ContactNotFoundError as e:
        assert e.__str__() == contact_not_found_msg


@pytest.mark.parametrize(
    "contact_id",
    [1, 2, 98],
)
def test_change_contact(data_book_short, deleted_book_short, contact_id):
    try:
        delete_contact(data_book_short, contact_id)
        assert data_book_short.contacts == deleted_book_short.contacts
    except ContactNotFoundError as e:
        assert e.__str__() == contact_not_found_msg
