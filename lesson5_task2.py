def case(num):
    modulo = num % 10
    if modulo == 0 or modulo > 4:
        return "слов"
    elif modulo == 1:
        return "слово"
    else:
        return "слова"


with open("task2.txt", "r") as my_file:
    text = my_file.readlines()
    print(f"Всего в фале {len(text)} строк")
    for i in range(len(text)):
        print(f"В строке номер {i + 1} содержится {len(text[i].split())} {case(len(text[i].split()))}")