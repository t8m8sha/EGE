from string import digits,ascii_uppercase
def convert(num, sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for x in range(1,2031):
    num = 6**260 + 6**160 + 6**60 - x
    num6 = convert(num,6)
    if num6.count('0') == 202:
        print(x)



