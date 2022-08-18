i, y = 0, 0

for i in range(2, 10): 
    print('## %d단 ##' % i)
    for j in range(1, 10):
            print('%d x %d = %d' % (i, j, i*j) )
    print()