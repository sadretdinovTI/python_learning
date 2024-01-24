words = [input('Enter a word: ') for num in range(int(input('Enter num: ')))]
for word in range(len(words)):
    if 'кот' in words[word]:
        print(word+1, words[word].find('кот')+1)