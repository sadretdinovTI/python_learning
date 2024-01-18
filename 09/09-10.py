nums_list = []
for num in range(int(input("Enter a number of numbers: "))):
    nums_list.append(int(input('Enter a number: ')))
p = int(input("Enter a number p: "))
q = int(input("Enter a number q: "))
print(sum(nums_list[p-1:q]))