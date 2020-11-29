my_list = [7, 5, 3, 3, 2]
number = int(input("Введите число:"))
for i in range(len(my_list)-1, -1, -1):
    if number <= my_list[i]:
        my_list.insert(i+1, number)
        break
    if i == 0:
        my_list.insert(0, number)
print(my_list)
