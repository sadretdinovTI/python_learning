height = int(input("Введите высоту пирамиды: "))

for row in range(height):
    for col in range(height - row - 1):
        print(" ", end="")
    for col in range(2 * row + 1):
        print("*", end="")
    print()