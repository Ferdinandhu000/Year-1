def factorial(n):
    ans = 1
    if n==1:
        return ans
    else:
        return n * factorial(n-1)

def func(x):
    i = 1
    val = 0
    while True:
        val += (-1)**(i+1)*(x**(2*i-1))/factorial(2*i-1)
        if abs(x**(2*i-1)/factorial(2*i-1)) < 1*10**(-5):
            break
        else:
            i += 1
    return val

x = eval(input('Please input x here: '))
print(func(x))
