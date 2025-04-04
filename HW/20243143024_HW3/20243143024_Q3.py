n = int(input('Please enter n here:'))
ans = 0
for i in range(n+1):
    ans += (-1)**(i+1) * i**2
print(ans)
