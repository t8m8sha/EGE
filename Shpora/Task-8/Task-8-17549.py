from itertools import product
alph = 'ФОКУС'
alph = sorted(alph)

for pos,val in enumerate(product(alph,repeat = 5), start = 1):
    if 'Ф' not in val and val.count('У') == 2:
        print(pos)

