count_strokes = int(input('Введите число строк: '))
for i in range(count_strokes):
    stroke = input('Введите слово: ')
    if 'Кот' in stroke or 'кот' in stroke:
            print('МЯУ')
            break
