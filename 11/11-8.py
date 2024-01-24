get_request = input('Enter url: ').split('?')[1]
print(get_request.split('&')[0][2::])
