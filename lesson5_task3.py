with open("task3.txt", "r") as my_file:
    text = my_file.readlines()
    sum_salary = 0
    count_of_emloyee = 0
    for i in range(len(text)):
        employee_list = text[i].split()
        if len(employee_list) > 0:
            employee_salary = employee_list[len(employee_list) - 1]
            first_num = employee_salary[0]
            employee_salary = int(employee_salary)
            employee_full_name = text[i][:text[i].index(first_num)]
            count_of_emloyee += 1
            sum_salary += employee_salary
            if employee_salary < 20000:
                print(f"Сотрудник {employee_full_name} получает меньше 20 т.р., а именно: {employee_salary}")
    print(f"В коллективе {count_of_emloyee} сотрудников и их средняя зп составляет"
          f" {round(sum_salary / count_of_emloyee, 2)}")
