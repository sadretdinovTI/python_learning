word = input().lower()
max = 0
for i in range(len(word)):
    if word.count(word[i]) > max:
        max = word.count(word[i])
print(max)