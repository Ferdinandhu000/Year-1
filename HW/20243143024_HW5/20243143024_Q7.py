def selection_sort(s):
    for i in range(len(a)-1):
        minIdx = i
        for j in range(i+1,len(s)):
            if s[minIdx]>s[j]:
                minIdx = j
        if minIdx != i:
            s[i],s[minIdx] = s[minIdx],s[i
                                         ]
    return s
                


a = [0,4,12,10,7,3,9,1,5,6]
print(selection_sort(a))
