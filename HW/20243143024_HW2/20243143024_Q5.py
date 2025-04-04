num = input('Input a 5-digit number here:')
a = 0
for i in range(2):
    if num[i] == num[4-i]:
        a += 1
        continue
    else:
        print('The number is not a palindrome!')
        break
if a==2:
    print('The number is a palindrome!')
