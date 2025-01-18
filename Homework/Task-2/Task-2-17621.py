print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not(x<=z) or (y==w) or y
                if not f:
                    print(w, x, y, z, f)
##
z 110
x 010
y 000
w 111
f 000