#iterative method
def fibo():
    a,b = 0,1
    ls = []
    for i in range(100):
        a,b = b,a+b
        ls.append(a)
    return ls

print(fibo())




#recursive method
def Fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)

for i in range(1,101):
    print(Fibo(i))
