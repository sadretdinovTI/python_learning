count_mans = int(input('Количество мужчин: '))
mans_set = set()
duplicate = set()
intersection_count = 0
for i in range(count_mans):
    surname = input('Фамилия: ')
    if surname not in mans_set:
        mans_set.add(surname)
    else:
        intersection_count += 1
        if surname not in duplicate:
            duplicate.add(surname)
intersection_count += len(duplicate)
print(intersection_count, duplicate)