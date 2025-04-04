def GCD(x,y):
    for i in range(max(x,y),0,-1):
        if(x%i==0 and y%i==0):
            return i
a,b = eval(input())
print(GCD(a,b))
        
