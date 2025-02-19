from Homework_3_Testing.model.contact import Contact
from Homework_3_Testing.model.data_ru import *
from Homework_3_Testing.model.custom_exceptions import (
    WrongMenuInputError,
    WrongNameError,
    WrongNumberFormatError,
    IdNotFoundError,
    CreationContactError,
)
from Homework_3_Testing.model.model import Phonebook

_table_size = 96
_id_size = 5
_table_borders = "\n" + Fillers.star.value * _table_size
_name_tittle_size = _number_tittle_size = _comment_tittle_size = int(_table_size / 3)
table_core = (
    TableStuf.name_tittle.value
    + (_name_tittle_size - len(TableStuf.name_tittle.value)) * Fillers.space.value
    + TableStuf.number_tittle.value
    + (_number_tittle_size - len(TableStuf.number_tittle.value)) * Fillers.space.value
    + TableStuf.comment_tittle.value
    + (_comment_tittle_size - len(TableStuf.comment_tittle.value)) * Fillers.space.value
)


class Console:
    """Класс для ввода/вывода информации на экран

    Переменные классы:
    phonebook - хранит экземпляр класса Phonebook
    user_input - хранит введенное пользователем параметры

    Методы класса:
    user_input_from_keyboard - обеспечивает запись в user_input с клавиатуры
    menu_input_validation - валидация пункта выбора меню
    contact_validation - валидация имени, номера, комментария контакта
    contact_id_validation - валидация правильности ID контакта
    print_start_menu - вывод меню в консоль
    print_message - вывод сообщения в консоль
    show_contacts - вывод всех контактов
    show_contacts_with_ia - вывод контактов с id
    """

    def __init__(self, phonebook: Phonebook, user_input: str = None):
        self.phonebook = phonebook
        self.user_input = user_input

    def user_input_from_keyboard(self, msg: str):
        """Записать ввод с клавиатуры в user_input"""
        self.user_input = input(msg)

    def menu_input_validation(self) -> int:
        """Проверить правильность ввода выбора меню"""
        if self.user_input.isdigit() and 0 < int(self.user_input) < 10:
            return int(self.user_input)
        raise WrongMenuInputError(wrong_menu_input_error_msg)

    def contact_validation(
        self,
        msg_error: str = None,
        name_val: bool = False,
        number_val: bool = False,
        key_id: str = None,
    ):
        """Проверить правильность имени, номера и комментария контактов

        Функция запрещает создавать пустой контакт и контакты с номером не равным 10 цифрам
        """

        if name_val:
            if key_id and self.user_input == "":
                old_contact = self.phonebook.contacts[key_id]
                return old_contact.name
            if not self.user_input.strip().isalpha():
                raise WrongNameError(msg_error)
            elif self.user_input.replace(" ", "") == "":
                raise WrongNameError(wrong_first_name_error_msg)
            else:
                return self.user_input
        elif number_val:
            if key_id and self.user_input == "":
                old_contact = self.phonebook.contacts[key_id]
                return old_contact.number
            if len(self.user_input) == 10 and self.user_input.isdigit():
                return self.user_input
            raise WrongNumberFormatError(msg_error)
        else:

            return self.user_input

    def contact_id_validation(self, msg_error):
        """Проверить существования id запрашиваемого контакта"""
        if (
            self.user_input.isdigit()
            and int(self.user_input) in self.phonebook.contacts.keys()
        ):
            return int(self.user_input)
        raise IdNotFoundError(msg_error)

    @staticmethod
    def print_start_menu() -> None:
        """Напечатать меню в консоли"""
        for i, item in enumerate(MenuItems):
            if not i:
                print(item.value)
            else:
                print(f"\t{i}.{item.value}")

    @staticmethod
    def print_message(msg: str) -> None:
        "Печать сообщения в консоли"
        print("\n" + Fillers.equality.value * len(msg))
        print(msg)
        print(Fillers.equality.value * len(msg) + "\n")

    def show_contacts(self):
        """Показать все контакты"""
        print(_table_borders + "\n" + table_core)
        for contact_id, contact in self.phonebook.contacts.items():
            print(
                f"{contact.name.strip():<32}"
                + f"{contact.number.strip():<32}"
                + f"{contact.comment.strip():<32}"
            )
        print(_table_borders)

    @staticmethod
    def show_contacts_with_id(requested_contacts: dict[int, Contact]):
        """Показать контакты с id"""
        print(
            _id_size * Fillers.space.value
            + _table_borders
            + "\n"
            + TableStuf.id_tittle.value
            + (_id_size - len(TableStuf.id_tittle.value)) * Fillers.space.value
            + table_core
        )

        for contact_id, contact in requested_contacts.items():
            print(
                f"{contact_id:<5}"
                + f"{contact.name.strip():<32}"
                + f"{contact.number.strip():<32}"
                + f"{contact.comment.strip():<32}"
            )

        print(_table_borders)
