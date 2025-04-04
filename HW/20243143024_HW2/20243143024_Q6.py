psw = input('Input your password here:')
n = int(input('Input your shift value:'))
cphr = []
for i in range(len(psw)):
    if ord(psw[i])>=48 and ord(psw[i])<=57:
        cphr.append(chr((ord(psw[i])-48+n)%10+48))
    elif ord(psw[i])>=65 and ord(psw[i])<=90:
        cphr.append(chr((ord(psw[i])-65+n)%26+65))
    elif ord(psw[i])>=97 and ord(psw[i])<=122:
        cphr.append(chr((ord(psw[i])-97+n)%26+97))
    else:
        print('error!')
print('Your new cipher is '+''.join(cphr))
