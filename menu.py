import datetime

notes_file = open('my_notes.txt', mode='r+', encoding='utf-8')

date_of_create = datetime.datetime.today()
dictionary_of_notes = {}  # Словарь заметок
index_of_note = 0
enter_from_program = True

print(f"\033[36;2mДобро пожаловать в менеджер заметок!\n\033[m")
username = input("Введите имя пользователя: ")  # имя пользователя


def create_note_func():
    print(f"\nДата создания заметки: {date_of_create.strftime("%d.%m.%Y")}")

    print("\nВведите окончание даты заметки (дедлайн) в числовом формате")

    day_to_input = input("Введите день: ")
    while not day_to_input.isdigit():
        print("\033[91;1mВы ввели не число!\n\033[m")
        day_to_input = input("Введите день: ")

    month_to_input = input("Введите месяц: ")
    while not month_to_input.isdigit():
        print("\033[91;1mВы ввели не число!\n\033[m")
        month_to_input = input("Введите месяц: ")

    year_to_input = input("Введите год: ")
    while not year_to_input.isdigit():
        print("\033[91;1mВы ввели не число!\n\033[m")
        year_to_input = input("Введите год: ")

    issue_date_str = day_to_input + "." + month_to_input + "." + year_to_input
    issue_date = datetime.datetime.strptime(issue_date_str, "%d.%m.%Y")
    day_deadline = abs(issue_date - date_of_create)

    if issue_date < date_of_create:
        print(f"\033[91;1mВы пропустили дедлайн!\n "
              f"С конца дедлайна прошло {day_deadline.days} дней!\033[m")
        return issue_date

    elif day_deadline < datetime.timedelta(days=5):
        print(f"\033[91;1mДо конца дедлайна осталось {day_deadline.days} дней!\033[m")
        return issue_date

    return issue_date


def save_notes_to_file(dictionary, file_name):
    for key, value in dictionary.items():
        file_name.write(f'{key} {value}\n')
    print("\n")


def display_notes(notes):
    print("")
    for outer_key, inner_dict in notes.items():
        for inner_key, value in inner_dict.items():
            if isinstance(value, list):
                print(inner_key)
                for item in value:
                    print(f"\t- {item}")
            else:
                print(f"{inner_key} {value}")
        print("")


def remove_outer_dict_by_list(notes, target_list_items):
    keys_to_delete = []  # Список ключей внешнего словаря, которые нужно будет удалить
    for outer_key, inner_dict in notes.items():
        for inner_key, value in inner_dict.items():
            if isinstance(value, list):
                found_target = False
                for item in value:
                    if item in target_list_items:
                        found_target = True
                        break  # Прерываем цикл, как только нашли target_item
                if found_target:
                    keys_to_delete.append(outer_key)  # Добавляем ключ во внешний словарь, который нужно удалить
                    break  # Выходим из цикла по inner_dict, чтобы не проверять другие ключи

    for key in keys_to_delete:
        del notes[key]

    return notes


while enter_from_program:
    print("\nВыберите номер действия:"
          "\n\033[35;2m1: Создать новую заметку\033[m"
          "\n\033[35;2m2: Показать все заметки\033[m"
          "\n\033[35;2m3: Обновить заметку\033[m"
          "\n\033[35;2m4: Удалить заметку\033[m"
          "\n\033[35;2m5: Найти заметки\033[m"
          "\n\033[35;2m6: Выйти из программы\033[m")

    try:
        number_of_menu = int(input("Выберите номер действия: "))
    except ValueError:
        print("\n\033[91;1m\nВы ввели не число!\n\tВозвращение в меню!\n\033[m")
        continue

    # Создать новую заметку
    if number_of_menu == 1:
        issue_date = create_note_func()
        index_of_note += 1  # Индекс создаваемой записи
        names_of_note = []  # Список всех имён

        while True:
            note_status = input('Введите статус заметки: '
                                '\n"1" - выполнено'
                                '\n"2" - в процессе'
                                '\n"3" - отложено'
                                '\n-> ')

            if note_status == '1' or note_status == 'выполнено':
                status = 'выполнено'
                break
            elif note_status == '2' or note_status == 'в процессе':
                status = 'в процессе'
                break
            elif note_status == '3' or note_status == 'отложено':
                status = 'отложено'
                break
            else:
                print('Попробуйте снова')

        yes_no = input('\nСоздать имя заметки? "Да" или "Нет": ')
        while yes_no.upper() == "ДА" or yes_no.upper() == "LF":  # Если пользователь вписывает да в разных регистрах - ему предлагается ввести имя
            names_of_note.append(input("Введите имя заметки: "))
            yes_no = input('Создать имя заметки? "Да" или "Нет": ')

        note = input("\nВведите описание заметки: ")

        notes_information = {"Пользователь:": username,
                             "Наименования:": names_of_note,
                             "Статус:": status,
                             "Дата создания:": date_of_create.strftime("%d.%m.%Y"),
                             "Дедлайн:": issue_date.strftime("%d.%m.%Y"),
                             "Описание:": note}

        # Словарь информации о заметке
        dictionary_of_notes.update({index_of_note: notes_information})
        save_notes_to_file(notes_information, notes_file)

    # Показать все заметки
    elif number_of_menu == 2:
        if not dictionary_of_notes:
            print("\033[91;1m\nУ вас нет заметок!\n\tВозвращение в меню!\n\033[m")
        else:
            display_notes(dictionary_of_notes)

    # Обновить заметку
    elif number_of_menu == 3:
        print()

    # Удалить заметку
    elif number_of_menu == 4:
        title_for_delete = input("Введите имя заметки")
        remove_outer_dict_by_list(dictionary_of_notes, title_for_delete)
        print()

    # Найти заметки
    elif number_of_menu == 5:
        print()

    # Выйти из программы
    elif number_of_menu == 6:
        notes_file.close()
        exit()

    elif number_of_menu >> 6 or number_of_menu << 1:
        print("\n\033[91;1m\nТакого номера в меню нет!\n\tВозвращение в меню!\n\033[m")

    else:
        print("")
