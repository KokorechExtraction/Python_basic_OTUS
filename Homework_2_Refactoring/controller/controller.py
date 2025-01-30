from os import cpu_count

from Homework_2_Refactoring.model.contact import Contact
from Homework_2_Refactoring.model.custom_exceptions import (
    WrongMenuInputError,
    WrongFormatError,
    WrongNameError,
    WrongNumberFormatError,
    ContactNotFoundError,
    CreationContactError,
    IdNotFoundError,
)
from Homework_2_Refactoring.view.view import Console
from Homework_2_Refactoring.model.phonebook import Phonebook
from Homework_2_Refactoring.model.model import (
    add_to_buffer_from_file,
    contact_to_str,
    contact_to_json,
    create_contact,
    find_contact,
    change_contact,
    delete_contact,
)
from Homework_2_Refactoring.model.ioclass import Reader, Writer
from Homework_2_Refactoring.model.data_ru import *


def start_menu():
    exit_status = True
    phonebook = Phonebook()
    console = Console(phonebook)
    reader = Reader(phonebook)
    writer = Writer(phonebook)
    while exit_status:
        console.print_start_menu()
        console.user_input_from_keyboard(input_menu_msg)
        try:
            console.menu_input_validation()
        except WrongMenuInputError as e:
            console.print_message(e.__str__())
        match console.user_input:
            case UserChoice.open_file.value:
                try:
                    add_to_buffer_from_file(phonebook, reader)
                except FileNotFoundError:
                    console.print_message(phone_book_does_not_exist)
                else:
                    console.print_message(phone_book_is_open)
            case UserChoice.show_contacts.value:
                console.show_contacts()
            case UserChoice.save_file.value:
                try:
                    if writer.format_check():
                        contact_to_str(phonebook, writer)
                        writer.save()
                    else:
                        contact_to_json(phonebook, writer)
                        writer.save()
                    console.print_message(phone_book_is_saved)
                except WrongFormatError as e:
                    console.print_message(e.__str__())
            case UserChoice.create_contact.value:
                try:
                    create_contact(
                        phonebook,
                        console.contact_validation(
                            enter_the_first_name, wrong_name_error_msg, name_val=True
                        ),
                        console.contact_validation(
                            enter_the_number,
                            wrong_number_format_error_msg,
                            number_val=True,
                        ),
                        console.contact_validation(enter_the_comment),
                    )
                    console.print_message(creation_successful_msg)
                except WrongNameError as e:
                    console.print_message(e.__str__())
                except WrongNumberFormatError as e:
                    console.print_message(e.__str__())

            case UserChoice.find_contact.value:
                try:
                    console.user_input_from_keyboard(enter_the_key_word)
                    console.show_contacts_with_id(
                        find_contact(
                            phonebook,
                            console.user_input.lower(),
                        )
                    )
                except ContactNotFoundError as e:
                    console.print_message(e.__str__())

            case UserChoice.change_contact.value:
                try:
                    changed_id = console.contact_id_validation(
                        enter_Id_to_change, wrong_id_msg
                    )
                    changed_name = console.contact_validation(
                        enter_the_first_name_to_cng,
                        wrong_name_error_msg,
                        name_val=True,
                        key_id=changed_id,
                    )

                    changed_number = console.contact_validation(
                        enter_the_number,
                        wrong_number_format_error_msg,
                        number_val=True,
                        key_id=changed_id,
                    )
                    changed_comment = console.contact_validation(enter_the_comment)
                    change_contact(
                        phonebook,
                        changed_id,
                        changed_name,
                        changed_number,
                        changed_comment,
                    )
                    console.print_message(changing_successful_msg)

                except ContactNotFoundError as e:
                    console.print_message(e.__str__())
                except WrongNameError as e:
                    console.print_message(e.__str__())
                except WrongNumberFormatError as e:
                    console.print_message(e.__str__())
                except IdNotFoundError as e:
                    console.print_message(e.__str__())

            case UserChoice.delete_contact.value:
                try:
                    changed_id = console.contact_id_validation(
                        enter_Id_to_delete, wrong_id_msg
                    )
                    delete_contact(phonebook, changed_id)
                    console.print_message(deletion_successful)
                except IdNotFoundError as e:
                    console.print_message(e.__str__())
                except ContactNotFoundError as e:
                    console.print_message(e.__str__())

            case UserChoice.exit_phone_book.value:
                exit_status = False
