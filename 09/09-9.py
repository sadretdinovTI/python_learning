vklad_3x = []
for client in range(int(input("Enter number of clients: "))):
    vklad_3x.append((input("Enter sum: ")))
for sum in range(len(vklad_3x)):
    print(vklad_3x[sum])
print()
for sum3x in range(len(vklad_3x)):
    print(int(vklad_3x[sum3x]) * 3)