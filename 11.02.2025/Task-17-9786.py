with open('17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max([i for i in data if str(i)[-2:] == '25'])
ans = []

for i in range(len(data)- 2):
    num1 = data[i]
    num2 = data[i+1]
    num3 = data[i+2]
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    u3 = len(str(abs(num3))) == 4

    f2 = u1 + u2 + u3 <= 2

    f3 = summ <= max_25

    if f2 and f3:
        ans.append(summ)

print(len(ans)), print (max(ans)