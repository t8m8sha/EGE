with open('24_4544.txt') as file:
    data = file.readline()
ans = 0
data = data.replace('XIX','XI IX')
data = data.split()
print(len(max(data, key=len)))
#293
