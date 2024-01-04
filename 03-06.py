while True:
    password1 = input("Введите пароль: ")
    password2 = input("Повторите пароль: ")
    if len(password1) < 8:
        print('Короткий!')
        pass
    elif '123' in password1:
        print('Простой!')
        pass
    elif password1 != password2:
        print('Различаются!')
        pass
    else:
        print('OK')
        break
