class Complex_num:
    def __init__(self, x, y):
        self.number = complex(x, y)

    def __str__(self):
        return str(self.number)

    def __add__(self, other_number):
        return self.number + other_number.number

    def __mul__(self, other_number):
        return self.number * other_number.number


a = Complex_num(3, 5)
print(f"a = {a}")
b = Complex_num(2, 3)
print(f"b = {b}")
print("Теперь пробуем арифмитические операции")
print(f"складываем a и b, получаем: {a + b}")
print(f"умножаем a и b, получаем: {a * b}")
