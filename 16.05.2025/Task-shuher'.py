from string import ascii_uppercase,digits
def convert(num,sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


data = '0123456789'
for l in range(len(data)):
    for r in range(len(data),l,-1):
        ps = i[l:r]
        if int(ps,16) % 6 == 0:
            ans = max(ans,lrn(ps))
            break

print(ans)
