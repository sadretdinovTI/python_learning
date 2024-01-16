spisok1 = set()
spisok2 = set()
vvod1 = input()

while vvod1 != '':
    spisok1.add(vvod1)
    vvod1 = input()

vvod2 = input()
while vvod2 != '':
    spisok2.add(vvod2)
    vvod2 = input()

intersection = spisok1.intersection(spisok2)
if len(intersection) == 0:
    print('EMPTY')
else:
    print(intersection)
