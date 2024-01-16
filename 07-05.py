first_word = input('Enter a word: ')
second_word = input('Enter a word: ')
while first_word[-1] == second_word[0]:
    first_word = second_word
    second_word = input('Enter a word: ')
print(second_word)