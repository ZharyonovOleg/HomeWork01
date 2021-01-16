
import re

with open('05-04-01.txt') as funk:
    my_lines = funk.readlines()
    # print(my_lines)

with open('05-04-02.txt', 'w', encoding='utf-8') as funk_2:
    for el in my_lines:
        x = int(re.sub(r'\D', "", el[el.find(' ') + 1:]))
        if x == 1:
            funk_2.write('Один - 4' + '\n')
        elif x == 2:
            funk_2.write('Два - 2' + '\n')
        elif x == 3:
            funk_2.write('Три - 3' + '\n')
        elif x == 4:
            funk_2.write('Четыре - 4')

with open('05-04-02.txt') as funk:
    my_lines = funk.readlines()
print(my_lines) # не выдаёт юникод