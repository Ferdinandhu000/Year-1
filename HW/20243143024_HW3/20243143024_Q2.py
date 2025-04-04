try:
    x = eval(input('Please enter x here:'))
    if (x<0):
        y = -1
        print('y = {}'.format(y))
    elif(x==0):
        y = 0
        print('y = {}'.format(y))
    elif(x>0):
        y = 1
        print('y = {}'.format(y))
except NameError:
    print('Please enter a correct number!')
    
