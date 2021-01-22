class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.mass_1sq_m_on_5cm = 25
        self.thick_road = 5 / 100

    def mass(self):
        print('Массса использованного асфальта равна: ',
        int(self._lenght * self._width * self.mass_1sq_m_on_5cm * self.thick_road), 'килограмм')

road = Road(5000, 20)
road.mass() #### в методичке ошибка кажется с ответом