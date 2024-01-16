word = input()
shortest = word
longest = word
while True:
    next_word = input()
    if next_word == 'стоп':
        break
    if len(next_word) > len(longest):
        longest = next_word
    if len(next_word) < len(shortest):
        shortest = next_word
if len(set(shortest) - set(longest)) == 0:
    print('Да')
else:
    print('Нет')