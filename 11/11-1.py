text = input("Enter text: ")
words = text.split()
third_words = []
for i in range(2, len(text.split()), 3):
    third_words.append(text.split()[i])
result = " ".join(third_words)
print(result)
