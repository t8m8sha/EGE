cnt = 0
from itertools import product
alph = '0123456789ABCDE'
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] != '0' and i.count('8') == 1:
        if i.count('A') + i.count('B') + i.count('C') + i.count('D') + i.count('E') >= 2:
            cnt += 1
print(cnt)


