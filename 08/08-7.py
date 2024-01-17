num_strs = int(input("Enter: "))
count_strs = 0
for i in range(num_strs):
    count_strs += 1
    stroka = input("Enter a stroka: ")
    if 'кот' in stroka:
        for letters in range(len(stroka)):
            if stroka[letters] == 'к':
                print(count_strs, letters+1)