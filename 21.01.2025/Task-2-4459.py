print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((not x) <= y) and ((not y) == z) and w
                if f:
                    print(w,x,y,z,f)
#Otvet zyxw