def s_upper(a):
    s = 0
    for i in range(len(a)):
        for j in range(i,len(a[i])):
            s += a[i][j]
    return s

def p_upper(a):
    s = 1
    for i in range(len(a)):
        for j in range(i,len(a[i])):
            s *= a[i][j]
    return s
            


a = [
    [1,2,3],
    [3,2,1],
    [9,8,7]
    ]
print('The sum of all upper triangular elements in this matrix is {}\nThe product of all upper triangular elements in this matrix is {}'.format(s_upper(a),p_upper(a)))
