import os

PATH = 'Phone_book.txt'
DELIMITER: str = ';'
FILLERS: list = [' ', '*', '_']
ph_contacts: dict = {}
ph_status: bool = False
menu_items: list = ['Главное меню',
                    'Открыть файл',
                    'Сохранить файл',
                    'Создать контакт',
                    'Показать все контакты',
                    'Найти контакт',
                    'Изменить контакт',
                    'Удалить контакт',
                    'Выход']


def _show_menu():
    """Вывести в консоль главное меню с вариантами выбора"""
    for i, item in enumerate(menu_items):
        if not i:
            print(item)
        else:
            print(f'\t{i}.{item}')


def _input_validation(msg : str, error_msg : str) -> int:
    """Проверить правильность вводы пользователя в меню

    :param msg: arg1
    :param error_msg: arg2
    :return: Число, соответствующее выбору пользователя
    """
    user_choice = input(msg)
    if user_choice.isdigit() and 0 < int(user_choice) < len(menu_items):
        return int(user_choice)
    print(error_msg)


def _star_menu():
    """Запустить дерево выбора для пользователя"""
    menu_cycle = True
    while menu_cycle:
        _show_menu()
        _menu_choice = _input_validation(
            '\nВведите пункт меню: ',
            f'Введеный номер некооректен. Введите целое число от 1 до {len(menu_items) - 1}'
        )
        if _menu_choice == 1:
            print(_open_pb())
        elif _menu_choice == 2:
            _safe_pb('Телефонный справочник не был открыт.\nОткройте телефонный справочник')
        elif _menu_choice == 3:
            _create_contact()
        elif _menu_choice == 4:
            _show_contacts(ph_contacts,
                           'Телефонный справочник не был открыт.\nОткройте телефонный справочник')
        elif _menu_choice == 5:
            _find_contact()
        elif _menu_choice == 6:
            _change_contact()
        elif _menu_choice == 7:
            _delete_contact()
        elif _menu_choice == 8:
            _user_choise = input('Если хотете сохранить изменения перед выхожом введите "Да"\n'
                                 'Если просто хотите выйти введите любой символ: ')
            if _user_choise.lower() == 'да' and _user_choise is str:
                _safe_pb('Телефонный справочник не был открыт.\nОткройте телефонный справочник')
            menu_cycle = False


def _open_pb():
    """Открыть текстовый файл"""
    global ph_contacts
    if os.path.exists(PATH) is False:
        _user_decision = input('Телефонный справочник не создан.\n'
                               'Введите "Да", если хотете создать контакт.\n'
                               'Если хотите вернуться в меню, введите что-нибудь. Лол ')
        if _user_decision.lower() == 'да':
            _create_contact()
    else:
        with open(PATH, 'r', encoding='utf-8') as data_file:
            ph_contacts = {user_id: line.strip().split(DELIMITER) for user_id, line in enumerate(data_file, 1)}
            print(ph_contacts)
        return '\nТелефонная книга успешно открыта!\n'


def _safe_pb(msg_error: str):
    """Перезаписать изменения в файл.

    :param msg_error: Сообщение об ошибке
    """
    _data_list = []

    if ph_contacts:

        with open(PATH, 'w', encoding='utf-8') as data_file:
            for key in ph_contacts:
                _data_list.append(DELIMITER.join(ph_contacts[key]).strip())

            data = '\n'.join(_data_list)
            data_file.write(data)
            print('Телефонный справочник обновлен')

    else:
        print('\n' + msg_error + '\n')


def _show_contacts(dict_contacts: dict, msg_error: str, table_id=False):
    """Вывести список контактов в консоль

    :param dict_contacts: Список контактов
    :param msg_error: сообщение об ошибке, при выводе
    :param table_id: необходимость выводить ID контакта
    """
    _table_size = 96
    _id_size = 5
    _id_tittle = 'ID'
    _ph_name_tittle = 'Имя'
    _ph_number_tittle = 'Номер телефона'
    _ph_comment_tittle = 'Комментарий'
    _table_borders = '\n' + FILLERS[2] * _table_size

    _name_tittle_size = _number_tittle_size = _comment_tittle_size = int(_table_size / 3)

    _table_core = (_ph_name_tittle + (_name_tittle_size - len(_ph_name_tittle)) * FILLERS[0] +
                   _ph_number_tittle + (_number_tittle_size - len(_ph_number_tittle)) * FILLERS[0] + _ph_comment_tittle
                   + (_comment_tittle_size - len(_ph_comment_tittle)) * FILLERS[0])

    if dict_contacts:
        if table_id is False:
            print(_table_borders + '\n' + _table_core)

            for data in dict_contacts.values():
                _name = data[0].strip()
                _number = data[1].strip()
                _comment = data[2].strip()
                print(f'{_name:<32}' + f'{_number:<32}' + f'{_comment:<32}')

            print(_table_borders)

        else:
            print(_id_size * FILLERS[0] + _table_borders + '\n' + _id_tittle + (_id_size - len(_id_tittle)) * FILLERS[0]
                  + _table_core)

            for key in dict_contacts:
                _id = key
                _contact = dict_contacts[key]

                print(f'{_id:<5}' + f'{_contact[0].strip():<32}'
                      + f'{_contact[1].strip():<32}'
                      + f'{_contact[2].strip():<32}')

            print(_table_borders)

    else:
        print('\n' + msg_error + '\n')


