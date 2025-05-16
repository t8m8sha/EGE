from string import digits,ascii_uppercase
def convert(num,sys):
    res = ''
    alph = digits + ascii_uppercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for n in range(1,100_000):

