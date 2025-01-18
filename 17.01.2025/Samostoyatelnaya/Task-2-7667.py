print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a <= b)== c) or (not d) or (d  <= (not a))
                if not f:
                    print (a, b, c, d, f)