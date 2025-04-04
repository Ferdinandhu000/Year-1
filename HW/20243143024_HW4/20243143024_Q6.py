#iterative method
def f(a):
    n = 0
    a = str(a)
    if int(len(a)/2)%2 == 0:
        for i in range(int(len(a)/2)):
            if a[0]==a[-1]:
                a = a[1:-1]
            else:
                return False
    else:
        for i in range(int((len(a)-1)/2)):
                    if a[0]==a[-1]:
                        a = a[1:-1]
                    else:
                        return False

inp = input('input tring here: ')
if f(inp)==False:
    print('This is not a palindrome string!')
else:
    print('This is a palindrome string!')

