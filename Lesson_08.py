#############  LESSON 08  ################

# class DataBaseConnection:
#
#     @staticmethod
#     def connect():
#         print('connect')
#
#     def select(self):
#         print('select')
#
# DataBaseConnection.connect() # работает из-за @staticmethod, не создаётся экземпляр класса, работает с любым инитом, но работает, если внутри нет взаимодействия с СЕЛФ


# class MyClass:
#
#     @classmethod
#     def qwe(cls, x):
#         print(cls, x)
#         cls()
#
#
# MyClass.qwe(100)


# class Customer:
#     """Это класс покупатель"""
#
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
# john = Customer('John', 21311561531)
#
# john.qwe = 0
# print(john.__dict__)
# print(john.__doc__)
# print(john.__class__.__name__)
# print(john.__module__)
# print(john.__dir__())


### ООП-ПРОГРАММА ###

# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'
#
# class Teacher(Person):
#
#     def to_teach(self, subj, *people):
#         for pipl in people:
#             pipl.to_take(subj)
#
# class Pipl(Person):
#
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.knowledge = []
#
#     def to_take(self, subj):
#         self.knowledge.append(subj)
#
# class Subj:
#
#     def __init__(self, *subjects):
#         self.subjects = subjects
#
#     def __str__(self):
#         return f'{s.subjects}'
#
# s = Subj('math', 'physics')
# t = Teacher('Ivan', 'Ivanov')
# p1 = Pipl('Petr', 'Petrov')
# p2 = Pipl('Sidr', 'Sidorov')
# p3 = Pipl('Max', 'Maximov')
#
# # print(p1, p2, p3)
#
# t.to_teach(s, p1, p2)
# print(p1.knowledge[0])
# print(p3.knowledge)


# class MyOwnException(Exception):
#
#     def __init__(self, txt):
#         self.txt = txt
#
# if int(input()) < 0:
#     raise MyOwnException('Negative')
# else:
#     print('All OK')

# try:
#     if int(input()) < 0:
#         raise MyOwnException('Negative')
#     else:
#         print('All OK')
# except MyOwnException:
#     print('Been Negative')
#
# class my_dict(dict):
#     pass

### ООП КАНЕС!!! ###


##### pipy vsyakie #######
# import psutil


# import requests
# response = requests.get('https://www.bbc.com')