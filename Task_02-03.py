########  Task_2.3  ########

month = int(input('Введите номер месяца: '))

if month <=0 or month >= 13:
    print('Вы ввели несуществующий месяц')
    month = int(input('Введите номер месяца: '))
if month <=5 and month >= 3:
    print('Вы ввели весенний месяц')
if month <=8 and month >= 6:
    print('Вы ввели летний месяц')
if month <= 11 and month >= 9:
    print('Вы ввели осенний месяц')
if month <=2 and month >= 1:
    print('Вы ввели зимний месяц')
if month == 1:
    print('Вы ввели зимний месяц')