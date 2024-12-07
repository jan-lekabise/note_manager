titles = []
yes_no = input('\nСоздать имя заметки? "Да" или "Нет": ')

while yes_no.upper() == "ДА":
        titles.append(input("Введите имя заметки: "))
        yes_no = input('Создать имя заметки? "Да" или "Нет": ')

print(titles)