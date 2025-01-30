from .custom_exceptions import WrongNameError, ContactNotFoundError
from .phonebook import Phonebook
from .contact import Contact
from .ioclass import Reader, Writer
from .data_ru import *


def add_to_buffer_from_file(phonebook: Phonebook, reader: Reader) -> None:
    reader.open()
    for contact_id, item in enumerate(reader.data_files, 1):
        name, number, contact_comment = item.strip().split(DELIMITER)
        phonebook.contacts[contact_id] = Contact(name, number, contact_comment)


def contact_to_str(phonebook: Phonebook, writer: Writer) -> None:
    _data_list = []
    for contact_id, contact in phonebook.contacts.items():
        _data_list.append(
            DELIMITER.join([contact.name, contact.number, contact.comment])
        )
    writer.data_files = "\n".join(_data_list)


def contact_to_json(phonebook: Phonebook, writer: Writer) -> None:
    _json = {}
    for contact_id, contact in phonebook.contacts.items():
        _json[str(contact_id)] = {
            "name": contact.name,
            "number": contact.number,
            "comment": contact.comment,
        }
    writer.data_files = _json


def create_contact(
    phonebook: Phonebook,
    name: str,
    number: str,
    contact_comment: str,
) -> None:
    new_key = len(phonebook.contacts) + 1
    phonebook.contacts[new_key] = Contact(name, number, contact_comment)


def find_key_word(contact: Contact, key_word: str) -> bool:
    for item in (contact.name, contact.number, contact.comment):
        if key_word in item:
            return True
    return False


def find_contact(phonebook: Phonebook, key_word: str) -> dict[int, Contact]:
    requested_contacts = {}
    for contact_id, contact in phonebook.contacts.items():
        if find_key_word(contact, key_word):
            requested_contacts[contact_id] = contact
    if requested_contacts == {}:
        raise ContactNotFoundError(contact_not_found_msg)
    return requested_contacts


def change_contact(
    phonebook: Phonebook, contact_id: int, name: str, number: str, contact_comment: str
) -> None:
    if contact_id in phonebook.contacts.keys():
        if name != "":
            phonebook.contacts[contact_id].name = name
        if number != "":
            phonebook.contacts[contact_id].number = number
        if contact_comment != "":
            phonebook.contacts[contact_id].comment = contact_comment
    else:
        raise ContactNotFoundError(contact_not_found_msg)


def delete_contact(phonebook: Phonebook, contact_id: int) -> None:
    if contact_id in phonebook.contacts.keys():
        phonebook.contacts.pop(contact_id)
