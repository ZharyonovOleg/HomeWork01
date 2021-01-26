class Clothes:
    def __init__(self, v, h):
        self.size = v
        self.height = h

    @property
    def coat(self):
        self.coat_cloth = float((float(self.size) / 6.5) + 0.5)
        return self.coat_cloth

    @property
    def suite(self):
        self.suite_cloth = float((float(self.height) * 2) + 0.3)
        return self.suite_cloth

clothes = Clothes(float(input('Введите размер пальто: ')), (float(input('Введите ростовку костюма: '))))

print('На пальто понадобится ', clothes.coat, 'ткани')

print('На костюм понадобится ', clothes.suite, 'ткани')