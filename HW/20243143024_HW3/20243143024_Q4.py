a,b = eval(input('Please enter a and b here:'))
for i in range(min(a,b),0,-1):
    if(a%i==0 and b%i==0):
        print('The Greatest Common Divisor is ',i)
        break
j = 1
while True:
    if(j%a==0 and j%b==0):
        print('The Least common Multiple is ',j)
        break
    else:
        j += 1
