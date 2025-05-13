with open('24_4627.txt') as file:
    data = file.readline()

while "NPO" in data and "PNO" in data:
    data = data.replace("NPO", '1')
    data = data.replace("PNO",'1')
    for i in 'NOP':
        data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
