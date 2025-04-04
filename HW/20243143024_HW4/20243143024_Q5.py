def prime_num(n):
    a = 0
    if n==0 or n==1:
        return False 
    if n==2:
        return True
    for i in range(2,n):
        if n%i!=0:
            a += 1
    if a==n-2:
        return True
    else:
        return False

w = int(input('Please enter n here: '))
for e in range(w):
    if prime_num(e):
        print('{} is a prime number!'.format(e))
    else:
        print('{} is not a prime number!'.format(e))
        
        
