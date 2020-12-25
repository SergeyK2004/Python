from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cloth(self):
        return round(self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cloth(self):
        return round(self.height * 2 + 0.3)


a = Coat("пальтишко", 5)
b = Suit("Костюмчик", 7)
print(a.cloth + b.cloth)
