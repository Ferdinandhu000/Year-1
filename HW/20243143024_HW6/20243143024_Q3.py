def integral(f,x1,x2):
    val = 0
    dx = (x2 - x1)/1000
    for i in range(1000):
        f1 = eval(f.replace('x',str(x1+i*dx)))
        f2 = eval(f.replace('x',str(x1+(i+1)*dx)))
        f0 = (f1 + f2)/2
        val += f0*dx
    return val

f = input('Please input your function here (enter correct format like 2*x+1): ')
x1 = eval(input('Please input x1 here: '))
x2 = eval(input('Please input x2 here: '))
print(integral(f,x1,x2))
