with open('24_19489.txt') as file:
    data = file.readline()

data = data.split('WWF')
ans = 0

print(len(max(data, key=len)))
