class Date:
    def __init__(self, string_date):
        self.string_date = string_date

    @classmethod
    def date_to_num(cls, string_date):
        if cls.chek_date(string_date):
            my_list = string_date.split("-")
            day = int(my_list[0])
            month = int(my_list[1])
            year = int(my_list[2])
            print(day, month, year)

    @staticmethod
    def chek_date(string_date):
        my_list = string_date.split("-")
        day = int(my_list[0])
        month = int(my_list[1])
        year = int(my_list[2])
        result = True
        if (day > 31 or day < 1):
            print("Номер дня в дате должен быть в промежутке от 1 до 31")
            result = False
        if (month > 12 or month < 1):
            print("Номер месяца в дате должен быть в промежутке от 1 до 12")
            result = False
        if (year > 2020 or year < 2000):
            print("Номер года в дате должен быть в промежутке от 2000 до 2020")
            result = False
        return result


a = Date("15-02-2019")
print(Date.chek_date("32-15-2020"))
Date.date_to_num("17-11-2014")
