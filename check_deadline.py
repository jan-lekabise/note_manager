import datetime

print("Добро пожаловать в менеджер заметок!\n")

username = input("Введите имя пользователя: ")  # имя пользователя
dictionary_of_notes = {}  # Словарь заметок

index_of_note = 0  # Индекс создаваемой записи,
# для удобства пользователя чтоб начиналось с 1
create_note = input('Создать заметку? "Да" или "Нет": ')

if create_note.upper() == "ДА" or create_note.upper() == "LF":
    date_of_create = datetime.datetime.today()
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
    elif day_deadline < datetime.timedelta(days = 5):
        print(f"\033[91;1mДо конца дедлайна осталось {day_deadline.days} дней!\033[m")


    index_of_note = index_of_note + 1  # Индекс создаваемой записи
    notes_information = []  # Вся информация об одной записке с индексом
    names_of_note = []  # Список всех имён

    yes_no = input('\nСоздать имя заметки? "Да" или "Нет": ')
    while yes_no.upper() == "ДА" or create_note.upper() == "LF":  # Если пользователь вписывает да в разных регистрах - ему предлагается ввести имя
        names_of_note.append(input("Введите имя заметки: "))
        yes_no = input('Создать имя заметки? "Да" или "Нет": ')

    note = input("\nВведите описание заметки: ")

    notes_information = ["Имена вашей заметки:", names_of_note, "Дата вашей заметки:", issue_date, "Описание:", note]
    # Список информации о заметке
    dictionary_of_notes = {index_of_note: notes_information}
    # Привязка заметки к определённому индексу
    print("")
    print(dictionary_of_notes)

else:
    print(username + ", зря вы так, а проверить мою работу?")  # Шутка от разработчицы
