def s(a):
    s = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            s += a[i][j]
    return s

def p(a):
    s = 1
    for i in range(len(a)):
        for j in range(len(a[i])):
            s *= a[i][j]
    return s

a = [
    [1,2,3],
    [3,2,1],
    [9,8,7]
    ]
print('The sum of all elements in this matrix is {}, the product of all elements in this matrix is {}'.format(s(a),p(a)))
