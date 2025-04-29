from itertools import product

alph = '0123456789ABCD'

cnt = 0
for val in product(alph,repeat=8):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 2:
        if sum([1 for i in val if i in 'ABCD']) <= 4:
            cnt += 1
print(cnt)