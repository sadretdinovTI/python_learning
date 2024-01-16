message = input("Enter: ")
num_letter = int(input("Enter: "))
if num_letter > len(message):
    print('Error')
else:
    print(message[num_letter-1])