words = input('Enter a words: ').split()
print('[' + ', '.join('"' + word + '"' for word in words) + ']')