def my_func(arg1, arg2,arg3):
    my_list = list([arg1, arg2, arg3])
    my_list = sorted(my_list)
    return my_list[1] + my_list[2]

arg1 = int(input("Введите число:"))
arg2 = int(input("Введите 2-е число:"))
arg3 = int(input("Введите 3-е число:"))
print(f'Сумма двух наибольших числе из введенных вами равна: {my_func(arg1, arg2, arg3)}')