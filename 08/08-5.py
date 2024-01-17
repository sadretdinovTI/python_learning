count_message = int(input("Enter a number: "))
for i in range(count_message):
    message = input("Enter: ")
    if message[:2] == 'Не':
        if message[2] == ' ':
            print(message[3:])
        else:
            print(message[2:])
    else:
        print(message)