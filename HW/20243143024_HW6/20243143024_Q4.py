stu = {'张三': 90, '李四': 80, '钱二': 100, '赵大': 70, '孙五': 60}
def system_searching(dic):
    k = []
    v = []
    s = 0
    H = float('-inf')
    L = float('inf')
    for key in dic:
        k.append(key)   
    for value in dic.values():
        v.append(value)
    for i in tuple(v):
        if i > H:
            H = i
        if i < L:
            L = i
        s += i
        mean = s/len(v)
    while True:
        t = input('Press 1 to get the highest and lowest score;\nPress 2 to get the average;\nInput a student\'s name to get his/her admission score;\nPress 0 to quit:\n')
        if t == '0':
            return 0
        else:
            if t == '1':
                print('The highest score is {}\nThe lowest score is {}\n'.format(H,L))
            elif t == '2':
                print('The average is {}\n'.format(mean))
            else:
                if t in k:
                    print('{}\'s score is {}\n'.format(t,dic.get(t)))
                else:
                    print('Student not found.\n')

system_searching(stu)

