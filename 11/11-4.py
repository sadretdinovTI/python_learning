print(' '.join([str(int(i)**2) for i in '11,12,13,14,15,16,17,18,19,20'.split(',')
                if int(i) % 2 != 0 and str(int(i)**2)[-1] != '9']))