####################   LESSON 4   ########################

# import my_module

# my_module.my_func(5, 9)
# my_module.my_pow(5, 9)

# import my_module as lib
#
# lib.my_func(5 ,9)
# lib.my_pow(5, 9)

# from my_module import my_func, my_pow
#
# my_func(5, 9)
# my_pow(5, 9)

# from my_module import * # импортируем все функции. Сначала делается импорт, потом функции, а только потом остальное решение
#
# my_func(5, 9)
# my_pow(5, 9)

# import time
# print(time.time()) # время в секундах от 01.01.1970


# import time
#
# start_time = time.time()
# for x in range(10000000):
#     pass
# end_time = time.time()
# print(end_time - start_time)

# import time
#
# print(time.localtime()) # текущее время на компе

# import time
#
# print('qwe')
# time.sleep(3) # сколько секунд спать до следующей команды
# print('asd')


# import math
# print(math.pi) # число Пи
# print(math.floor(2.6)) # округление до меньшего целого
# print(math.ceil(2.6)) # округление до большего целого


# import sys
# for i in sys.path:
#     print(i) # список путей модулей

# import sys
# sys.path.insert(0, 'new_path') # добааление модулей из другого пути 'new_path'
# for i in sys.path:
#     print(i) # список путей модулей

# import sys # что то делать через командную строку, то есть запуск скрипта с параметрами
# import time
# if 'h' in sys.argv[1:]:
#     print('передайте два пути для резервного копирования через пробел')
# else:
#     copy_from, copy_to = sys.argv[1:]
#     print(f'Копирую из {copy_from} в {copy_to}...')
#     time.sleep(4)
#     print('Done!')

###ГЕНЕРАТОРЫ:
# my_list = [1, 6, 8, 9, 4] # для списков
#
# new_list = [x ** 3 + 1 for x in my_list if x >= 5]
# print(new_list)

# my_list = [1, 6, 8, 9, 4] # для словарей
#
# new_dict = {x: x ** 3 + 1 for x in my_list if x >= 5} # или # или new_dict = {x: x ** 3 + 1 for x in range(5, 10)}
# print(new_dict)

# my_list = [1, 6, 8, 9, 4] # для множеств
#
# new_set = {x ** 3 + 1 for x in my_list if x >= 5} # или new_set = {x ** 3 + 1 for x in range(5, 10)}
# print(new_set)

# my_list = [1, 6, 8, 9, 4] # для кортежей пока не работает, вернёмся позже!!!!
#
# new_tuple = (x ** 3 + 1 for x in my_list if x >= 5)
# print(new_tuple)


# def generator():
#     x = 0
#     while True:
#         x += 1
#         yield x # выплюнул объект, а если ретёрн,то это уже функция
#
# g_obj = generator()
# for i in g_obj:
#     print(i)


# import random
# print(random.random())
# print(random.randint(5, 10)) # создаются случайные числа от 5 (включительно) до 10 (включительно)
# print(random.randrange(10, 20, 3)) # создаются случайные числа от 10 (включительно) до 20 (включительно) с шагом 3
# # random.seed(10) # для фиксации и передачи на вход


# from functools import reduce, partial
# print(reduce(lambda x, y: x + y, [10, 20, 30])) # выполняется так 10+20=30+30=60

# from functools import reduce, partial
# def my_f(p1, p2):
#     return p1 * p2
# new_f = partial(my_f, 2) # частичная передача
# print(new_f(4))


# from itertools import count, cycle

# for i in count(2): # начинает с 2
#     print(i)
#     if i == 5:
#         break

# for i in cycle('RGY'): # повторяет RGY
#     print(i)