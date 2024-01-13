cat_count = 0
first_cat_line = -1
line_count = 1

while True:
    line = input()
    if line == "СТОП":
        break
    if "кот" in line:
        cat_count += 1
        if first_cat_line == -1:
            first_cat_line = line_count
    line_count += 1

print(cat_count, first_cat_line)
