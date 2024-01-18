words_list = []
for word in range(int(input("Enter num of words: "))):
    words_list.append(input('Enter word: '))
for i in range(len(words_list)-1):
    for j in range(len(words_list)-1-i):
        if ord(words_list[j][0]) > ord(words_list[j+1][0]):
            words_list[j], words_list[j+1] = words_list[j+1], words_list[j]
for word in words_list:
    print(word)