username = (input()) #имя пользователя
title = (input()) #заголовок заметки
content = (input()) #описание заметки
status = (input()) #статус заметки
created_date = (input()) #дата создания заметки в формате
                     # "день-месяц-год", например "10-11-2024"
issue_date = (input()) #дата истечения заметки (дедлайн) в формате
                    # "день-месяц-год", например "10-12-2024"

print("Имя пользователя", username, "\nЗаголовок заметки", title,"\nОписание заметки", content,
        "\nСтатус заметки", status,"\nДата создания заметки", created_date,
      "\nДата истечения заметки", issue_date)
