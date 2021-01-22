class Stationery:
    def __init__(self, title):
        self.title = 'Picture'
        self.draw()

    def draw(self):
        print(self.title, 'Start drawing')

Stationery('Picture')

class Pen(Stationery):
    def draw(self):
        print(self.title, 'Start drawing pen')

Pen('Picture')

class Pencil(Stationery):
    def draw(self):
        print(self.title, 'Continue drawing pencil')

Pencil('Picture')

class Handle(Stationery):
    def draw(self):
        print(self.title, 'Finish drawing handle')

Handle('Picture')