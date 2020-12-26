rating = [7, 5, 3, 3, 2]

print('Первоначальный рейтинг: ', rating)
new_elem = int(input('Введите новое число рейтинга: '))

for ind, elem in enumerate(rating):
    if new_elem < int(elem):
        continue
    rating.insert(ind, new_elem)
    break
else:
    rating.append(new_elem)
print(rating)