found_count = -1
count_strokes = 0
stroke = input('введите: ')
while stroke != 'СТОП':
    count_strokes += 1
    while ('Кот' in stroke) or ('кот' in stroke):
        if found_count == -1:
            found_count = count_strokes
        break
    stroke = input('введите: ')
print(found_count)


