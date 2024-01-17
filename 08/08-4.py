size = int(input("Enter size <=9: "))
gorizont = 'ABCDEFGHI'
vertical = '123456789'
for i in range(size-1, -1, -1):
    if i < size-1:
        print()
    for j in range(size):
        print(gorizont[j] + vertical[i], end=' ')
