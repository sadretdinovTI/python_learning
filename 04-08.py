num = int(input('Введите число: '))
if num < 0:
    print('Пуск')
else:
    for i in reversed(range(num + 1)):
        print('Осталось секунд:', i)
        if i == 0:
            print('Пуск')