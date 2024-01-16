step = int(input("Шаг: "))
message = input("Сообщение: ")
encrypted_message = ""

for letter in message:
    new_word = ord(letter) + step
    if ord(letter) < 1040 or ord(letter) > 1103:
        encrypted_message += letter
    elif 1072 <= ord(letter) <= 1103:
        if new_word > 1103:
            encrypted_message += chr(1072 + (new_word - 1104))
        else:
            encrypted_message += chr(new_word)
    else:
        if new_word > 1071:
            encrypted_message += chr(1040 + (new_word - 1072))
        else:
            encrypted_message += chr(new_word)

print(encrypted_message)
