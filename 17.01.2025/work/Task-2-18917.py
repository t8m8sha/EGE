print('t,s,r,a')
for t in range(2):
    for s in range(2):
        for r in range(2):
            for a in range(2):
                f = (s or (not r)) and (not(r == a)) and t
                if f:
                    print(t,s,r,a)