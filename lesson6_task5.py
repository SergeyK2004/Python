class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")



class Pen(Stationery):
    def draw(self):
        print("Рисуем ручку")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандаш")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркер")


a = Stationery("Блокнот")
a.draw()
b = Pen("Шариковая ручка")
b.draw()
c = Handle("Перманентный маркер")
c.draw()
