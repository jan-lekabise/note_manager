names_of_note = []
yes_no = input('Создать имя записки? "Да" или "Нет": ')
while yes_no.upper() == "ДА":
    names_of_note.append(input("Введите имя записки: "))
    yes_no = input('Создать имя записки? "Да" или "Нет": ')

print(names_of_note)