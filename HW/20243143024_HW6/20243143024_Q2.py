def func(a,n):
    s = ''
    for i in range(1,n):
        s += a*i + ' + '
    s = s + a*n
    return s

a = input('Please input a here: ')
n = int(input('Please input n here: '))
print(func(a,n))
