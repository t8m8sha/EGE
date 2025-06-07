from string import digits,ascii_uppercase
def convert(num,sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res +=alph[num%sys]
        num //= sys
    return res[::-1]

num = 343**1515 - 6 * 49**1520 + 5 * 49**1510 - 3 * 7**1530 - 1550
num1 = convert(num,7)
count = num1.count('0')
print(count)