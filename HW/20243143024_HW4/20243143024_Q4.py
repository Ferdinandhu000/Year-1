def Narci(n):
    n = str(n)
    try:
        if int(n)== int(n[0])**3 + int(n[1])**3 +int(n[2])**3:
            print('It is a Narcissistic number!')
        elif int(n) != int(n[0])**3 + int(n[1])**3 + int(n[2])**3:
            print('It isn\'t a Narcissistic number!')
    except IndexError:
        print('Please input a correct number!')


    print('The following are all the Narcissistic number: ')
    for i in range(100,1000):
        i = str(i)
        if int(i)== int(i[0])**3 + int(i[1])**3 +int(i[2])**3:
            print(i)


a = int(input('Please input a three-digit integer: '))
Narci(a)
