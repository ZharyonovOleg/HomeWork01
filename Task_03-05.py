numbers = input('Введите в строку несколько чисел, разделив их пробелом. Выход - клавиша "Q": ')
my_list = list(numbers.split(' '))
my_sum = 0
while True:
    if my_list[-1].upper() != 'Q':
        while len(my_list) > 0:
            my_sum = (my_sum + (int(my_list.pop())))
        print('Сумма введённых чисел равна: ', my_sum)
        numbers = input('Введите в строку ещё несколько чисел, разделив их пробелом. Выход - клавиша "Q": ')
        my_list = list(numbers.split(' '))
    else:
        my_list.pop()
        while len(my_list) > 0:
            my_sum = (my_sum + (int(my_list.pop())))
        print('Вы вышли из программы!!!')
        print('Сумма введённых чисел в итоге равна: ', my_sum)
        break

# ПРОБОВАЛ ЧЕРЕЗ ФУНКЦИЮ, НО НЕ СМОГ ЗАЦИКЛИТЬ
#
# def total_sum(numbers):
#
#     if numbers.upper() != 'Q':
#         my_list = list(numbers.split(' '))
#         my_sum = 0
#         if my_list[-1].upper() != 'Q':
#             while len(my_list) > 0:
#                 my_sum = (my_sum + (int(my_list.pop())))
#             return(my_sum)
#         else:
#             my_list.pop()
#             while len(my_list) > 0:
#                 my_sum = (my_sum + (int(my_list.pop())))
#             print('Вы вышли из программы!!!')
#             return(my_sum)
#
#     else:
#         print('Вы вышли из программы')
#
# print('Сумма введённых Вами чисел равна: ',
#       total_sum(input('Введите в строку несколько чисел, разделив их пробелом. Выход - клавиша "Q": ')))