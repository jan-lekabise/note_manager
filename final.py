print("Добро пожаловать в менеджер заметок!\n")

username = input("Введите имя пользователя: ") #имя пользователя
users_dictionary_notes = {} #Словарь, содержащий информацию о заметках, принадлежащих одному пользователю
dictionary_of_notes = {} #Словарь заметок

index_of_note = 0 #Индекс создаваемой записи,
            # для удобства пользователя чтоб начиналось с 1
create_note = input('Создать заметку? "Да" или "Нет": ')

if create_note.upper() == "ДА":
    print("\nВведите дату создания заметки\n")
    day_to_input = input("Введите день: ")
    month_to_input = input("Введите месяц: ")
    year_to_input = input("Введите год: ")
    date = day_to_input + "." + month_to_input + "." + year_to_input

    index_of_note = index_of_note + 1 #Индекс создаваемой записи
    notes_information = [] #Вся информация об одной записке с индексом
    names_of_note = [] #Список всех имён

    yes_no = input('\nСоздать имя заметки? "Да" или "Нет": ')
    while yes_no.upper() == "ДА":       #Если пользователь вписывает да в разных регистрах - ему предлагается ввести имя
        names_of_note.append(input("Введите имя заметки: "))
        yes_no = input('Создать имя заметки? "Да" или "Нет": ')

    note = input("\nВведите описание заметки: ")

    notes_information = ["Имена вашей заметки:", names_of_note, "Дата вашей заметки:", date, "Описание:", note]
            # Список информации о заметке
    dictionary_of_notes = {index_of_note: notes_information}
            # Привязка заметки к определённому индексу
    users_dictionary_notes = {username : dictionary_of_notes}
            # Привязка всех записок к одному пользователю, информативная для программиста
    print("")
    print(dictionary_of_notes)

else: print(username + ", зря вы так, а проверить мою работу?") #Шутка от разработчицы