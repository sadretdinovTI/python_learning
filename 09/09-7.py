messages_list = []
keywords_list = []
for lines in range(int(input("Enter num of lines: "))):
    messages_list.append(input("Enter message: "))
for search_lines in range(int(input("Enter num of search lines: "))):
    keywords_list.append(input("Enter the keyword: "))
for message in messages_list:
    all_keywords_found = True
    for keyword in keywords_list:
        if keyword not in message:
            all_keywords_found = False
            break
    if all_keywords_found:
        print(message)
