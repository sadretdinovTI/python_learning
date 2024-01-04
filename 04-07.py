num = int(input('Введите число: '))
count = 0
deliteli = ''
for i in range(1, num + 1):
    if num % i == 0:
        deliteli += str(i) + ' '
        count += 1
print(f'Делители числа {num}:', deliteli)

if count == 2:
    print('Простое')
else:
    print('Нет')