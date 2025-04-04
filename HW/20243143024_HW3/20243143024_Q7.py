ls = list(input())
ans = ''
for i in ls:
    if ('a' <= i <= 'z'):
        i = chr(ord(i)-32)
    elif('A' <= i <= 'Z'):
        i = chr(ord(i)+32)
    ans += i
print(ans)
