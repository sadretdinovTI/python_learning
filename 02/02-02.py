def calculate():
    product = 1
    for i in range(1, 10):
        product *= i
    return product

result = calculate()
print("Произведение чисел от 1 до 9: ", result)