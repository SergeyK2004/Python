def quotient(num, denom):
    return num / denom

numerator = int(input("Введите числитель:"))
denominator = 0
while denominator == 0:
    denominator = int(input("Введите знаменатель:"))
    if denominator == 0:
        print("На ноль делить нельзя!")
print(f'Результат деления {numerator} на {denominator} равен {quotient(numerator, denominator)}')