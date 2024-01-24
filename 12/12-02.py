words = input('Enter words: ').split()
print(len(max(words, key=len)))