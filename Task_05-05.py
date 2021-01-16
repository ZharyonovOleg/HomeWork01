with open('05-05.txt', 'w', encoding='utf-8') as funk:

    my_lines = []

    while True:
        x = input('Enter line for lines in file, if enter "Space" - EXIT: ')
        if x == '':
            break
        my_lines.append(x + '\n')
    funk.writelines(my_lines)

with open('05-05.txt', encoding='utf-8') as f_obj:
    new_lines = f_obj.readlines()
y = 0
for el in new_lines:
    y += int(el)
print('Сумма введённых чисел равна :', y)