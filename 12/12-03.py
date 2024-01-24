nums = [int(num) for num in input('Enter nums: ').split()]
start_end = [int(num) for num in input('Start and end: ').split()]
for num in start_end:
    if num < 0 or num > len(nums):
        print('Error')
print(sum(nums[start_end[0]:start_end[1] + 1:]))