word = list(input("Enter "))
for i in range(len(word)-1):
    if word[i].isalpha() and word[i+1].isalpha():
        word[i] += '-'
print(''.join(word).upper())
