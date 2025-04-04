def swapLowerUpper(s):
    res = list(s)
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            res[i] = chr(ord(s[i])-32)
    return ''.join(res)

def swapUpperLower(s):
    res = list(s)
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            res[i] = chr(ord(s[i])+32)
    return ''.join(res)


a = input()
print(swapLowerUpper(a))
print(swapUpperLower(a))
