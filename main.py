def add_contact(phone_number, name, surname, lastname):
    global phone_book
    new_contact = [name, surname, lastname]
    phone_book[phone_number] = new_contact

def get_name(phone_number):
    global phone_book
    return phone_book[phone_number][0] if phone_number in phone_book else 'NO PHONE'

def get_surname(phone_number):
    global phone_book
    return phone_book[phone_number][1] if phone_number in phone_book else 'NO PHONE'

def get_lastname(phone_number):
    global phone_book
    return phone_book[phone_number][2] if phone_number in phone_book else 'NO PHONE'

def get_phone_search_by_name(name):
    global phone_book
    res_values = list(filter(lambda x: name in x, phone_book.values()))
    res = {i: phone_book[i] for i in phone_book.keys() if phone_book[i] in res_values}
    return res

def get_phone_search_by_sername(sername):
    global phone_book
    res_values = list(filter(lambda x: sername in x, phone_book.values()))
    res = {i: phone_book[i] for i in phone_book.keys() if phone_book[i] in res_values}
    return res

def write_again():
    book_file = open(r'book.txt', 'w')
    for i in phone_book:
        book_file.write(f'{i}: {phone_book[i]}\n')
    book_file.close()

def change_name(number):
    global phone_book
    phone_book[number][0] = input('Введите новое имя: ')

def change_sername(number):
    global phone_book
    phone_book[number][1] = input('Введите новую фамилию: ')

def change_lastname(number):
    global phone_book
    phone_book[number][2] = input('Введите новое отчество: ')


menu = ['1: Добавить контакт', '2: Удалить контакт', '3: Найти контакт по имени',
        '4: Найти контакт по фамилии', '5: Найти контакт по отчеству', '6: Вывести данные о контакте по номеру',
        '7: Вывести все контакты', '8: Обновить книгу', '9: Изменить контакт', '10: завершить работу']

phone_book = {'56789': ['n', 's', 'ln'], '456': ['fdg', 'dfsg', 'gh']}
id_comand = 1
while True:
    print('Возможные команды: ')
    print('\n'.join(menu))
    k = int(input('Введите номер команды: '))
    if id_comand == 1:
        write_again()
    if k == 1:
        p, n, s, ln = input('введите номер: '), input('введите имя: '), input('введите фамилию: '), input('введите отчество: ')
        add_contact(p, n, s, ln)
        book_file = open(r'book.txt', 'a')
        book_file.write(f'{p}: {phone_book[p]}\n')
        book_file.close()
    elif k == 2:
        p = input('введите номер: ')
        if p in phone_book:
            del phone_book[p]
        else:
            print('Контакт отсутствует')
        write_again()
        id_comand += 1
    elif k == 3:
        print(get_phone_search_by_name(input('Введите имя: ')))
        id_comand += 1
    elif k == 4:
        print(get_phone_search_by_sername(input('Введите фамилию: ')))
        id_comand += 1
    elif k == 5:
        print(get_phone_search_by_sername(input('Введите отчество: ')))
        id_comand += 1
    elif k == 6:
        number = input('Введите номер телефона: ')
        print('\nКонтакт:')
        if number not in phone_book:
            print('Отсутствует')
        else:
            print(f'Номер телефона: {number}')
            print(f'Фамилия: {get_surname(number)}')
            print(f'Имя: {get_name(number)}')
            print(f'Отчество: {get_lastname(number)}')
        id_comand += 1
    elif k == 7:
        for i in phone_book.keys():
            print(f'\n*****\nКонтакт: {i}\nФамилия: {get_surname(i)}\nИмя: {get_name(i)}\n'
                  f'Отчество: {get_lastname(i)}\n*****')
        id_comand += 1
    elif k == 8:
        write_again()
        id_comand += 1
    elif k == 9:
        print('Что вы хотите изменить? (введите номер команды):')
        k = int(input('1: имя\n2:фамилия\n3:отчество\n'))
        if k == 1:
            change_name(input('Введите номер телефона:\n'))
        elif k == 2:
            change_sername(input('Введите номер телефона:\n'))
        elif k == 3:
            change_lastname(input('Введите номер телефона:\n'))
        else:
            print('Команда отсутствует. Повторите попытку.')
        write_again()
        id_comand += 1
    elif k == 10:
        print('__Завершение работы__')
        id_comand = 1
        break
    else:
        print('Команда отсутствует. Повторите попытку.')
    print()








