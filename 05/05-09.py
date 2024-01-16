flag = False
count_strs = int(input('Введите количество строк: '))
for i in range(count_strs):
    line = input()
    if 'кот' in line or 'Кот' in line:
        flag = True
    if 'пёс' in line or 'Пёс' in line:
        flag = False
if flag:
    print('МЯУ')
else:
    print('НЕТ')