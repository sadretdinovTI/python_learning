eng_count = int(input("How many english: "))
ger_count = int(input("How many germany: "))
list_peoples = set()
two_language = 0

for i in range(eng_count+ger_count):
    name = input("Enter name: ")
    if name in list_peoples:
        two_language += 1
    list_peoples.add(name)

one_language = len(list_peoples) - two_language
if one_language == 0:
    print("No")
else:
    print(one_language)