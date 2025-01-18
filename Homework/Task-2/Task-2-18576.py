print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not(w <= (x == (y or y))) and (z <= x)
                if f:
                    print (w,x,y,z,f)
##
y 001
x 110
w 111
z 100
f111