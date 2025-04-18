from itertools import permutations

alph = 'АБ АВ АГ БГ ВГ ГЕ ГД ЕЗ ДЖ ЗЖ ГЗ ГЖ'.split()
matrix = '235 13 12345678 36 13 347 368 37'.split()

print (*range(1,13))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)]
            for x,y in alph):
        print(*i)