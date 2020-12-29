def int_func(text):

    my_str = (text)
    my_list = list(my_str)
    my_list.reverse()
    my_list[-1] = my_list[-1].title()
    my_list.reverse()
    my_str = ''.join(my_list)

    print(my_str)

    print(my_str.title())

int_func(input('Введите в строку словосочетание,\n разделив его слова пробелом,'
               '\n состоящее из слов,\n состоящих из маленьких букв: '))