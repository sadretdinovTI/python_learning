first_line = input('Enter: ')
num_lots, final_sum = int(first_line[:4]), int(first_line[4:])
error_lines = []
false_sum = []
for line in range(num_lots):
    lot_line = input('Enter a number: ')
    lot, num, summ = int(lot_line[:7]), int(lot_line[8:12]), int(lot_line[13:])
    false_sum.append(lot*num)
    if lot * num != summ:
        error_lines.append(line+1)
print(final_sum - sum(false_sum))
for line in error_lines:
    print(line, end=' ')