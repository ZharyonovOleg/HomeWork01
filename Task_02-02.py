my_list = [input('Введите первый элемент списка: '),
           input('Введите второй элемент списка: '),
           input('Введите третий элемент списка: '),
           input('Введите четвёртый элемент списка: '),
           input('Введите пятый элемент списка: ')]

my_list[0], my_list[1], my_list[2], my_list[3], my_list[4] = my_list[1], my_list[0], my_list[3], my_list[2], my_list[4]
print(my_list)


#
# range не увидел в методичке
my_list = [input('Введите первый элемент списка: '),
           input('Введите второй элемент списка: '),
           input('Введите третий элемент списка: '),
           input('Введите четвёртый элемент списка: '),
           input('Введите пятый элемент списка: ')]
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)


