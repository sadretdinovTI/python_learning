login = input('Введите логин: ')
reserv = input('Введите адрес: ')
if '@' in login:
    print('Некорректный логин')
    if '@' not in reserv:
        print('Неккоректный адрес')
print('OK')