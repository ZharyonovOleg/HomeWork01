import math

def fact(n):
    print('Факториал числа', n, 'равен:', math.factorial(n), '. Множители:')
    x = 0
    while True:
        x += 1
        if x == n + 1:
            break
        yield x

g_obj = fact(int(input('Введите факториал какого числа нужно найти: ')))
for i in g_obj:
    print(i)