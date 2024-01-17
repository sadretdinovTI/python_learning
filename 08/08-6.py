max_symbols = int(input('Enter max symbols: '))
header_count = int(input('Enter count of headers: '))
for i in range(header_count):
    header = input('Enter: ')
    if len(header) < 4:
        break
    if len(header) >= (max_symbols-3):
        print(header[:(max_symbols-3)] + '...')
    else:
        print(header)

