from .custom_exceptions import WrongNameError, ContactNotFoundError
from .phonebook import Phonebook
from .contact import Contact
from .ioclass import Reader, Writer
from .data_ru import *


def add_to_buffer_from_file(phonebook: Phonebook, reader: Reader) -> None:
    """Добавить данные из файла в созданный справочник"""
    reader.open()
    for contact_id, item in enumerate(reader.data_files, 1):
        name, number, contact_comment = item.strip().split(DELIMITER)
        phonebook.contacts[contact_id] = Contact(name, number, contact_comment)


def contact_to_str(phonebook: Phonebook, writer: Writer) -> None:
    """Преобразовать объект класса Contact в строку"""
    _data_list = []
    for contact_id, contact in phonebook.contacts.items():
        _data_list.append(
            DELIMITER.join([contact.name, contact.number, contact.comment])
        )
    writer.data_files = "\n".join(_data_list)


def contact_to_json(phonebook: Phonebook, writer: Writer) -> None:
    """Преобразовать объект класса Contact в json"""
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
    """Создать контакт в созданном экземпляре Phonebook с указанными именем, номером, комментарием"""
    new_key = len(phonebook.contacts) + 1
    phonebook.contacts[new_key] = Contact(name, number, contact_comment)


def find_key_word(contact: Contact, key_word: str) -> bool:
    """Найти ключевое слово в экземпляре класса Contact, вернуть True, если есть совпадение, если нет - False"""
    for item in (contact.name.lower(), contact.number, contact.comment.lower()):
        if key_word.lower() in item:
            return True
    return False


def find_contact(phonebook: Phonebook, key_word: str) -> dict[int, Contact]:
    """Найти контакт по ключевому слову"""
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
    """Изменить контакт по-заданному ID, если ID не найдено вызвать исключение ContactNotFoundError"""
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
    """Удалить контакт по-заданному ID, если ID не найдено вызвать исключение ContactNotFoundError"""
    if contact_id in phonebook.contacts.keys():
        phonebook.contacts.pop(contact_id)
    else:
        raise ContactNotFoundError(contact_not_found_msg)
