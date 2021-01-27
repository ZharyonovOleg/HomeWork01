################### Lesson_07.py ###############################

# class Car:
#     def __init__(self):
#         self.modules = []
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car.modules.append(module1)
# car.modules.append(module2)
# car.modules.append(module3)
#
# print(car.modules)  # сделаем удобнее:

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car + module1 # + (плюс) это на самом деле не + , а add
# car + module2
# car + module3
### car + module1 + module2 + module3 # работать так не будет
# print(car.modules)

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self # чтобы работало
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car + module1 + module2 + module3 # работать так будет из-за return
#
# print(car.modules)

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self # чтобы работало
#
#     def __str__(self): # стринговое представление объекта
#         return f'{self.modules}' # обязательно str-данные
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car + module1 + module2 + module3 # работать так будет из-за return
#
# print(car)

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self # чтобы работало
#
#     def __str__(self): # стринговое представление объекта
#         return f'{self.modules}' # обязательно str-данные
#
#     def __del__(self): # удаляем все объекты из памяти, если они не нужны и перед закрытием программы
#         print('объект удалён')
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car + module1 + module2 + module3 # работать так будет из-за return
#
# print(car)

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self # чтобы работало
#
#     def __str__(self): # стринговое представление объекта
#         return f'{self.modules}' # обязательно str-данные
#
#     def __del__(self): # удаляем все объекты из памяти, если они не нужны и перед закрытием программы
#         print('объект удалён')
#
#     def __setattr__(self, key, value):
#         # super().__setattr__(key, value) # можно через super
#         self.__dict__[key] = value # так моднее
#         print(f'добавлен ключ {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item] # для выполнения обращения к модулю
#
#     def __call__(self, price=None): # имитация запуска экземпляра класса как функции
#         return f'Полная информация: машина {self.name}, модули: {self.modules}, цена: {price}'
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car + module1 + module2 + module3 # работать так будет из-за return
# car.name = 'Tesla' # здесь отрабатывает setattr для модификации и добавления
#
# ## print(car.modules[1]) # обращение к первому модулю
#
# ## print(car[1]) # так будет работать с __getitem__
#
# # print(car)
#
# print(car(5000)) # car со скобками, так как работает как функция из-за __call__, берёт цену из скобок


# class Car:
#     def __init__(self):
#         self.modules = []
#         self.fc = 7 # типа расход топлива
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self # чтобы работало
#
#     def __str__(self): # стринговое представление объекта
#         return f'{self.modules}' # обязательно str-данные
#
#     def __del__(self): # удаляем все объекты из памяти, если они не нужны и перед закрытием программы
#         print('объект удалён')
#
#     def __setattr__(self, key, value):
#         # super().__setattr__(key, value) # можно через super
#         self.__dict__[key] = value # так моднее
#         print(f'добавлен ключ {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item] # для выполнения обращения к модулю
#
#     def __call__(self, price=None): # имитация запуска экземпляра класса как функции
#         return f'Полная информация: машина {self.name}, модули: {self.modules}, цена: {price}'
#
#     def __eq__(self, other): # в методичке другие варианты, работают также
#         return self.fc == other
#
# car = Car()
# module1 = 'подогрев руля'
# module2 = 'подогрев лобового стекла'
# module3 = 'круиз-контроль'
#
# car + module1 + module2 + module3 # работать так будет из-за return
# car.name = 'Tesla' # здесь отрабатывает setattr для модификации и добавления
#
# print(car.modules[1]) # обращение к первому модулю
#
# print(car[1]) # так будет работать с __getitem__
#
# print(car)
#
# print(car(5000)) # car со скобками, так как работает как функция из-за __call__, берёт цену из скобок
#
# print(car == 7) # ответ True (__eq__)
# print(car == 8) # Ответ False (__eq__)



######## Переопределение методов #########

##уже была тема: Это специальный механизм, позволяющий использовать метод класса-родителя в классе-потомке с добавлением некоторой функциональности



######## Интерфейсы #########
#
# from abc import ABC, abstractmethod
#
# class MyAbcClass(ABC): # Для работы в команде, название методов не менять. Это шаблон
#     @abstractmethod # декоратор
#     def my_method1(self):
#         pass
#
#     @abstractmethod
#     def my_method2(self):
#         pass
#
# class MyClass(MyAbcClass):
#     def my_method1(self):
#         print('qwe')
#     def my_method2(self):
#         print('asd')
#
# mc = MyClass()
# mc.my_method1()
# mc.my_method2()


## qwe = [1, 2, 3, 4, 5]
##
## for i in qwe:
##     print(i)
##
## raise - выводит нужную ошибку, например TimeoutError или любую другую.


# class Iterator: # будут вопросы в тестировании
#     def __init__(self):
#         self.i = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration # отработка до ошибки (или до команды) StopIteration. Так работает цикл for
#
# qwe = Iterator()
#
# for i in qwe:
#     print(i)


######### Декоратор @property ##############

# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self._age = age
#
#     @property # Для того, чтобы обращаться к методу, как к атрибуту, то есть чтобы не писать () в print(human.age())
#     def age(self):
#         # всякие условия и проверки для self._age
#         return self._age
#
# human = Human('Ivan', 'Ivanov', 50)
# print(human.age)
# print(human.name)
# print(human.surname)


############ Композиция ############

# class WinDoor: # вычитание окон и дверей из площади стен
#     def __init__(self, w, h):
#         self.square = w * h
#
# class Room:
#     def __init__(self, l1, l2, h):
#         self.square = 2 * h * (l1 + l2)
#         self.wd = []
#
#     def add_windoor(self, w, h):
#         self.wd.append(WinDoor(w, h))
#
#     def common_square(self):
#         main_square = self.square
#         for el in self.wd:
#             main_square -= el.square
#         return  main_square
#
# r = Room(10, 15, 3)
#
# print(r.square)
#
# r.add_windoor(2, 1)
# r.add_windoor(2, 2)
# r.add_windoor(2, 3)
#
# print(r.common_square())


# Домашка примерно с 02:08:00