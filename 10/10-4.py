word_list = []
for line in range(int(input('Enter a number of lines: '))):
    word_list.append(input('Enter a word: '))
for i in range(len(word_list)-1):
    for j in range(len(word_list)-1-i):
        if len(word_list[j]) > len(word_list[j+1]):
            word_list[j], word_list[j+1] = word_list[j+1], word_list[j]
        elif ord(word_list[j][0]) > ord(word_list[j+1][0]):
            word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]

for word in word_list:
    print(word)