from Homework_3_Testing.model.model import Phonebook

import pytest


class TestPhonebook:

    @pytest.mark.parametrize(
        "path, expected",
        [
            ("phonebook.txt", "phonebook.txt"),
            ("phonebook.json", "phonebook.json"),
            (123, 123),
            ("Homework_3_Testing\phonebook.txt", "Homework_3_Testing\phonebook.txt"),
            ("phonebook.txt", "phonebook.txt"),
            ("phonebook.txt", "phonebook.txt"),
        ],
    )
    def test_path(self, path, expected):
        phonebook = Phonebook(path)
        assert phonebook.path == expected

    def test_contacts(self, data_phonebook, data_phonebook_dict):
        assert data_phonebook.contacts == data_phonebook_dict
