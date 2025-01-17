print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (z and not w) or (z == x) or y
                if not f:
                    print(w,x,y,z,f)
#2 ответ: wzyx ( у w и у x одни и те же наборы цифр