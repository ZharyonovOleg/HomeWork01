ef my_func(n_1, n_2, n_3):
    return (max([(n_1 + n_2), (n_1 + n_3), (n_2 + n_3)]))
print(my_func((int(input('Введите любое первое число: '))),
        (int(input('Введите любое второе число: '))),
        (int(input('Введите любое третье число: ')))))