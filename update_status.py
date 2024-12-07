notes_dict = {}

status_true = True
while status_true:
    note_status = input('Введите статус заметки: '
                        '\n"1" - выполнено'
                        '\n"2" - в процессе'
                        '\n"3" - отложено'
                        '\n-> ')

    if note_status == '1' or note_status == 'выполнено':
        notes_dict['Название заметки'] = 'выполнено'
        status_true = False
    elif note_status == '2' or note_status == 'в процессе':
        notes_dict['Название заметки'] = 'в процессе'
        status_true = False
    elif note_status == '3' or note_status == 'отложено':
        notes_dict['Название заметки'] = 'отложено'
        status_true = False
    else:
        print('Попробуйте снова')

print(notes_dict)

change_status = input('Изменить статус заметки?'
                      '\n"Да" или "Нет"\n')
if change_status.upper() == 'ДА':
    status_true = True
    while status_true:
        note_status = input('Введите статус заметки: '
                            '\n"1" - выполнено'
                            '\n"2" - в процессе'
                            '\n"3" - отложено'
                            '\n-> ')

        if note_status == '1' or note_status == 'выполнено':
            notes_dict['Название заметки'] = 'выполнено'
            status_true = False
        elif note_status == '2' or note_status == 'в процессе':
            notes_dict['Название заметки'] = 'в процессе'
            status_true = False
        elif note_status == '3' or note_status == 'отложено':
            notes_dict['Название заметки'] = 'отложено'
            status_true = False
        else:
            print('Попробуйте снова')

print(notes_dict)
