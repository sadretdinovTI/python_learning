num = int(input('Введите целое неотрицательное число: '))
factorial = 0
if num == 0 or num == 1:
    factorial == 1
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
print('Факториал числа', num, 'равен', factorial)