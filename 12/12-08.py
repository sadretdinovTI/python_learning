line = input("Enter: ").lower()
letter = 0
count = 0
for char in range(len(line)):
    if line.count(line[char]) > count:
        count = line.count(line[char])
        letter = line[char]
print(letter)