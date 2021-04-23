class Cell:
    def __init__(self, cellule):
        self.cellule = cellule
    
    def __add__(self, other_cell):
        return Cell(self.cellule + other_cell.cellule)

    def __sub__(self, other_cell):
        if self.cellule > other_cell.cellule:
            return Cell(self.cellule - other_cell.cellule)
        else:
            print("Вторая клетка должна быть меньше первой.")
            return self

    def __mul__(self, other_cell):
        return Cell(self.cellule * other_cell.cellule)

    def __truediv__(self, other_cell):
        if (self.cellule // other_cell.cellule) > 0:
            return Cell(self.cellule // other_cell.cellule)
        else:
            print("Значение при делении меньше 1.")
            return Cell(1)

    def make_order(self, count):
        modulo = self.cellule
        string = ''
        while modulo >0:
            string += "*" * min(modulo, count) + "\n"
            modulo -= count
        print(string)

a = Cell(12)
b = Cell(3)
c = a - b
c.make_order(5)
            