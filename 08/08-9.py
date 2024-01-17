num_words = int(input("Enter num: "))
for i in range(num_words):
    word = input("Enter: ")
    if word[:2] == '%%':
        print(word[2:])
    elif word[:4] == '####':
        pass
    else:
        print(word)

