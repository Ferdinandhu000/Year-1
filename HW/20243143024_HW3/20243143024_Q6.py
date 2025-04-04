ls = list(input())
letter = 0
digit = 0
space = 0
other = 0
for i in ls:
    if ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
        letter += 1
    elif('0' <= i <= '9'):
        digit += 1
    elif(ord(i) == 32):
        space += 1
    else:
        other += 1
print('letter: ',letter,'\ndigit: ',digit,'\nspace: ',space,'\nother character: ',other)
