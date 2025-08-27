import pytest

from Homework_3_Testing.model.custom_exceptions import WrongNameError
from Homework_3_Testing.view.view import Console
from Homework_3_Testing.model.phonebook import Phonebook
from Homework_3_Testing.model.custom_exceptions import (
    WrongMenuInputError,
    WrongNumberFormatError,
    IdNotFoundError,
)
from Homework_3_Testing.model.data_ru import *


class TestConsole:

    @pytest.mark.parametrize(
        "user_input, expected",
        [
            ("1", 1),
            ("0", wrong_menu_input_error_msg),
            ("10", wrong_menu_input_error_msg),
            ("Gasd", wrong_menu_input_error_msg),
            (True, wrong_menu_input_error_msg),
            ("@#$", wrong_menu_input_error_msg),
        ],
    )
    def test_menu_input_validation(self, user_input, expected):
        console = Console(Phonebook())
        console.user_input = user_input

        try:
            assert console.menu_input_validation() == expected
        except WrongMenuInputError as e:
            assert e.__str__() == expected
        except AttributeError:
            pass

    @pytest.mark.parametrize(
        "user_input, msg_error_test, name_val_test, number_val_test, key_id_test, expected",
        [
            ("Сергей", None, False, False, None, "Сергей"),
            ("Сергей", None, True, False, None, "Сергей"),
            (
                "Сергей123",
                wrong_name_error_msg,
                True,
                False,
                None,
                wrong_name_error_msg,
            ),
            (
                "Сергей###",
                wrong_name_error_msg,
                True,
                False,
                None,
                wrong_name_error_msg,
            ),
            (
                "",
                wrong_first_name_error_msg,
                True,
                False,
                None,
                wrong_first_name_error_msg,
            ),
            ("", None, True, False, 1, "Миша"),
            ("3333333331", None, False, True, None, "3333333331"),
            (
                "33333333311",
                wrong_number_format_error_msg,
                False,
                True,
                None,
                wrong_number_format_error_msg,
            ),
            (
                "333333333f",
                wrong_number_format_error_msg,
                False,
                True,
                None,
                wrong_number_format_error_msg,
            ),
            ("", None, False, True, 1, "1231231231"),
        ],
    )
    def test_contact_validation(
        self,
        data_book_short,
        user_input,
        msg_error_test,
        name_val_test,
        number_val_test,
        key_id_test,
        expected,
    ):
        console = Console(data_book_short)
        console.user_input = user_input

        try:

            assert (
                console.contact_validation(
                    msg_error_test,
                    name_val_test,
                    number_val_test,
                    key_id_test,
                )
                == expected
            )
        except WrongNameError as e:
            assert e.__str__() == expected
        except WrongNumberFormatError as e:
            assert e.__str__() == expected

    @pytest.mark.parametrize(
        "user_input, expected",
        [
            ("1", 1),
            ("35", wrong_id_msg),
            ("qwe", wrong_id_msg),
            ("###", wrong_id_msg),
        ],
    )
    def test_contact_id_validation(self, data_book_short, user_input, expected):
        console = Console(data_book_short)
        console.user_input = user_input
        try:
            console.contact_id_validation(wrong_id_msg) == expected
        except IdNotFoundError as e:
            assert e.__str__() == expected
