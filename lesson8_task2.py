class Zero_divider(Exception):
    def __init__(self, dividend):
        self.text = f"Попытка разделить {dividend} на Ноль. Деление на ноль невозможно!"


class Division:
    def __init__(self, dividend, divider):
        try:
            if divider == 0:
                raise Zero_divider(dividend)
            result = dividend / divider
        except Zero_divider as error:
            print(error.text)
        else:
            print(result)


a = Division(3, 0)
b = Division(7, 4)
