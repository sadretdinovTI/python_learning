num_nums = int(input('Enter a number of numbers: '))
nums = []
for num in range(num_nums):
    nums.append(int(input('Enter a number: ')))
product = int(input('Enter the product: '))
flag = False
for i in range(num_nums - 1):
    for j in range(i+1, num_nums):
        if nums[i] * nums[j] == product:
            flag = True
            break
if flag:
    print('YES')
else:
    print('NO')