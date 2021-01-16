####### Some homework 4 ###############

####### Task_04-01 ####### СПОРНО! НЕ РАБОТАЕТ
##
##import sys
##
##hours, salary_p_h, bonus = map(float, sys.argv[1:])
##print('Salary - {}'.format(hours * salary_p_h + bonus))


######### Task_04-02 ######################
#
# my_list = [1, 91, 1, 72, 3, 4, 6]
# print([num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0])

######## Task_04-04 ################
#
# my_list = [1, 91, 1, 72, 3, 4, 6]
# print(([x for x in my_list if my_list.count(x) == 1]))

####### Task_04-06 ############ НЕ ПОНЯТНО
#
# from itertools import cycle
#
# my_list = [1, 91, 1, 72, 3, 4, 6]
#
# iter = cycle(my_list)
# stop = ''
# while stop != 'q':
#     print(next(iter), end='')
#     stop = input()

####### Task_04-07 ############ ОГОНЬ!!!!!! Я не сделал в функцию факториал
#
# from math import factorial
# from itertools import count
#
# def fibo_gen():
#     for el in count(1):           # это бесконечный цикл, начинающийся с 1
#         yield factorial(el)
#
# x = 1
# for i in fibo_gen():
#     print('Factorial {} - {}'.format(x, i))
#     if x == 15:
#         break
#     x += 1



##################### LESSON 05 #############################

# f_obj = open('234.txt', encoding='utf-8') # для виндомс: encoding='utf-8'
#
# # print(f_obj) # ошибка, так как нет файла 234.txt
# # print(f_obj.read())
# # print(f_obj.read)
#
# # for line in f_obj.readlines():
# #     print(line)  # выдаст строки с промежутками  # потому, что print добавляет в конце \n
#
# # for line in f_obj.readlines():
# #     print(line, end='') # некрасивый способ убрать пробелы между строками
#
# # for line in f_obj.readlines():
# #     print(line.strip())  # так лучше убрать пустые строки между непустыми строками
#
# # print(f_obj.readline())  # считывать по строкам
# # print(f_obj.readline())  # считывать по строкам... и так далее по строкам
#
# # for line in f_obj:
# #     print(line.strip()) # опять выдаёт строки без промежутков
#
# ## ВСЕГДА В КОНЦЕ НУЖНО ЗАКРЫВАТЬ ФАЙЛ, С КОТОРЫМ РАБОТАЛ!!!!! ##### так:
# # f_obj.close()


# создать и записать: ###

# f_obj = open('1234.txt', 'w') # создание. Режим w жёстко и без спроса всё перезаписывает
# f_obj.write('qwe\nasd\nzxc') # содержимое созданного
# f_obj.close() # закрытие созданного

# f_obj = open('1234.txt', 'w') # создание
# f_obj.write(' ') # содержимое перезаписывается
# f_obj.close() # закрытие созданного

# f_obj = open('1234.txt', 'w') # создание
# my_lines = ['qwe\n', 'asd\n', 'zxc\n']
# f_obj.writelines(my_lines)
# f_obj.close() # закрытие созданного

### Менеджер контекста ####

# with open('234.txt', encoding='utf-8') as f_obj:
#     print(f_obj.read())
#     print(f_obj.closed) # здесь файл открыт
# print(f_obj.closed) # а здесь, то есть на уровне выше, файл закрыт. Это используется для автоматического закрытия файла

# with open('234.txt', 'w+', encoding='utf-8') as funk:
#     funk.write('qwe\nzxc')
#     funk.seek(0) # переход в нужную позицию в байтах
#     print(funk.read())

# with open('234.txt', 'w+', encoding='utf-8') as funk:
#     funk.write('qwe\nzxc')
#     funk.seek(0) # переход в нужную позицию в байтах
#     print(funk.mode)
#     print(funk.name)
#     print(funk.closed)

# with open("Pyton.txt", "w") as funk:
#     print("Необычная работа функции Print", file=funk) # в данном случае функция принт заполняет файл вроде

# import os
# # # # # # # os.remove('234.txt') # удалить файл
# # # # # # os.rename('234.txt', '345.txt') # переименовать
# # # # # print(os.listdir()) # содержимое текущей папки
# # # #
# # # os.path.isdir(x) # проверка является ли x папкой
# #
# # print(os.listdir())
# # print(os.path.isdir('321'))
# # path1 = r'C:\Users\zhary\PycharmProjects\pythonProject'
# # folder = 'qwe'
# # filename = '01.py'
# # print(os.path.join(path1, folder, filename)) # соединение пути
#
# path1 = r'C:\Users\zhary\PycharmProjects\pythonProject\345.txt'
# print(os.path.split(path1)) # разъединение пути
# print(os.path.split(path1)[1]) # срез (отделение)

############### json ####################

# import json

# data = {'income': {'salary': 50000, 'bonus': [20000, 5000]}}
#
# with open('Gena.json', 'w') as f_json:
#     json.dump(data, f_json)
#
# with open('Gena.json') as funk:
#     data = json.load(funk)
# print(data)
# print(type(data))

#####################

# import shutil
#
# shutil.copy('001.txt', '06101\\001.txt')


# import sys
# # print(sys.path)
# sys.path.insert(0, 'path')
# for x in sys.path:
#     print(x)