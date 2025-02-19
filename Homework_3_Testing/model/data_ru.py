from enum import Enum


wrong_menu_input_error_msg = "Неверный формат ввода. Введите число от 1 до 8"
wrong_format_msg = (
    "Формат не поддерживается. Телефонный справочник может взаимодействовать "
    "только с форматами .txt или .json"
)
wrong_name_error_msg = "Имя не может содержать цифры"
wrong_first_name_error_msg = "Имя контакта не может быть пустым"
wrong_number_format_error_msg = "Номер должен содержать десять цифр"
phone_book_does_not_exist = (
    "В указанной директории телефонного справочника не существует"
)
creation_successful_msg = "Контакт успешно создан!"
changing_successful_msg = "Контакт успешно изменен!"
deletion_successful = "Контакт успешно удален!"
contact_not_found_msg = "Поиск по ключевому слову завершен. Контакт не найден"
wrong_id_msg = "Контакта с таким ID не существует"
input_menu_msg = "\nВведите пункт меню: "
phone_book_is_open = "Телефонный справочник открыт"
phone_book_is_saved = "Телефонный справочник успешно сохранен"
enter_the_first_name = "Введите имя контакта: "
enter_the_first_name_to_cng = (
    "Введите имя контакта (при необходимости) или нажмите Enter: "
)
enter_the_number = "Введите телефонный номер в формате +7 ХХХ ХХХ ХХ ХХ: "
enter_the_comment = "Введите комментарий (при необходимости) или нажмите Enter: "
enter_the_key_word = "Введите ключевое слова для поиска контакта: "
enter_Id_to_change = "Введите ID контакта, который хотите изменить: "
enter_Id_to_delete = "Введите ID контакта, который хотите удалить: "

PATH: str = "phone_book.txt"
DELIMITER: str = ";"


class MenuItems(Enum):
    main_menu = "Главное меню"
    open_file = "Открыть файл"
    save_file = "Сохранить файл"
    create_contact = "Создать контакт"
    show_contacts = "Показать все контакты"
    find_contact = "Найти контакт"
    change_contact = "Изменить контакт"
    delete_contact = "Удалить контакт"
    exit_phone_book = "Выход"


class Fillers(Enum):
    space = " "
    star = "*"
    low_case_line = "_"
    equality = "="


class TableStuf(Enum):
    id_tittle = "ID"
    name_tittle = "Имя"
    number_tittle = "Номер телефона"
    comment_tittle = "Комментарий"


class UserChoice(Enum):
    open_file = "1"
    save_file = "2"
    create_contact = "3"
    show_contacts = "4"
    find_contact = "5"
    change_contact = "6"
    delete_contact = "7"
    exit_phone_book = "8"
