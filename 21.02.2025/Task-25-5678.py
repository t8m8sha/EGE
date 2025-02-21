from itertools import product
ans=[]
for r1 in range(3):
    for z1 in product('1234567890',repeat=r1):
        z1 =''.join(z1)
        for r2 in range(3 - r2):
            for z2 in product('1234567890',repeat=r2):
                z2=''.join(z2)
                num = int(124{r1}5{r2}79)

ans = sorted(ans)
for i in ans:
    print(*i)


