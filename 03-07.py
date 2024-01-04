min_num = 1
max_num = 1000
tries = 0
found = False

while not found and tries < 10:
    guess = (min_num + max_num) // 2
    print(guess)
    response = input("Загаданное число больше или меньше? ")

    if response == "больше":
        min_num = guess + 1
    elif response == "меньше":
        max_num = guess - 1
    elif response == "равно":
        found = True
        print("Угадал!")

    tries += 1

if not found:
    print("Не угадал!")