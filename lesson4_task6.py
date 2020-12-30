from itertools import count, cycle

start_num = int(input("С какого числа начнем?"))
for i in count(start_num):
    print(i)
    if i >= 10:
        break

start_list = input("Введите список элементов через пробел:").split()
count_of_repeat = 20
for el in cycle(start_list):
    print(el)
    count_of_repeat -= 1
    if count_of_repeat <= 0:
        break
