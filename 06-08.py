count_mans = int(input('Количество мужчин: '))
mans_set = set()
intersection_count = 0
for i in range(count_mans):
    surname = input('Фамилия: ')
    if surname in mans_set:
        intersection_count += 2
    mans_set.add(surname)
print(intersection_count)