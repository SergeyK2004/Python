with open("task1.txt", "w") as my_file:
    while True:
        string = input("Введите строку для добавления в файл или пустую строку для окончания ввода:").strip()
        if string == '':
            break
        else:
            print(string, file=my_file)