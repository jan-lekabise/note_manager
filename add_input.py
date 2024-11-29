title = input("Введите заголовок заметки:")

print("\nВведите формат даты: 00.00.0000 - день-месяц-год")

day_to_input = input("Введите день:")
month_to_input = input("Введите месяц:")
year_to_input = input("Введите год:")
date=day_to_input+"."+month_to_input+"."+year_to_input

print(title, " (", date,")" )