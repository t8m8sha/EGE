print('w x y z fS')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (y<=x) and not z and w
                if f:
                    print(w,x,y,z)
#otvet wxyz