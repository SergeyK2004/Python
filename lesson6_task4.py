class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print(self._car_info() + " поехала")

    def stop(self):
        print(self._car_info() + " остановлена")

    def turn(self, direction):
        print(self._car_info() + " поворачивает на", direction)

    def show_speed(self):
        print(self._car_info() + ". Скорость машины:", self.speed)

    def _car_info(self):
        info = ("Полицейская машина " if self.is_police else "Машина ") \
                + (f"{self.name}, цвет  {self.color} ")
        return info


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(self._car_info() + ". Скорость превышена, и "
              if self.speed > 60 else "Скорость машины ",
              "составляет", self.speed)


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(self._car_info() + ". Скорость превышена, и " if self.speed > 40
              else "Скорость машины ", "составляет", self.speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


a = WorkCar("Mazda", "black", 70)
a.show_speed()
b = SportCar("Nissan", "white", 140)
b.show_speed()
c = PoliceCar("Toyota", "black", 120)
c.show_speed()
c.go()
c.turn("право")
