white_list = [input('Enter a word: ') for words in range(int(input("Enter number of words: ")))]
for num_requests in range(int(input("Enter number of requests: "))):
    request = input("Enter a word: ")
    if request in white_list:
        print(request)