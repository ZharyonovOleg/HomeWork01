numerator = float(input('Для деления двух чисел введите числитель: '))
denomerator = float(input('и знаменатель: '))

class MyOwnException(Exception):

    def __init__(self, txt):
        self.txt = txt

try:
    if denomerator == 0:
        raise MyOwnException('Negative')
    else:
        print('Ответ: ', float(numerator / denomerator))
except:
    print('На ноль делить нельзя')