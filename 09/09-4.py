post = list()
for message in range(int(input('Enter number of lines: '))):
    post.append(input('Enter a message:'))
for new_message in range(int(input('Enter number of lines: '))):
    print(post[int(input("Enter new message: ")) - 1])