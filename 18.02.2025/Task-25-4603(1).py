from itertools import product
for r in range(4):
    for z in product('0123456789',repeat=r):
        z = ''.join(z)

        num = (f'1234{z}7')
        if num <=10**8 and num%141 == 0:
            ans.append([num,num//141])
ans = sorted(ans)
for i in ans:
    print(num,num//141)