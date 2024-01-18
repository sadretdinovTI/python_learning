num_kids = int(input("Enter number of kids: "))
names_list = []
for name in range (num_kids):
    names_list.append(input("Enter your name and mark: "))
print()
for name in names_list:
    if int(name[-1]) >= 4:
        print(name)