def bubble_sort(s):
    for i in range(len(s)-1):
        for j in range(len(s)-i-1):
            if s[j] > s[j+1]:
                s[j],s[j+1] = s[j+1],s[j]
        
    return s


a = [0,4,12,10,7,3,9,1,5,6]
print(bubble_sort(a))
