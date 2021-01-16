
###### ОЧЕНЬ ТРУДНО!!!!!!

import json

firm_dict = {}
aver_prof = []

with open('05-07.txt') as funk:
    my_lines = funk.readlines()
# print(my_lines)

for line in my_lines:
    a, b, c, d = line.split()
    profit = int(c) - int(d)
    firm_dict[a] = profit
    if profit > 0:
        aver_prof.append(profit)

aver_prof = sum(aver_prof) / len(aver_prof)
out_info = [firm_dict, {'average profit': aver_prof}]

with open('05-07.json', 'w', encoding='utf-8') as f_json:
    json.dump(out_info, f_json, ensure_ascii=False)

with open('05-07.json') as f_json:
    print(json.load(f_json))