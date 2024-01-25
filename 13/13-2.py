phone_dict = {}
for num in range(int(input())):
    phone, name = input().split()
    if name in phone_dict:
        phone_dict[name].append(phone)
    else:
        phone_dict[name] = phone
for num in range(int(input())):
    found_name = input()
    if found_name in phone_dict:
        print(phone_dict[found_name])
    else:
        print("Not found")