book_lib = int(input())
book_list = int(input())
books_set = set()

for i in range(book_lib):
    book_name = input()
    books_set.add(book_name)
for i in range(book_list):
    book_name = input()
    if book_name in books_set:
        print('YES')
    else:
        print('NO')