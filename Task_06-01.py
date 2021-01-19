import time

class TrafficLight:
    def __init__(self, color):
        self._color = color

        self.running()
    def running(self):
        print(self._color, 'Red')
        time.sleep(7)
        print(self._color, 'Yellow')
        time.sleep(2)
        print(self._color, 'Green')
        time.sleep(3)

tr_l = TrafficLight('TrafficLight: ')