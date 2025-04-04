a,b,c = eval(input('Please input lengths of three line segments that form a triangle: '))
if(a+b>c and a+c>b and b+c>a):
    if(a==b==c):
        print('This is a equilateral triangle!')
    elif(a==b or a==c or b==c):
        if(a**2 + b**2 == c**2  or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
            print('This is a isosceles right triangle!')
        else:
            print('This is a isosceles triangle!')
    elif(a**2 + b**2 == c**2  or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
        print('This is a right-angled triangle!')
    else:
        print('This is a normal triangle!')
else:
    print('Three lines can not form a triangle!')
