from Homework_3_Testing.model.model import Contact

import pytest


class TestContact:

    def test_name(self, data_names):
        for name in data_names:
            contact = Contact(name)
            assert contact.name == name

    def test_number(self, data_number):
        for number in data_number:
            contact = Contact("None", number, "None")
            assert contact.number == number

    def test_comment(self, data_names):
        for comment in data_names:
            contact = Contact("None", "None", comment)
            assert contact.comment == comment

    def test_name_setter(self, data_names):
        contact = Contact()
        for name in data_names:
            contact.name = name
            assert contact.name == name

    def test_number_setter(self, data_number):
        contact = Contact()
        for number in data_number:
            contact.number = number
            assert contact.number == number

    def test_comment_setter(self, data_names):
        contact = Contact()
        for comment in data_names:
            contact.comment = comment
            assert contact.comment == comment
