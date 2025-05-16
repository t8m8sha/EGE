with open('24_4643.txt') as file:
    data = file.readline()
    data = data.replace('A', "Z")
    data = data.replace('B',"Z")
    data = data.replace('2','1')
data = data.replace('11Z', 'V')
data = data.replace('Z', ' ')
data = data.replace('1',' ')
data = data.split()
print(len(max(data, key=len)))

