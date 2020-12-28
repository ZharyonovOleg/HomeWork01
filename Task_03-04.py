print('1 вариант: ')

def my_func_1(x, y):
    while y >= 0 or y != int(y):
        print('Вы ввели не отрицательное или не целое отрицательное число')
        y = float(input('Введите второе целое отрицательное число: '))
    return (x ** y) # или return pow(x, y)
print(my_func_1(float(input('Введите первое действительное число: ')),
              (float(input('Введите второе целое отрицательное число: ')))))

print(" ")
print('2 вариант: ')
print(" ")

def my_func_2(x, y):
    while y >= 0 or y != int(y):
        print('Вы ввели не отрицательное или не целое отрицательное число')
        y = float(input('Введите второе целое отрицательное число: '))
    if y < 0:
        x = (1.0 / x)
        y = -y
    res = 1
    while y > 0:
        res = res * x
        y = y - 1
    return res
print(my_func_2(float(input('Введите первое действительное число: ')),
              (float(input('Введите второе целое отрицательное число: ')))))