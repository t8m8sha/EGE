count = 0
for n in range(1, 100_000):
    num = hex(n)[2:]
    if num.count("b") % 2 == 0:
        num = '1' + num
    else:
        num = num + '1'
    num = int(num,16)
    if 9 < num < 100:
        count += 1

print(count)