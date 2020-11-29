list = input("Введите список значений через запятую").split(",")
print("Ваш список - ", list)
for i in range(1,len(list), 2):
    temp = list[i - 1]
    list[i - 1] = list[i]
    list[i] = temp
print("Переделаный список - ", list)
