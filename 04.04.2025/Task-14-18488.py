from string import digits,ascii_uppercase
def convert(num,sys):
    alph = digits + ascii_uppercase
    result = ""
    while num:
        result += alph[num%base]
        num //= base
    return result[::-1]
count = 0
for x in range(0,1_000_000):
    num = 7**666 + 7**333 + 49**x - 343
    num1 = convert(num,7)
    if "6" * 49 in num:
        print(min(x))

