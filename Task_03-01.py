def division(num_1, num_2):
    while num_2 == 0:
        print('Вы ввели для знаменателя значение "ноль", а на ноль делить нельзя!')
        num_2 = int(input('Введите знаменатель: '))
    print('Ответ: ', round((num_1 / num_2), 3))
division((int(input('Введите числитель: '))), (int(input('Введите знаменатель: '))))