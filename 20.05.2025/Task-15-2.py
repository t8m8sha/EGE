from itertools import combinations
def f(x,A1,A2):
    P = 256 < x < 1001
    Q = 4 < x < 101
    R = 98 < x < 259
    A = A1 <= x <= A2
    return(A <= R) and (not(A <= P) <= Q)
ans = []
line = [x + eps for x in range(4,1000) for eps in [0,0.1,0.9]]
for A1,A2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(A1-A2)

print(min(ans))

