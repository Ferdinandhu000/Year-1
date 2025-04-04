import math
a = 5170
b = 3778
alpha = (a + b) / 2
s = 0.5 * a * b * math.sin(alpha * math.pi / 180)
c = b**2 + a**2 - 2*a*b*math.cos(alpha * math.pi / 180)
print('The area is ',s)
print('The perimeter is ',a + b + c)
