import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

        self.running()
    def running(self):
        print(self.__color, 'Red')
        time.sleep(7)
        print(self.__color, 'Yellow')
        time.sleep(2)
        print(self.__color, 'Green')
        time.sleep(3)

tr_l = TrafficLight('TrafficLight: ')