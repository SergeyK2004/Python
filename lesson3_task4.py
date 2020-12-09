def my_degree_func1(x, y):
    return x ** y

def my_degree_func2(x, y):
    abs_of_y = abs(y)
    result = 1
    for i in range(abs_of_y):
        result *= x
    return 1 / result

x = int(input("Введите целое положительное число x:"))
y = int(input("Введите целое отрицательное число y:"))
print("Найдем х в степени у двумя способами.")
print(f'{x} в степени {y} найденое первым способом через "**" = {my_degree_func1(x, y)}')
print(f'{x} в степени {y} найденое вторым способом через математические операции = {my_degree_func2(x, y)}')
