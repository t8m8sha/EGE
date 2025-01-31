for x in range(1,25)[::-1]:
    num1 = 11353**25 * x * 12**25 + 135**25 * x * 21**25
        if num1 % 24 == 0:
            print int(num1 // 24)
            break