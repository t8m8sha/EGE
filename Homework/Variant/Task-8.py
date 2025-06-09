cnt = 0
from itertools import product
alph = '0123456789AB'
for i in product(alph,repeat = 5):
    if i.count('7') == 1 and i.count('9') >= 3 and i[0] != '0':
        i = ''.join(i)
        cnt += 1
print(cnt)


