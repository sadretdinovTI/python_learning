def calculate_inverse(number):
    if abs(number) < 0.000001:
        return "миллион"
    else:
        return 1 / number

user_input = float(input("Введите дробное число: "))
result = calculate_inverse(user_input)
print("Обратное число:", result)