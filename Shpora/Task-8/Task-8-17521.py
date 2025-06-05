cnt = 0
from itertools import product

alph = '01234567'
alphchet = '0246'
alphnechet = '1357'
    
for i in product(alph,repeat = 5):
    if  i[0] != '0' and i[0] not in alphnechet and i[4] != '2' and i[4] != '6' and i.count('7') <= 2:
        cnt += 1
print(cnt)