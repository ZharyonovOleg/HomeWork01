################## LESSON 06 ######################
# #
# # def print_human_name(human):
# #     print(human['name'])
# #
# # h1 = {'name': 'ABC'}
# # h2 = {'name': 'ASD'}
# # # print_human_name(h1)
# # h3 = {'full_name': 'ZXC'}
# # # print_human_name(h3) # работать не будет
#
# class Phone:
#     def __init__(self, phone_model): # init метод, который вызывается в первую очередь в момент создания класса, называется конструктор класса
#         self.ph_model = phone_model
#         self._loading()
#         self.__serial_num = 123456
#
#     def call(self): # функция внутрии класса уже не функция, а становится методом
#         print('calling')
#
#     def _loading(self):
#         print(self.ph_model, 'loading')
#
#     def get_serial_num(self):
#         return self.__serial_num
#
# # phone = Phone('nokia1100') # в скобках можно написать (phone_model='nokia1100')
# # phone2 = Phone('nokia3110')
# # phone.call()
# # print(phone.get_serial_num())
# # print(phone.__serial_num()) # выдаст ошибку так как __ прячет сильнее.
# # phone._Phone__serial_num = 0
# # print(phone._Phone__serial_num) # obj._ClassName__atr
#
# ## дальше наследование (видимо из предыдущего класса)
#
# class SmartPhone(Phone): # новый класс с наследованием старого
#
#     def sms(self):
#         print('sms sending')
#
#     def email(self):
#         print('email sending')
#
# # sm_phone = SmartPhone(phone_model='Nokia 8800')
# # sm_phone.call()
# # sm_phone.sms()
#
# class IPhone(SmartPhone): # дальнейшее наследование, в том числе частичное и с модификацией функций
#
#     def __init__(self, phone_model): # init метод, можно поменять при необходимости и не писать весь, что можно делать и на других
#         super().__init__(phone_model)
#         print('show apple')
#
#     def player(self):
#         print('music')
#
#     def browser(self):
#         print('surfing')
#
#     def sms(self):
#         print('Imessage sending') # меняем атрибут смс на другой, также можно переделать __init__
#
# # iphone = IPhone('11pro')
# # iphone.player()
# # iphone.sms()
#
# class NextGen(IPhone): # это для создания класса для дальнейшей работы, ПАСС - пропустить
#     pass


# # множественное наследование от нескольких в одного:
#
# class Player:
#     def player_method(self):
#         print('player_method')
#
# class Navigator:
#     def navigator_method(self):
#         print('navigator_method')
#
# class MPhone(Player, Navigator):
#     def mphone(self):
#         print('mphone')
#
# mphone = MPhone()
# mphone.mphone()
# mphone.navigator_method()
# mphone.player_method()


# ### Полиморфизм (имеющий многие формы):
# 
# class Auto: # перегрузка методов
#     def auto_start(self, param1, param2=None):
#         if param2 is not None:
#             print(param1 + param2)
#         else:
#             print(param1)
# 
# auto = Auto()
# auto.auto_start(10)
# auto.auto_start(10, 20)