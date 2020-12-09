def user_to_str(name, last_name, year_of_birthday, city, e_mail, phone):
    return f'{name} {last_name}, {year_of_birthday}г.р. проживает в г.{city}. e-mail: {e_mail}, tel: {phone}'

name = input("Введите имя:")
last_name = input("Введите фамилию:")
year_of_birthday = input("Укажите год своего рождения")
city = input("Введите город:")
e_mail = input("Укажите свой e-mail:")
phone = input("Ваш номер телефона:")

print(user_to_str(name = name, last_name = last_name, year_of_birthday = year_of_birthday, city = city, e_mail = e_mail, phone = phone))