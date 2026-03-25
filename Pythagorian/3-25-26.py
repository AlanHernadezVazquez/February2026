x = ','
a_range = input('Enter an integer (a): ')
a_range = int(a_range)
b_range = input('Enter an integer (b): ')
b_range = int(b_range)
c_range = input('Enter an integer (c): ')
c_range = int(c_range)
for a in range(1,a_range):
    for b in range(1,b_range):
        for c in range(1,c_range):
            a_s = a ** 2
            b_s = b ** 2
            c_s = c ** 2
            if a_s + b_s == c_s:
                print('Found a Pythagoran Triple:',a,x,b,x,c)

            