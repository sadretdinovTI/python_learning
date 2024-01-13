war = 'Евразия'
peace = 'Остазия'
answer = 0
count_strs = int(input('количество команд от правительства: '))
for i in range(count_strs):
    question = input('Введите одно из: С кем война?; С кем мир?; Меняем: ')
    if question == 'С кем война?':
        answer == war
        print(war)
    if question == 'С кем мир?':
        answer == peace
        print(peace)
    if question == 'Меняем':
        war, peace = peace, war


