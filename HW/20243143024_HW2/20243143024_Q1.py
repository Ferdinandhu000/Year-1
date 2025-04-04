import math
ls = input('Please input a, b and alpha:').split()
a = eval(ls[0])
b = eval(ls[1])
alpha = eval(ls[2])
S = a * b * math.sin(alpha*math.pi/180) / 2
c = (a**2 + b**2 - math.cos(alpha*math.pi/180) * 2 * a * b)**0.5
C = a + b + c
print('The triangle wth side lengths {:.1f},{:.1f}, and angle {} degree has an area of {:.2f} and a perimeter of {:.2f}.'.format(a,b,alpha,S,C))
