def Pascal(n):
    a = [[0 for m in range(n)] for x in range(n)]
    for q in range(n):
        a[0][q] = 1
        a[q][q] = 1
        a[q][0] = 1
    for i in range(2,n):
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for t in range(len(a)):
        for v in range(t+1):
            print(a[t][v],end = '  ')
        print('\n')

n = int(input('Please input n here:'))
Pascal(n)
