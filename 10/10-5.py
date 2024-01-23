soliders = []
final_soliders = set()
for name in range(int(input("How many soliders: "))):
    soliders.append(int(input('Name: ')))
step = int(input("How many steps: "))
repeat = int(input("How many repeat: "))
soliders *= repeat
for i in range(repeat):
    for j in range(step-1,len(soliders),step):
        final_soliders.add(soliders[j])
for solider in (set(soliders) - final_soliders):
    print(solider)