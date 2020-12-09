with open("task4.txt", "r") as read_file, open("task4_new.txt", "w") as write_file:
    text = read_file.readlines()
    for i in range(len(text)):
        string = text[i].split(" — ")
        print(string)
        if len(string) > 1:
            if string[0] == "One":
                new_string = "Один"
            elif string[0] == "Two":
                new_string = "Два"
            elif string[0] == "Three":
                new_string = "Три"
            elif string[0] == "Four":
                new_string = "Четыре"
            new_string += " - " + string[1]
            write_file.write(new_string)
        else:
            write_file.write(text[i])

