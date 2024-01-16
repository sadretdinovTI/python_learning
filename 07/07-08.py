num = int(input("Enter a number (> 1kkk): "))
while num < 1000000000:
    x = int(str(num)[0])
    num *= x
    if x == 1:
        break
print(num)
