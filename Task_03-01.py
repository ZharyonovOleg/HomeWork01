def division():
    num_1 = int(input('Введите числитель: '))
    num_2 = int(input('Введите знаменатель: '))
    while num_2 == 0:
        print('Вы ввели для знаменателя значение "ноль", а на ноль делить нельзя!')
        num_2 = int(input('Введите знаменатель: '))
    print('Ответ: ', round((num_1 / num_2), 3))

division()