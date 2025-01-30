class CustomException(Exception):
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
