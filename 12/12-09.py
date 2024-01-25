letter = input('Enter a letter: ')
sentence = input('Enter a sentence: ')
for word in sentence.split():
    if letter.lower() in word.lower():
        print(word)