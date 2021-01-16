#### ОЧЕНЬ ТРУДНО!!!!!!

with open('05-06.txt') as funk:
    my_lines = funk.readlines()
# print(my_lines)
my_dict = {}
for line in my_lines:
    spl_line = line.split()
    subject = spl_line[0]
    sum_les = sum([int(x[:x.find('(')]) for x in spl_line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_les
print(my_dict)