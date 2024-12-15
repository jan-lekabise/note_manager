import datetime

print(datetime.date.today())

a = datetime.datetime.today()
print(a)
print(type(a))
b = datetime.datetime.now()
print(b)
print("")

now = datetime.datetime.now()
then = datetime.datetime(2017, 2, 26)
# Кол-во времени между датами.
delta = now - then

print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print("")

seconds = delta.total_seconds()
hours = seconds // 3600

print(hours)

minutes = (seconds // 3600) // 60
print(minutes)