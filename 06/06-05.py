eng_count = int(input("How many english: "))
ger_count = int(input("How many germany: "))
fra_count = int(input("How many france: "))

eng_set = set()
ger_set = set()
fra_set = set()

for i in range(eng_count+ger_count+fra_count):
    name = input("Enter your name: ")
    if i < eng_count:
        eng_set.add(name)
    elif i < eng_count+ger_count:
        ger_set.add(name)
    else:
        fra_set.add(name)
two_languages = (eng_set & ger_set) | (eng_set & fra_set) | (ger_set & fra_set)
print(len(two_languages))
