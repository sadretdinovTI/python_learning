words = input()
count = 0
for word in words:
    if word.isalpha():
        count += 1
print(count)
# or print(len(''.join(input().split())))