citys = set()
count_citys = int(input('Введите число городов: '))

for i in range(count_citys):
    city = input('Введите город: ')
    citys.add(city)

dop_city = input('Введите новый город: ')
if dop_city in citys:
    print('TRY ANOTHER')
else:
    citys.add(dop_city)
    print('OK')

