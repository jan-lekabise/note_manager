import datetime

date_of_create = datetime.datetime.today()
dictionary_of_notes = {}  # Словарь заметок

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

def create_name_of_note_func():
    names_of_note.append(input("Введите имя заметки: "))
    yes_no = input('Создать имя заметки? "Да" или "Нет": ')
    return yes_no


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


def display_notes(notes):
    for value, p_info in notes.items():
        for key in p_info:
            print(key, p_info[key])
        print("")

print(f"\033[36;2mДобро пожаловать в менеджер заметок!\n\033[m")

username = input("Введите имя пользователя: ")  # имя пользователя

index_of_note = 0  # Индекс создаваемой записи, отображаться не будет, информация для программиста
yes_no = input('Создать заметку? "Да" или "Нет": ')

# Процесс создания словаря записок
while yes_no.upper() == "ДА" or yes_no.upper() == "LF": # Процесс создания словаря записок
    issue_date = create_note_func()

    index_of_note += 1  # Индекс создаваемой записи
    names_of_note = []  # Список всех имён

    yes_no = input('\nСоздать имя заметки? "Да" или "Нет": ')

    while yes_no.upper() == "ДА" or yes_no.upper() == "LF":  # Если пользователь вписывает да в разных регистрах - ему предлагается ввести имя
        names_of_note.append(input("Введите имя заметки: "))
        yes_no = input('Создать имя заметки? "Да" или "Нет": ')

    note = input("\nВведите описание заметки: ")

    notes_information = {"Пользователь:": username,
                         "Наименования:": names_of_note,
                         "Дата создания:": date_of_create.strftime("%d.%m.%Y"),
                         "Дедлайн:": issue_date.strftime("%d.%m.%Y"),
                         "Описание:": note}

    # Словарь информации о заметке
    dictionary_of_notes.update({index_of_note: notes_information})
    # Привязка заметки к определённому индексу

    yes_no = input('\nСоздать заметку? "Да" или "Нет": ')

print('Удалить заметку? "Да" или "Нет": ')

yes_no = input('\n\nПрочитать все заметки? "Да" или "Нет": ')
if yes_no.upper() == "ДА" or yes_no.upper() == "LF":
    display_notes(dictionary_of_notes)

title_for_delete = input("Введите имя заметки")
remove_outer_dict_by_list(dictionary_of_notes, title_for_delete)
