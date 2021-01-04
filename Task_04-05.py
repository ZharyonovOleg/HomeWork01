from functools import reduce

my_list = ([x * 1 for x in range(100, 1001) if x % 2 <= 0])
print(my_list)
print(reduce(lambda x, y: x * y, my_list))