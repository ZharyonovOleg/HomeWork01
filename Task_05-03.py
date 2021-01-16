import re

f_obj = open('05-03.txt')

my_lines = f_obj.readlines()
# print(my_lines)
f_obj.close()
num_empl = len(my_lines)

for el in my_lines:
    if float(re.sub(r'\D', "", el[el.find(' ') + 1:])) > 20000: # решено с помощью гугла re sub \D, НЕ ПОНЯЛ КАК ИЗБАВИТЬСЯ ОТ \n в конце
        print(el[:el.find(' ')], 'зарабатывает больше 20000 рублей')

print('Количество сотрудников, информация о которых содержится в данном файле составляет: ', num_empl)

new_lines = []

for el in my_lines:
    x = float(re.sub(r'\D', "", el[el.find(' ') + 1:]))
    new_lines.append(x)

print('Средняя зарплата указанных сотрудников составляет: ', sum(new_lines) / num_empl)