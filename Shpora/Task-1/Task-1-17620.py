from itertools import permutations

matrix = '256 134 267 27 16 135 34'.split()
graph = 'AB AF FB FE BD ED EC DG CG'.split()

print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix [i.index(y)] for x,y in graph):
        print(*i)

#otvet 9