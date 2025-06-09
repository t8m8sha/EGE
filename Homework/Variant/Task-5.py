ans = []
for n in range(1,100_000):
    R = bin(n)[2:]
    if n % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    result = int(R,2)
    if n <= 12:
        ans.append(result)
print(max(ans))
