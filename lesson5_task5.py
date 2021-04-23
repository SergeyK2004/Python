with open("task5.txt", "w") as write_file:
    text = "24 12 54 23 8 5 3 98 12 2 31"
    write_file.write(text)

with open("task5.txt", "r") as read_file:
    text = read_file.read()
    summa = 0
    for num in text.split():
        summa += int(num)
print(summa)
