number1 = float(input('Введите число: '))
number2 = float(input('Введите число: '))
action = input('Введите операцию: ')
if action == '+':
    print(number1+number2)
elif action == '-':
    print(number1-number2)
elif action=='*':
    print(number1*number2)
elif action=='/':
    print(number1/number2)
else:
    print(888888)