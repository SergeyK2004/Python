import json
with open("task7.txt", "r") as read_file, open("task7.json", "w") as write_file:
    text = read_file.readlines()
    my_dict = {}
    av_prof = {}
    sum_count = 0
    sum_profit = 0
    for string in text:
        firm = string.split()
        firm_name = firm[0]
        firm_profit = int(firm[2]) - int(firm[3])
        if firm_profit > 0:
            sum_count += 1
            sum_profit += firm_profit
        my_dict[firm_name] = firm_profit
    av_prof["average_profit"] = round(sum_profit / sum_count, 2)
    string_to_file = [my_dict, av_prof]
    json.dump(string_to_file, write_file)

