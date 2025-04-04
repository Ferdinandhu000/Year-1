def s_outer(a):
    s = 0
    for t in range(len(a[0])):
        s += a[0][t]
    for i in range(1,len(a)-1):
        s += ( a[i][0]+a[i][-1] )
    for v in range(len(a[-1])):
        s += a[-1][v]
    return s

def p_outer(a):
    s = 1
    for t in range(len(a[0])):
        s *= a[0][t]
    for i in range(1,len(a)-1):
        s *= ( a[i][0]*a[i][-1] )
    for v in range(len(a[-1])):
        s *= a[-1][v]
    return s

a = [
    [1,2,3],
    [3,2,1],
    [9,8,7]
    ]
print('The sum of all elements in the outermost elements in this matrix is {}\nThe product of all elements in the outermost elements in this matrix is {}'.format(s_outer(a),p_outer(a)))
