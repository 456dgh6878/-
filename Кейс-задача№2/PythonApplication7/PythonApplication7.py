year = int(input('Введите год своего рождения:'))
month = int(input('Введите месяц своего рождения:'))
day = int(input('Введите день своего рождения:'))
import calendar
from datetime import datetime
def day_week():
# weekday() возвращает индекс дня недели для заданной даты
    dayday = calendar.weekday(year, month, day)
    wh = calendar.weekheader(9).split()
    print(wh[dayday]) 
def year_wis():
# Является ли год високосным
    if calendar.isleap(year):
        print("Год высокосный")
    else:
        print("Год не высокосный")
def age():
# Выводит кол-во целых лет
    current_datetime = datetime.now()
    newyear =int(current_datetime.year)
    a = newyear - year
    print(a)
stryear = str(year)
strmonth = str(month)
strday = str(day)
day_week()
year_wis()
age()
# Выодит дату в рамке из звездочек
s = stryear + "." + strmonth + "." + strday
w = 30

print('\n'.join(['*' * w, '*{:^{wid}}*'.format(s, wid=w-2), '*' * w]))

