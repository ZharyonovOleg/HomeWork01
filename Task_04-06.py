from itertools import count, cycle

print('Первый список: ')
for i in count(3):
    print(i)
    if i == 10:
        break

print('Второй список: ')
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
for i in cycle(my_list):
    print(i)
    if i == 11:
        break