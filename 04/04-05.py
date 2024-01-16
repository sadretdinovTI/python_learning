count = 0
product = 1
while  count < 6:
    num = int(input('Введите число: '))
    if num != 0:
        product *= num
    count += 1
print(product)
