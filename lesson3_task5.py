def summ_str(my_list):
    result_list = my_list.split()
    result_numeric_list = map(int, result_list)
    result_summ = sum(result_numeric_list)
    return result_summ

result = 0
stop = False
while not stop:
    user_str = input("Введите строку чисел разделенных пробелом, для остановки\
 закончите ввод символом '/'")
    if user_str[-1] == '/':
        stop = True
        user_str = user_str[:-1]
    if len(user_str)>0:
        result +=  summ_str(user_str)
        print(f"Результат сложения: {result}")