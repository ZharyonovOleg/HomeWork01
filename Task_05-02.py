f_obj = open('05-02.txt')

my_lines = f_obj.readlines()

print('Количество строк в файле = ', len(my_lines))

for x, y in enumerate(my_lines):
    print((x + 1), 'строка содержит - ', len(y.split()), 'слов')
f_obj.close()