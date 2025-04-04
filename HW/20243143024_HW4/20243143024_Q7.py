def Hanoi(n,A,B,C):
    if n==1:
        print('Move {} from {} to {}'.format(n,A,C))
    else:
        Hanoi(n-1,A,C,B)
        print('Move {} from {} to {}'.format(n,A,C))
        Hanoi(n-1,B,A,C)

n = int(input('Please enter n here: '))
Hanoi(n,'A','B','C')
