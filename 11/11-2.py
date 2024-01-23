nums = [int(input('Enter a number: ')) for i in range(int(input('Enter num of nums: ')))]
print('\n'.join(i * '*' for i in nums))