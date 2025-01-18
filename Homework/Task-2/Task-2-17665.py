print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (z <= (not(y<=x))) or w
                if not f:
                    print (w,x,y,z,f)
##
Ответ:
Z - 111
y - 100
x - 101
w - 000
f - 000

