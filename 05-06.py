count_strokes = 0
found_count = 0
total = 0
while True:
    num = int(input("Число: "))
    count_strokes += 1
    total += num
    if total == 10:
        found_count = count_strokes
        break
    if num == 0:
        break
print(found_count)





