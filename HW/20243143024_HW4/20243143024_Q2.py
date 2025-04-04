def f(n):
    for i in range(1,n+1):
        m = str(i)*(2*i-1)
        print('{:^17}'.format(m))
a = int(input())
f(a)
