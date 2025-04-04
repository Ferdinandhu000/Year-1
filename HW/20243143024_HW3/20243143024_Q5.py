w = 100
for i in range(20):
    for j in range(33):
        k = 100-i-j
        cost = 5*i + 3*j + k/3
        if (cost <= w):
            print('{} cocks, {} hens and {} chicks'.format(i,j,k))
