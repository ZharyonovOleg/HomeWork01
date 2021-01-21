class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(self.speed)

    def go(self):
        print('Поехали!!!')

    def stop(self):
        print('Остановка!')

    def turn(self):
        if (str(input('Введите "L",'
                      ' чтобы повернуть налево или "любую другую клавишу",'
                      ' чтобы повернуть направо: '))) == ('L'):
            print('Машина', car.color, car.name, 'повернула налево')
        else:
            print('Машина', car.color, car.name, 'повернула направо')


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 60:
            print('Если Вы едете на городском автомобиле,'
                  ' то Вы превысили скорость!!!')
        else:
            print('Если Вы едете на грузовике,'
                  ' то Вы соблюдаете скоростной режим!!!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print('Если Вы едете на грузовике,'
                  ' то Вы превысили скорость!!!')
        else:
            print('Если Вы едете на грузовике,'
                  ' то Вы соблюдаете скоростной режим!!!')

class PoliceCar(Car):
    pass

a = int(input('Введите скорость автомобиля: '))
b = str(input('Введите цвет автомобиля: '))
c = str(input('Введите марку автомобиля: '))
d = bool(input('Полицейская это машина или нет?\n Введите любую букву,'
                      ' если машина полицейская или просто нажмите "ENTER",'
                      '\n если машина НЕ полицейская: '))

car = Car(a, b, c, d)

print('Машина', car.color, car.name)
car.go()
print('Машина', car.color, car.name)
car.stop()
car.turn()

town_car = TownCar(a, b, c, d)
work_car = WorkCar(a, b, c, d)

town_car.show_speed()
work_car.show_speed()