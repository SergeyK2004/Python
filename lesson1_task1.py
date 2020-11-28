hello_text = "Привет"
name = input("Ваше имя:")
print(hello_text, name)
q_text = name + ", сколько вам лет?"
age = int(input(q_text))
my_age = 46
if my_age > age:
    print(f"{name}, вы младше меня на {my_age - age} лет.")
elif my_age == age:
    print(f"{name}, мы с вами ровестники.")
else:
    print(f"{name}, вы старше меня на {age - my_age} лет.")