for n in range(5,100_000):
    num = bin(n)[2:]
    if num.count('1') > num.count('0'):
        num = num + '0'
    else:
        num = num + '1'
    if len(num) % 2 == 0:
        num = num[:len(num) // 2 - 1] + num[len(num) //  2 + 1:]
    else:
        num = num[:len(num) // 2 - 1]+ num[len(num) // 2:]
    num = int(num,2)
    if num == 52:
        print(num)