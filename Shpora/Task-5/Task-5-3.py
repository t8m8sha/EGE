ans = []
for N in range(1,100_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '0'
        R = '10' + R[2:]
    else:
        R = R + '1'
        R = '11' + R[2:]
    R = int(R,2)
    if R > 50:
        ans.append(N)
print(min(ans))
