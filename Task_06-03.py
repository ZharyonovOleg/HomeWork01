class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

class Position(Worker):

    def get_full_name(self):
        print('Полное имя сотрудника: ', self.name, self.surname)

    def get_total_income(self):
        print('Полный доход этого сотрудника: ', self.__income)

position = Position((input('Введите имя сотрудника: ')),
                (input('Введите фамилию сотрудника: ')),
                (input('Введите должность сотрудника: ')),
                    (sum({'wage': (int(input('Введите размер зарплаты: '))), 'bonus': (int(input('Введите размер премии: ')))}.values())))
# не пойму никак почему ошибка

position.get_full_name()
position.get_total_income()