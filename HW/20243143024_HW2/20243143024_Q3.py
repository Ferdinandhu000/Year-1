w1_earth = eval(input('input the weight of the object on earth:'))
w1_moon = w1_earth * 0.165
w2_earth = w1_earth * (1.01)**10
w2_moon = w2_earth * 0.165
print('After 10 years, the weight of the object on earth is {}, and {} on moon.'.format(w2_earth,w2_moon))
