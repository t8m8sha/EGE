with open('24_3228.txt') as file:
    data = file.readline()
while "AC" in data and 'AB' in data:
    data = data.replace("AC",'1')
    data = data.replace('AB','1')
    for i in 'ABC':
        data = data.replace(i,' ')
data = data.split()
print(len(max(data,key=len)))