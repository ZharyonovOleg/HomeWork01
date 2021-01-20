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
        x = str(input('Введите в какую сторону совершается поворот налево или направо: '))
        if x == ('налево'):
            print('машина повернула налево')
        elif x == ('направо'):
            print('машина повернула направо')

car = Car((int(input('Введите скорость автомобиля: '))),
          (str(input('Введите цвет автомобиля: '))),
          (str(input('Введите марку автомобиля: '))),
          (bool(input('Полицейская ли это машина или нет?\n Введите "True", если машина полицейская или "False",\n если машина НЕ полицейская: '))))

class TownCar(Car):

    def show_speed(self):
        if self.speed >= 60:
            print('Если Вы едете на городском автомобиле, то Вы превысили скорость!!!')

class SportCar(TownCar):
    pass

class WorkCar(SportCar):
    def show_speed(self):
        if self.speed >= 40:
            print('Если Вы едете на грузовике, то Вы превысили скорость!!!')

class PoliceCar(WorkCar):
    pass


print(car.name)
car.go()
print(car.name)
car.stop()
car.turn()

town_car = TownCar
work_car = WorkCar

town_car.show_speed()

work_car.show_speed()