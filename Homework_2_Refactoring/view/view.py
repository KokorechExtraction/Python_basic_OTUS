from Homework_2_Refactoring.model.contact import Contact
from Homework_2_Refactoring.model.data_ru import *
from Homework_2_Refactoring.model.custom_exceptions import (
    WrongMenuInputError,
    WrongNameError,
    WrongNumberFormatError,
    IdNotFoundError,
    CreationContactError,
)
from Homework_2_Refactoring.model.model import Phonebook

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

    def __init__(self, phonebook: Phonebook, user_input: str = None):
        self.phonebook = phonebook
        self.user_input = user_input

    def user_input_from_keyboard(self, msg: str):
        self.user_input = input(msg)

    def menu_input_validation(self) -> int:
        if self.user_input.isdigit() and 0 < int(self.user_input) < 10:
            return int(self.user_input)
        raise WrongMenuInputError(wrong_menu_input_error_msg)

    def contact_validation(
        self,
        msg: str,
        msg_error: str = None,
        name_val: bool = False,
        number_val: bool = False,
        key_id: str = None,
    ):

        self.user_input_from_keyboard(msg)

        if name_val:
            if key_id and self.user_input == "":
                old_contact = self.phonebook.contacts[key_id]
                return old_contact.name
            if any(character.isdigit() for character in self.user_input.strip()):
                raise WrongNameError(msg_error)
            elif self.user_input.replace(" ", "") == "":
                raise WrongNameError(wrong_first_name_error_msg)
            else:
                return self.user_input
        elif number_val:
            if key_id and self.user_input == "":
                old_contact = self.phonebook.contacts[key_id]
                return old_contact.number
            if not len(self.user_input) != 10 or self.user_input.isdigit():
                return self.user_input
            raise WrongNumberFormatError(msg_error)
        else:

            return self.user_input

    def contact_id_validation(self, msg, msg_error):
        self.user_input_from_keyboard(msg)
        if (
            self.user_input.isdigit()
            and self.user_input in self.phonebook.contacts.keys()
        ):
            return int(self.user_input)
        raise IdNotFoundError(msg_error)

    @staticmethod
    def print_start_menu() -> None:
        for i, item in enumerate(MenuItems):
            if not i:
                print(item.value)
            else:
                print(f"\t{i}.{item.value}")

    @staticmethod
    def print_message(msg: str) -> None:
        print("\n" + Fillers.equality.value * len(msg))
        print(msg)
        print(Fillers.equality.value * len(msg) + "\n")

    def show_contacts(self):
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
