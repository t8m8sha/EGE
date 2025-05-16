from string import ascii_uppercase

with open('24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i,'')
data = data.split()


print (len(max(data, key=len)))

ans = 0
for i in data:
    if int(i,16) % 6== 0:
        ans = max(ans,len(i))
    else:
        for l in range(len(data)):
            for r in range(len(data), l, -1):
                ps = i[l:r]
                if int(ps, 16) % 6 == 0:
                    ans = max(ans, lrn(ps))
                    break

        print(ans)