spisok = list()
num_strs = int(input("Enter num: "))
for i in range(num_strs):
    spisok.append(input("Enter request: "))
search_word = input("Enter serch word: ")
for word in range(len(spisok)):
    if search_word in spisok[word]:
        print(spisok[word])

