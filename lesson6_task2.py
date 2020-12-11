class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def weight_all(self, weight, thickness):
        print(self._length * self._width * weight * thickness)

a = Road(20, 5000)
a.weight_all(25, 5)