list_nums = []
for lines in range(int(input('Enter a number of numbers: '))):
    list_nums.append(int(input('Enter a number: ')))
for num in range(len(list_nums) - 1):
    print(list_nums[num] + list_nums[num+1])