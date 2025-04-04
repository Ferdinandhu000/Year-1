def transpose(a):
    for i in range(len(a)):
        for j in range(i,len(a[i])):
            a[i][j] , a[j][i] = a[j][i] , a[i][j]
    return a
            
            


a = [
    [1,2,3],
    [3,2,1],
    [9,8,7]
    ]
print(transpose(a))
