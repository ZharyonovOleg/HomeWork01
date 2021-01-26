from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v, h):
        self.size = v
        self.height = h

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suite(self):
        pass

class Cloth(Clothes):
    @property
    def coat(self):
        self.coat_cloth = float((float(self.size) / 6.5) + 0.5)
        return self.coat_cloth

    @property
    def suite(self):
        self.suite_cloth = float((float(self.height) * 2) + 0.3)
        return self.suite_cloth

    @property
    def total(self):
        self.total_cloth = self.coat_cloth + self.suite_cloth
        return self.total_cloth


cloth = Cloth(float(input('Введите размер пальто: ')), (float(input('Введите ростовку костюма: '))))

print('На пальто понадобится ', cloth.coat, 'ткани')

print('На костюм понадобится ', cloth.suite, 'ткани')

print('На костюм понадобится ', cloth.total, 'ткани')