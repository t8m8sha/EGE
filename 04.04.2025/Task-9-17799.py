from itertools import permurations
ans = []
alph = sorted("АРГУМЕНТ")
for pos, val in enumerate(product(alph, repeat=4), start=1):
    if len(set(val)) == len(val):
        if val == ''.join(sorted(val)):
            ans.append(pos)
print(max(ans))


