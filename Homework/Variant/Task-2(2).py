print('W X Y Z F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((w<=y)<= x) or (not z)
                if not f:
                    print(w,x,y,z)
