import datetime

date_of_create = datetime.datetime.today()
dictionary_of_notes = {}  # Словарь заметок

def create_note_func():
    print(f"\nДата создания заметки: {date_of_create.strftime("%d.%m.%Y")}")

    print("\nВведите окончание даты заметки (дедлайн)")
    day_to_input = input("Введите день: ")
    month_to_input = input("Введите месяц: ")
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


def create_name_of_note_func():
    names_of_note.append(input("Введите имя заметки: "))
    yes_no = input('Создать имя заметки? "Да" или "Нет": ')
    return yes_no


print(f"\033[36;2mДобро пожаловать в менеджер заметок!\n\033[m")

username = input("Введите имя пользователя: ")  # имя пользователя

index_of_note = 0  # Индекс создаваемой записи,
# для удобства пользователя чтоб начиналось с 1
create_note = input('Создать заметку? "Да" или "Нет": ')

while create_note.upper() == "ДА" or create_note.upper() == "LF":
    issue_date = create_note_func()

    index_of_note = index_of_note + 1  # Индекс создаваемой записи
    notes_information = []  # Вся информация об одной записке с индексом
    names_of_note = []  # Список всех имён

    yes_no = input('\nСоздать имя заметки? "Да" или "Нет": ')

    while yes_no.upper() == "ДА" or yes_no.upper() == "LF":  # Если пользователь вписывает да в разных регистрах - ему предлагается ввести имя
        yes_no = create_name_of_note_func()

    note = input("\nВведите описание заметки: ")

    notes_information = ["Имена вашей заметки:", names_of_note, "Дата вашей заметки:",
                         date_of_create.strftime("%d.%m.%Y"),
                         "Дедлайн:", issue_date.strftime("%d.%m.%Y"), "Описание:", note]
    # Список информации о заметке
    dictionary_of_notes[index_of_note] = {index_of_note : notes_information}
    # Привязка заметки к определённому индексу

    print("")
    print(dictionary_of_notes)

    create_note = input('\n\n\nСоздать заметку? "Да" или "Нет": ')
print(dictionary_of_notes)