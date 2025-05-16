from string import ascii_uppercase,digits
def convert(num,sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]



for x in range(0,10_000):
    num = 6**900 + 6**10 - x
    num = convert(num,6)
    if num.count('3') == num.count('5'):
        print (x)
