import re

class NumbersOnly(Exception):
    def __init__(self, txt):
        self.txt = txt

def check_if_float(string):
    pattern = r'-{1}\d+\.\d+|\d+\.\d+'
    x = re.findall(pattern, string)
    try:
        new_string = string.replace(x[0], '')
        if len(x) != 0 and new_string == '':
            return True
    except IndexError:
        return False


lst = []
print('Вводите числа для формирования списка. Для выхода напишите слово exit')
for num in iter(input, 'exit'):
    try:
        if not num.lstrip('-').isnumeric() and not check_if_float(num):
            raise NumbersOnly('Вы ввели не число, пожалуйста, повторите ввод')
        lst.append(num)
    except NumbersOnly as no:
        print(no)
        continue
print(lst)