class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        print('Полное имя сотрудника: ', self.name, self.surname)

    def get_total_income(self):
        print('Полный доход этого сотрудника: ', self._income)

a = input('Введите имя сотрудника: ')
b = input('Введите фамилию сотрудника: ')
c = input('Введите должность сотрудника: ')
wage = int(input('Введите размер зарплаты: '))
bonus = int(input('Введите размер премии: '))
d = sum({'wage': wage, 'bonus': bonus}.values())

position = Position(a, b, c, d)

position.get_full_name()
position.get_total_income()