avgiq = 0
humans = int(input('Введите количество тестируемых людей: '))
for i in range(humans):
    setiq = int(input('Введите показатель iq: '))
    if i == 0:
        print(0)
        avgiq = setiq
    else:
        avgiq = (avgiq * i + setiq) / (i + 1)
        if setiq > avgiq:
            print('>')
        else:
            print('<')