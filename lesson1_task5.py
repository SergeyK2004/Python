proceeds = float(input("Введите сумму выручки:"))
costs = float(input("Введите сумму издержек:"))
if proceeds > costs:
    profit = proceeds - costs
    print(f"В этом периоде вы получили прибыль в размере: {profit:.2f}")
    profitability = int((profit / proceeds) * 100)
    print(f"Рентабельность: {profitability}%")
    persons = int(input("Укажите количество сотрудников вашей компании:"))
    print(f"Прибыль на каждого сотрудника компании составила: {profit / persons:.2f}")
elif proceeds == costs:
    print("Ваша компания сработала в ноль.")
else:
    print("Финансовый результат работы Вашей компании - убыток.")