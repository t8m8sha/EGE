ans = []
for N in range(1,100_000):
    R = bin(N)[2:]
    if sum(map(int, R)) % 2 == 0:
        R = R + '0'
        R = '10' + R[2:]
    else:
        R = R + '1'
        R = '11' + R[2:]
    if int(R,2) >= 16:
        ans.append(N)
print (min(ans))
