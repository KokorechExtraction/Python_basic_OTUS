class CustomException(Exception):
    """Класс содержит набор персональных исключений.

    WrongMenuInputError - неправильное значение для переменной выбора пункта меню
    WrongPhoneBookLocation - неправильный путь файла справочника
    WrongFormatError - неправильный формат справочника
    WrongNameError - неправильное имя контакта
    WrongNumberFormatError - неверный формат номера контакта
    ContactNotFoundError - ошибка поиска контакта
    IdNotFoundError - ID контакта не найдено
    CreationContactError - ошибка создания контакта
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"


class WrongMenuInputError(CustomException):
    pass


class WrongPhoneBookLocation(CustomException):
    pass


class WrongFormatError(CustomException):
    pass


class WrongNameError(CustomException):
    pass


class WrongNumberFormatError(CustomException):
    pass


class ContactNotFoundError(CustomException):
    pass


class IdNotFoundError(CustomException):
    pass


class CreationContactError(CustomException):
    pass
