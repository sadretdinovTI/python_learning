numbersD = [int(input()) for _ in range(17)]

for i in range(17):
    if i % numbersD[i] == 0:
        print("ДА")
    else:
        print("НЕТ")
