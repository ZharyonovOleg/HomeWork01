f_obj = open('05-01.txt', 'w', encoding='utf-8') # создание
my_lines = []

while True:
    x = input('Enter line for lines in file, if enter "Space" - EXIT: ')
    if x == '':
        break
    my_lines.append(x + '\n')
f_obj.writelines(my_lines)

for line in f_obj:
    print(line.strip()) # !!!!!!!!! не выдаёт на экран, хотя в файл вроде записывает
f_obj.close()