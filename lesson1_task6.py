dist = int(input("Укажите дистанцию первой пробежки в км:"))
target = int(input("Укажите цель в км:"))
count = 1
dist_now = float(dist)
while dist_now < target:
    count += 1
    dist_now += dist_now * 0.1
print(f"Цель в {target}км будет достигнута в {count}-й день")
