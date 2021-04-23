class Only_numeric(Exception):
    def __init__(self, string):
        self.text = f"'{string}' не является числом. Вводите только числа!"


my_list = []
stop_work = False
while not stop_work:
    try:
        string = input("Введите число или stop для остановки:")

        if (string.isdigit()):
            my_list.append(int(string))
        elif (string == "stop"):
            stop_work = True
        else:
            raise Only_numeric(string)
    except Only_numeric as error:
        print(error.text)
    else:
        print(my_list)
