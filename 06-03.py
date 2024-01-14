eng_count = int(input("How many english: "))
ger_count = int(input("How many germany: "))
list_eng = set()
list_ger = set()

for i in range(eng_count):
    eng_name = input("ENG learning name: ")
    list_eng.add(eng_name)
for i in range(ger_count):
    ger_name = input("GER learning name: ")
    list_ger.add(ger_name)

sym_diff = list_eng.symmetric_difference(list_ger)
print(len(sym_diff))

