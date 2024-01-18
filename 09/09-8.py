soups_list = ['щи', 'борщ', 'щавелевый суп', 'овсяной суп', 'суп по-чабански']
for days in range(int(input('How many days: '))):
    print(soups_list[days % 5])