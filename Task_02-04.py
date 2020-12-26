words_str = str(input('Введите фразу минимум из двух слов: '))
spaces = words_str.count(' ')
words_str = words_str[0:(10 + spaces):]
words_list = list(words_str.split(' '))
for ind, elem in enumerate(words_list):
    print(ind, elem)