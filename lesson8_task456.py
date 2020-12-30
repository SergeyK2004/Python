class Storage:
    technics = {}

    def __init__(self):
        pass

    def receive(self, unit, count):
        if not isinstance(count, int):
            print("Количество техники должно быть целым числом")
        else:
            Storage.technics[unit.name] = self.technics.get(
                unit.name, 0) + count

    def issue(self, unit, count):
        if not isinstance(count, int):
            print("Количество техники должно быть целым числом")
        else:
            Storage.technics[unit.name] = self.technics.get(
                unit.name, 0) - count

    def __str__(self):
        return str(Storage.technics)


class Technics:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Printers(Technics):
    def __init__(self, name, cost, cartridge_resurs):
        super().__init__(name, cost)
        self.cartridge_resurs = cartridge_resurs


class Scaner(Technics):
    def __init__(self, name, cost, resolution):
        super().__init__(name, cost)
        self.resolution = resolution


class Copier(Technics):
    def __init__(self, name, cost, copies_per_min):
        super().__init__(name, cost)
        self.copies_per_min = copies_per_min


a = Storage()
b = Copier("Canon 35", 19200, 6)
a.receive(b, 1)
print(a)
c = Copier("Canon 12", 12500, 5)
d = Scaner("HP a67", 24800, 1200)
a.receive(c, 2)
a.receive(d, 3)
print(a)
a.issue(c, "1")
a.issue(c, 1)
print(a)
