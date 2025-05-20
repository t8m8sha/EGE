from re import *
with open('24_17641.txt') as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = fr'({number}[+*])+{number}'

matches = finditer(pattern,data)
matches = [match.group() for match in matches]

ans = 0
for match in matches:
    if eval(match) == 0:
        ans = max(ans,len(match))
    else:
        for l in range(len(match) +1):
            for r in range(len(match),l,-1):
                sub_str = match[:r].strip('+*')
                if len(sub_str) < 2:
                    break
                if sub_str[0] =='0' and sub_str[1] in '0123456789':
                    continue
                if eval(match) == 0:
                    ans = max(ans, len(sub_str))
                    break

print(ans)