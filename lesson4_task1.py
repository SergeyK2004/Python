from sys import argv
script_name, hours, hour_price, prize = argv
print(f"Зарплата за {hours} часов, включая премию {prize} составляет {int(hours) * int(hour_price) + int(prize)} рублей.")