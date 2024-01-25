word = input()
max = count = 0
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        count += 1
        if count > max:
            max = count
print(max)