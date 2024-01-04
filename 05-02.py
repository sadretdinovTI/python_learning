count_strokes = int(input())
flag = False
for i in range(count_strokes):
    stroke = input()
    if 'кот' in stroke or 'Кот' in stroke:
        flag = True
if flag:
    print('МЯУ')
else:
    print('НЕТ')