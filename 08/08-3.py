name = input("Enter: ")
for letter in name:
    if not (48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122
            or ord('_') == ord(letter)):
        print('Неверный символ: ', letter)
        break
else:
    print('OK')