def _create_contact():
    """Создать новый контакт в буфере"""
    _new_key = 1

    if ph_contacts:
        user_name = input_check('name')
        if user_name == '8':
            return print('Создание контакта отменено')
        user_number = input_check('number')
        if user_number == '8':
            return print('Создание контакта отменено')
        user_comment = input_check('comment')

        new_contact = [user_name, user_number, user_comment]

        list_of_keys = {key for key in ph_contacts}
        while _new_key in list_of_keys:
            _new_key += 1
        print(_new_key)
        ph_contacts.update({_new_key: new_contact})
        print(ph_contacts)

        _user_decision = input('Введите "Да", если хотете создать контакт.\n'
                               'Если хотите вернуться в меню, введите что-нибудь. Лол ')
        if _user_decision.lower() == 'да':
            _create_contact()

        else:
            if input('ведите "Да", если хотете создать контакт.\n'
                     'Если хотите вернуться в меню, введите что-нибудь. Лол ').lower() == 'да':
                _safe_pb('Телефонный справочник не был открыт.\nОткройте телефонный справочник')
            else:
                return print('Контакт(ы) успешно создан')

    else:
        print('\n' + 'Телефонный справочник не открыт. Создание новых контактов может привести \n'
                     'к потере данных. Для корректной работы необходимо сначала открыть справочник' + '\n')


def input_check(data: str) -> str:
    """Проверить формат ввода для контакта

    :param data: Поле выбора для проверки формата одного из полей справочника
    :return: Введение данные в соответствии с форматом
    """
    if data == 'name':
        name = input('Введите имя: ')
        while any(character.isdigit() for character in name.strip()) or name.replace(' ', '') == '':
            name = input('Имя не может содержать цифры. Повторно введите имя или введите 8 для возврата в меню: ')
            if name == '8':
                return '8'

        name = ' '.join(name.title().strip().split())
        return name
    elif data == 'number':
        number = input('Введите телефонный номер: +7')
        while len(number) != 10 or not number.isdigit():
            number = input(
                'Номер должен содержать не более десяти цифр. Повторно введите номер или введите 8 для возврата в меню: ')
            if number == '8':
                return '8'
        return number
    elif data == 'comment':
        comment = input('Введите комментарий: ')
        return comment


def _find_contact():
    """Найти контакт в буфере"""
    _set_of_keys = set()
    _list_of_contacts = []

    _user_search = input('Введите ключевое слово для поиска: ')

    for key in ph_contacts:
        for item in ph_contacts[key]:
            if _user_search in item:
                _set_of_keys.add(key)

    for key in list(_set_of_keys):
        _list_of_contacts.append(ph_contacts[key])

    _looking_contacts = {contact_id: contact for contact_id, contact in zip(list(_set_of_keys), _list_of_contacts)}
    _show_contacts(_looking_contacts, 'Ну ты даешь', table_id=True)

    _user_choice = input('Введите 1, если хотите изменить контакт.\n\n'
                         'Введите 2, если хотите удалить контакт.\n\n'
                         'Введите любой другой символ, если хотите вернуться в главное меню: ')

    if _user_choice.isdigit() and int(_user_choice) == 1:
        _change_contact()
    elif _user_choice.isdigit() and int(_user_choice) == 2:
        _delete_contact()


def _change_contact():
    """Изменить контакт в буфере"""
    if ph_contacts:
        _user_choice = input('Введите ID, которого хотите изменить, '
                             'или введите любой символ для поиска контакта по ключевому слову: ')

        if _user_choice.isdigit() and int(_user_choice) in ph_contacts.keys():

            _user_name = input_check('name')
            if _user_name == '8':
                return print('Создание контакта отменено')
            _user_number = input_check('number')
            if _user_number == '8':
                return print('Создание контакта отменено')
            _user_comment = input_check('comment')

            _changed_contact = [_user_name, _user_number, _user_comment]

            ph_contacts[int(_user_choice)] = _changed_contact

        elif _user_choice.isdigit() and int(_user_choice) not in ph_contacts.keys():
            print('Контакта с таким ID не существует')
            _change_contact()
        else:
            _find_contact()
    else:

        print('\n' + 'Телефонный справочник закрыт. Откройте телефонный справочник' + '\n')


def _delete_contact():
    """Удалить контакт из буфера"""
    if ph_contacts:
        _user_choice = input('Введите ID, которого хотите удалить, '
                             'или введите любой символ для поиска контакта по ключевому слову: ')

        if _user_choice.isdigit() and int(_user_choice) in ph_contacts.keys():

            print(f'Контакт {ph_contacts.pop(int(_user_choice))} удален')

        elif _user_choice.isdigit() and int(_user_choice) not in ph_contacts.keys():
            print('Контакта с таким ID не существует')
            _delete_contact()
        else:
            _find_contact()
    else:

        print('\n' + 'Телефонный справочник закрыт. Откройте телефонный справочник' + '\n')


_star_menu()
