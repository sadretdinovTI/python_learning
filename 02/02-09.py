man1 = int(input('Введите рост: '))
man2 = int(input('Введите рост: '))
man3 = int(input('Введите рост: '))
tallest = max(man1, man2, man3)
shortlest = min(man1, man2, man3)
sorted_high = sorted([man1, man2, man3], reverse=True)
for height in sorted_high:
    print(height)