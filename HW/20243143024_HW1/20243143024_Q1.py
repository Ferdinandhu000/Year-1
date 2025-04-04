import math
a = 5170
b = 377800
c = (a + b) / 2
x1 = (-b + math.sqrt(b**2 - 4 *a * c)) / (2 * a)
x2 = (-b - math.sqrt(b**2 - 4 *a * c)) / (2 * a)
delta = b**2 - 4 *a * c
if(delta < 0):
    print('The equation has no real root!')
elif(delta == 0):
    print('The equation has only one root ',x1)
else:
    print('The equation has two roots ',x1,' and ',x2 )

