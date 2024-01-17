orel = max_orel = 0
word = input("Enter: ")
for i in range(len(word)):
    if word[i] == 'о':
        orel += 1
        if orel > max_orel:
            max_orel = orel
    else:
        orel = 0
print(max_orel)