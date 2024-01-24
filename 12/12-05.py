words = [input() for i in range(int(input()[1:]))]
new_words = []
for word in words:
    if '#' in word:
        new_words.append(word[:word.find('#')].strip())
    else:
        new_words.append(word.strip())
for word in new_words:
    print(word)