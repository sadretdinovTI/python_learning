num_strs = int(input("Enter num: "))
strs_list = list()
for i in range(num_strs):
    word = input("Enter word: ")
    strs_list.append(word)
num_letter = int(input("Enter num: "))
for words in strs_list:
    if len(words) < num_letter:
        continue
    print(words[num_letter - 1])

