class Road:
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width
        self.mass_1m = 25
        self.mass_5cm = 5 / 100

    def mass(self):
        print('Массса использованного асфальта равна: ', self.__lenght * self.__width * self.mass_1m * self.mass_5cm)

road = Road(5000, 20)
road.mass() #### в методичке ошибка математическая, должно быть 125000 тонн