from itertools import permutations

alph = "АБ АГ АВ БВ БГ ГД ВД ДЕ ДЗ ЕЗ ЕЖ ЖЗ ГЖ".split()
matrix = "256 1458 478 237 126 158 348 2367".split()

print (*range(1, 14))

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)]
        for x,y in alph):
            print (*i)