coins = int(input("Введите количество монет у Учителя: "))
while coins >= 8:
    coins //= 8
print("Оставшееся количество монет: ", coins)