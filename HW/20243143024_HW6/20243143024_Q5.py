stu = {
    '张三': [90, 79, 92],
    '李四': [80, 85, 78],
    '钱二': [100, 90, 95],
    '赵大': [70, 56, 82],
    '孙五': [60, 87, 75]
}

def system_searching(dic):
    k = []
    v = []
    for key in dic:
        k.append(key)   
    for value in dic.values():
        v.append(value)
    
    while True:
        v1 = []
        s = 0
        i = 0
        H = float('-inf')
        L = float('inf')
        t = input('Enter the index of the course to get the students\' names who get the highest and lowest score and also the average score of this course;\nInput a student\'s name to get his/her highest and lowest score;\nPress 0 to quit:\n')
        if t == '0':
            return 0
        elif t.isdigit():
            index = eval(t) -1
            for c in range(len(v)):
                v1.append(v[c][index])
            for i in v1:
                s += i
                if i > H:
                    H = i
                if i < L:
                    L = i
            person_H = k[v1.index(H)]
            person_L = k[v1.index(L)]
            mean = s/len(v1)
            print('In course {}, {} got the highest score:{} and {} got the lowest score:{}\n'.format(eval(t),person_H,H,person_L,L))
        elif t in k:
            v2 = []
            v2 = dic.get(t)
            s = 0
            h = float('-inf')
            l = float('inf')
            for j in v2:
                s += j
                if j > h:
                    h = j
                if j < l:
                    l = j
            mean_ = s/len(v2)
            print('{} got the highest score:{} and got the lowest score:{}, the average score is {}\n'.format(t,h,l,mean_))
        else:
            print('Student not found.\n')
            
system_searching(stu)
