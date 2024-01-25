tokens = input("Enter: ").split()
stack = []
for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        num1 = stack.pop()
        num2 = stack.pop()

        if token == '+':
            result = num2 + num1
        elif token == '-':
            result = num2 - num1
        elif token == '*':
            result = num2 * num1

        stack.append(result)

print(result)
