recipe = [input('step: ') for step in range(int(input('How many steps: ')))]
print(', '.join(step for step in recipe if 'лук' not in step))