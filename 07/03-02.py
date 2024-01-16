password1 = input('Введите пароль: ')
if len(password1) < 8:
    print('Короткий!')
else:
    password2 = input('Подтвердите пароль: ')
    if password1 == password2:
        print('ОК')
    else:
        print('Различаются!')