import math


def fact(n):
    for el in range(1, n+1):
        yield math.factorial(el)


num = int(input("Введите число:"))

for el in fact(num):
    print(el)
