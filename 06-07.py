count_listov = int(input('Количество листов: '))
intersection_set = set()

count_surname1 = int(input('Количество фамилий на 1 листе: '))
for i in range(count_surname1):
    surname = input('Фамилия: ')
    intersection_set.add(surname)

for i in range(count_listov - 1):
    current_set = set()

    count_surname2 = int(input('Количество фамилий на текущем листе: '))
    for i in range(count_surname2):
        surname = input('Фамилия: ')
        current_set.add(surname)

    intersection_set = intersection_set.intersection(current_set)

for surname in intersection_set:
    print(surname)


