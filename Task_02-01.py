my_list = ['Oleg', 40, 'Nadya', 29, 'Vova', 8, 'Vanya', 3, 'Vasya', 0]
my_list.reverse()
while len(my_list) > 0:
     out = my_list.pop()
     print(out, 'ИМЕЕТ ТИП ДАННЫХ:', type(out))