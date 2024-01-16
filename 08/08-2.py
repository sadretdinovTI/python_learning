word1 = input('Enter a word: ')
word2 = input('Enter a word: ')
if len(word1) != len(word2):
    print('Invalid input')
else:
    bulls = 0
    cows = set()
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            bulls += 1
        else:
            if word1[i] in word2:
                cows.add(word1[i])
print(bulls, len(cows))