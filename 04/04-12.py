countNums = int(input('Введите число больше 0: '))
save = 0
for i in range(countNums):
    num = int(input('Введите любое число '))
    if i == 0:
        save = num
    else:
        if i % 2 == 0:
            save += num
        else:
            save -= num
print(save)