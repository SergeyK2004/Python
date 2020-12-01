users_number = input("Введите число")
amount = int(users_number)
max_number = 0;
while amount > 0:
    modulo = amount % 10
    amount = amount // 10
    if modulo > max_number:
        max_number = modulo
print(f"В вашем числе {users_number} самая большая цифра = {max_number}")
