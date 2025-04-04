def f1(*x):
    x_max = max(x)
    x_min = min(x)
    ans = x_min/x_max
    return ans

def f2(*x):
    s = 0
    for i in x:
        s += i
    avg = s/len(x)
    ans = s/avg
    return ans

def f3(*x):
    x_max = max(x)
    x_min = min(x)
    deviation = x_max - x_min
    return deviation

a = eval(input())
print(f1(*a))
print(f2(*a))
print(f3(*a))
