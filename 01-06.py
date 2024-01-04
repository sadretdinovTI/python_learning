print('Любите ли вы котиков?')
answer1 = input()
print('Умеете ли вы программировать?)')
answer2 = input()
if answer1 == 'да' and answer2 == 'да':
    print('Вы обладаете незаурядным умом.')
elif answer1 == 'нет' and answer2 == 'да':
    print('Вы преобладаете незаурядным умом.')
elif answer1 == 'нет' and answer2 == 'нет':
    print('Вы обладаете заурядным умом.')
elif answer1 == 'да' and answer2 == 'нет':
    print('Вы обладаете кошачим умом.')
else:
    print('Произошла ошибка, завершаем работу...')