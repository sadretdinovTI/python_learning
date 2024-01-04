count = 0
found_stroke = 0
flag = False
while True:
    count += 1
    stroke = input()
    if 'кот' in stroke or 'Кот' in stroke:
        found_stroke = count
        flag = True
    elif stroke == 'СТОП':
        break
if flag:
    print(found_stroke)
