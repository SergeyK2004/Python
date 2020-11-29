products = [(1, {'название': 'мышь', 'цена': 200.0, 'количество': 3, 'eд': 'шт'}), (2, {'название': 'кошь', 'цена': 540.0, 'количество': 4, 'eд': 'шт'}), (1, {'название': 'клава', 'цена': 200.0, 'количество': 4, 'eд': 'шт'}), (2, {'название': 'монитор', 'цена': 430.0, 'количество': 1, 'eд': 'кор'})]
cont = 0
# Для упрощения проверки можно закомментить следующий блок до черты, он обнуляет значения присвоеные выше.
products = []
cont = 1
# -------------------------------
count = 0
while cont == 1:
    count += 1
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit = input("Укажите единицу измерения: ")
    product = {"название": name, "цена": price, "количество": quantity, "eд": unit}
    new_position = (count, product)
    products.append(new_position)
    cont = int(input("Введите 1 для следующего товара или 0 для завершения: "))
my_dic = {}
for i in products[0][1].keys():
    my_dic.setdefault(i, list())
for i in products:
    for key, value in i[1].items():
        my_dic[key].append(value)
print("Список товаров:")
for key, value in my_dic.items():
    my_dic[key] = list(set(value))
    print(key, ":", my_dic[key])
